"""Data getters for processed joined skills data
"""
import pandas as pd
import io
import boto3


def get_joined_skills() -> pd.DataFrame:
    """Load joined skills data

    Returns:
        dataframe: skills and occupation dataframe with text concatenated
    """
    s3 = boto3.client("s3")
    obj = s3.get_object(
        Bucket="occup-groupings-nh", Key="data/processed/occup_skills_join.csv"
    )
    return pd.read_csv(io.BytesIO(obj["Body"].read()))
