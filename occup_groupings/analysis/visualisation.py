""" bar chart plotting tfidf scores for a word in the corpus vs occupations
    plot dendrogram to identify the optimal number of clusters
"""
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from occup_groupings.getters.outputs.final_clusters import get_clusters


def feature_bar_chart(df, occupation, feature):
    """bar chart plotting tfidf scores for a word in the corpus vs occupations

    args:
    df: dataframe
    occupation: occupation
    feature: word in the corpus
    """
    plt.style.use("ggplot")

    x = df[occupation]
    y = df[feature]

    plt.figure(figsize=(15, 5))
    plt.bar(x, y, color="blue")
    plt.xticks(fontsize=12)
    plt.xlabel(occupation, fontsize=18)
    plt.ylabel("tfidf scores", fontsize=18)
    plt.title(feature, fontsize=18)

    return plt


def plot_dendrogram(tier_1=None, tier_2=None):

    cluster_assignments = get_clusters()

    if (tier_1 is not None) & (tier_2 is not None):
        cluster_assignments = cluster_assignments[
            (cluster_assignments["tier_1_clusters"] == tier_1)
            & (cluster_assignments["tier_2_clusters"] == tier_2)
        ]

    if (tier_1 is not None) & (tier_2 is None):
        cluster_assignments = cluster_assignments[
            cluster_assignments["tier_1_clusters"] == tier_1
        ]
    if (tier_1 is None) & (tier_2 is None):
        cluster_assignments = get_clusters()

    cols = [
        "occupation",
        "skills_and_occup_descr",
        "tier_1_clusters",
        "tier_2_clusters",
        "tier_3_clusters",
    ]
    tfidf_scores = cluster_assignments.drop(cols, axis=1)
    plt.figure(figsize=(10, 5))
    dendrogram = sch.dendrogram(sch.linkage(tfidf_scores, method="ward"))
    plt.title("Dendrogram")
    plt.xlabel("Occupations")
    plt.ylabel("Euclidean distances")

    plt.tick_params(axis="x", which="both", bottom=False, top=False, labelbottom=False)

    return plt
