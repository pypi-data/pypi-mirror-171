import boto3
from botocore.client import Config
from typing import List, Dict, Any


def s3_upload(
    access_key: str,
    secret_key: str,
    aws_session_token: str,
    target_bucket: str,
    url: str,
    upload_task_id: str,
    file_path: str,
    file_name: str,
) -> bool:
    """
    Connects to the object storage with temporary credentials generated for the
    given user_id, project_id and bucket
    """
    s3 = boto3.resource(
        "s3",
        endpoint_url=url,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=aws_session_token,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )
    s3_object = s3.Object(target_bucket, f"{upload_task_id}/{file_name}")
    with open(file_path, "rb") as file:
        s3_object.put(Body=file)
    return True


def batch(records: List[Dict[str, Any]], batch_size: int):
    """Batches records into batches of size `batch_size`.

    Args:
        records (List[Dict[str, Any]]): List of records to batch.
        batch_size (int): Size of the batches.

    Yields:
        List[Dict[str, Any]]: Batches of records.
    """
    for i in range(0, len(records), batch_size):
        yield records[i : i + batch_size]
