"""function to write to s3 bucket
"""
from io import StringIO
import boto3


def write_to_s3(df, bucket, key):
    """write item to an s3 bucket

    Args:
        bucket: s3 bucket to write to
        key: file path for bucket
        df: dataframe to write

    """

    csv_buffer = StringIO()
    df.to_csv(csv_buffer)
    s3_resource = boto3.resource("s3")
    s3_resource.Object(bucket, key).put(Body=csv_buffer.getvalue())
