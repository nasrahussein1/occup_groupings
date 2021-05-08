""" run pipeline and produce clustering
"""

from occup_groupings.pipeline.generate_joined_data import generate_data
from occup_groupings.pipeline.tfidf_vectorisation import vectorisation
from occup_groupings.analysis.clustering import tier_1_clustering
from occup_groupings.analysis.clustering import tier_2_clustering
from occup_groupings.analysis.clustering import tier_3_clustering
from occup_groupings.getters.outputs.tfidf_scores import get_tfidf_scores
from occup_groupings.utils.to_s3 import write_to_s3

if __name__ == "__main__":
    generate_data()
    vectorisation()
    tfidf_scores = get_tfidf_scores()
    tier_1_clusters = tfidf_scores.copy()
    y_hc = tier_1_clustering()
    tier_1_clusters["tier_1_clusters"] = y_hc
    tier_2_clusters = tier_2_clustering(tier_1_clusters)
    tier_3_clusters = tier_3_clustering(tier_2_clusters)
    final_occup_hierarchy = tier_3_clusters[
        [
            "occupation",
            "skills_and_occup_descr",
            "tier_1_clusters",
            "tier_2_clusters",
            "tier_3_clusters",
        ]
    ]
    write_to_s3(
        final_occup_hierarchy,
        "occup-groupings-nh",
        "data/clustering_output/new_occup_classification.csv",
    )
