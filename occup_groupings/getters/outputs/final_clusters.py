"""Data getters for final clusters
"""
import pandas as pd
import io
import boto3


def get_clusters() -> pd.DataFrame:
    """Load occuplations with assigned clusters

    Returns:
        dataframe: occupations with tfidf values for words i the corpus and cluster assignments
    """
    s3 = boto3.client("s3")
    obj = s3.get_object(
        Bucket="occup-groupings-nh", Key="data/clustering_output/tier_3_clusters.csv"
    )
    return pd.read_csv(io.BytesIO(obj["Body"].read()))
