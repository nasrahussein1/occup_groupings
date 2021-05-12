""" generate bar char visualising word tfidf scores vs occupations
    generate visualisations and generate dendrograms
"""

from occup_groupings.analysis.visualisation import feature_bar_chart
from occup_groupings.analysis.visualisation import plot_dendrogram
from occup_groupings.getters.outputs.tfidf_scores import get_tfidf_scores
from occup_groupings.utils.to_s3 import write_plot_to_s3


if __name__ == "__main__":
    tf_idf_df_assemble_head = (
        get_tfidf_scores().sort_values("assemble", ascending=False).head()
    )
    plt = feature_bar_chart(tf_idf_df_assemble_head, "occupation", "assemble")

    write_plot_to_s3(plt, "occup-groupings-nh", "figures/assemble_tfidf_scores.png")

    plot_dendrogram(None, None)
    write_plot_to_s3(plt, "occup-groupings-nh", "figures/dendrogram.png")

    plot_dendrogram(0, None)
    write_plot_to_s3(plt, "occup-groupings-nh", "figures/dendrogram_cluster_0.png")
