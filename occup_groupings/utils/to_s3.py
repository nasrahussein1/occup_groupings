"""functions to write to s3 bucket
"""
from io import StringIO
import io
import tempfile
import boto3
import joblib

s3_resource = boto3.resource("s3")


def write_to_s3(df, bucket, key):
    """write item to an s3 bucket

    Args:
        bucket: s3 bucket to write to
        key: file path for bucket
        df: dataframe to write

    """

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource.Object(bucket, key).put(Body=csv_buffer.getvalue())


def write_model_to_s3(model, bucket, key):
    """write model to an s3 bucket

    Args:
        bucket: s3 bucket to write to
        key: file path for bucket
        model: trained model

    """

    with tempfile.TemporaryFile() as fp:
        joblib.dump(model, fp)
        fp.seek(0)
        s3_resource.Object(bucket, key).put(Body=fp.read())


def write_plot_to_s3(plot, bucket, key):
    """write plot to an s3 bucket

    Args:
        bucket: s3 bucket to write to
        key: file path for bucket
        plot: visualisation

    """
    img_data = io.BytesIO()
    plot.savefig(img_data, format="png")
    img_data.seek(0)

    s3_resource.Object(bucket, key).put(Body=img_data)
