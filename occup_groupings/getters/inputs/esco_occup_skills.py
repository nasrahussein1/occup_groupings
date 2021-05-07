"""Data getters for ESCO data and skills and occup data
"""
import pandas as pd
import io
import boto3


def get_occupations() -> pd.DataFrame:
    """Load occupations

    Returns:
        dataframe: occupations data
    """

    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket="occup-groupings-nh", Key="data/raw/occupations_en.csv")
    return pd.read_csv(io.BytesIO(obj["Body"].read()))


def get_skills() -> pd.DataFrame:
    """Load skills

    Returns:
        dataframe: skills data
    """
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket="occup-groupings-nh", Key="data/raw/skills_en.csv")
    return pd.read_csv(io.BytesIO(obj["Body"].read()))


def get_esco_occup_skills() -> pd.DataFrame:
    """Load esco_occup_skills

    Returns:
        dataframe: ESCO occup_skills data
    """

    s3 = boto3.client("s3")
    obj = s3.get_object(
        Bucket="occup-groupings-nh", Key="data/raw/ESCO_occup_skills.json"
    )

    return pd.read_json(io.BytesIO(obj["Body"].read()))
