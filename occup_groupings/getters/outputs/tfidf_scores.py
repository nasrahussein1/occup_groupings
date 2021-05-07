"""Data getters for processed tfidf scores
"""
import pandas as pd
import io
import boto3


def get_tfidf_scores() -> pd.DataFrame:
    """Load tfidf scores

    Returns:
        dataframe: tfidf scores for each occupation based on words in the corpus
    """
    s3 = boto3.client("s3")
    obj = s3.get_object(
        Bucket="occup-groupings-nh", Key="data/processed/tfidf_values.csv"
    )
    return pd.read_csv(io.BytesIO(obj["Body"].read()))
