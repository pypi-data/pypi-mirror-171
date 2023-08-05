import os

from azure.storage.blob import BlobClient


def read_jsonlines_blob(url: str, encoding: str = 'UTF-8',
                        logging_enable: bool = True):
    """
    Reads jsonlines document from the specified blob.
    
    Args:
        url (str): Blob full endpoint URL.
        encoding (str): Encoding type. Defaults to ``UTF-8``.
        logging_enable(bool): If you want to enable logging or not. Defaults to ``True``.

    Returns:
        List of JSON objects.
    """
    if os.path.splitext(url)[1] != '.jsonl':
        raise Exception('Blob must be a jsonlines document (".jsonl").')
    
    blob_client = BlobClient.from_blob_url(blob_url=url,
                                           logging_enable=logging_enable)
    
    return blob_client.download_blob().content_as_text(encoding=encoding).splitlines()


def read_txt_blob(url: str, encoding: str = 'UTF-8', logging_enable: bool = True) -> list:
    """
    Reads blob containing URLs for scraping.

    Args:
        url (str): Blob full URL.
        encoding (str): Encoding format for text downloading.
        logging_enable (bool): To enable logging when downloading blob content.

    Returns:
        List of URLs.

    """
    if os.path.splitext(url)[1] != '.txt':
        raise Exception('Blob must be a txt document (".txt").')
    
    with BlobClient.from_blob_url(blob_url=url, logging_enable=logging_enable) as blob_client:
        return blob_client.download_blob().content_as_text(encoding=encoding).splitlines()
