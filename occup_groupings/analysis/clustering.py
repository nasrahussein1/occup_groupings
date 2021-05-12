""" run agglomerative clustering on tfidf scores to group occupations
"""

from occup_groupings import config
from sklearn.cluster import AgglomerativeClustering
from occup_groupings.getters.outputs.tfidf_scores import get_tfidf_scores
from occup_groupings.utils.to_s3 import write_model_to_s3

min_df = config["tfidf_vectorisation"]["params"]["min_df"]
max_df = config["tfidf_vectorisation"]["params"]["max_df"]
stop_words = config["tfidf_vectorisation"]["params"]["stop_words"]
n_clusters_tier_1 = config["clustering"]["params"]["n_clusters_tier_1"]
n_clusters_tier_2 = config["clustering"]["params"]["n_clusters_tier_2"]
affinity = config["clustering"]["params"]["affinity"]
linkage = config["clustering"]["params"]["linkage"]


def tier_1_clustering():
    """train hierarchical cluster model to generate 1st tier of clusters for occupations

    Returns:
        1st tier of occupation groupings
    """
    hc = AgglomerativeClustering(
        n_clusters=n_clusters_tier_1, affinity=affinity, linkage=linkage
    )
    model = hc.fit(
        get_tfidf_scores().drop(["occupation", "skills_and_occup_descr"], axis=1)
    )
    y_hc = model.labels_

    write_model_to_s3(
        model, "occup-groupings-nh", "data/models/tier1/tier_1_clustering_model.sav"
    )  # save tier 1 model to s3 bucket

    return y_hc


def tier_2_clustering(df):
    """train hierarchical clustering model to generate 2nd tier of clusters for occupations
    args:
        df: dataframe

    Returns:
        2nd tier of occupation groupings
    """
    df_copy = df.copy()
    for i in range(n_clusters_tier_1):

        df_i = df[df["tier_1_clusters"] == i]
        tfidf_scores = df_i.drop(
            ["tier_1_clusters", "occupation", "skills_and_occup_descr"], axis=1
        )
        index_values = tfidf_scores.index.values.astype(int)
        hc = AgglomerativeClustering(
            n_clusters=n_clusters_tier_2, affinity=affinity, linkage=linkage
        )
        model = hc.fit(tfidf_scores)

        write_model_to_s3(
            model,
            "occup-groupings-nh",
            "data/models/tier2/tier_2_clustering_model" + "_" + str(i) + ".sav",
        )  # save the tier 2 models to s3 bucket

        y_hc = model.labels_

        df_copy.loc[index_values, "tier_2_clusters"] = y_hc
    return df_copy


def tier_3_clustering(df):

    df_copy = df.copy()
    for i in range(n_clusters_tier_1):
        for j in range(n_clusters_tier_2):

            df_i_j = df[(df["tier_1_clusters"] == i) & (df["tier_2_clusters"] == j)]
            tfidf_scores = df_i_j.drop(
                [
                    "tier_1_clusters",
                    "tier_2_clusters",
                    "occupation",
                    "skills_and_occup_descr",
                ],
                axis=1,
            )
            index_values = tfidf_scores.index.values.astype(int)
            hc = AgglomerativeClustering(
                n_clusters=2, affinity="euclidean", linkage="ward"
            )
            model = hc.fit(tfidf_scores)

            write_model_to_s3(
                model,
                "occup-groupings-nh",
                "data/models/tier3/tier_3_clustering_model"
                + "_"
                + str(i)
                + "_"
                + str(j)
                + ".sav",
            )  # save the tier 3 models to s3 bucket

            y_hc = model.labels_
            df_copy.loc[index_values, "tier_3_clusters"] = y_hc

    return df_copy
