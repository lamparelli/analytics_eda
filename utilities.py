from google.cloud import bigquery
import os
import errno

bigQueryTokenFileName = "bq_key.json"

"""
Returns a dataframe containing the BigQuery table data
"""
def retrieveBigQueryData(bigQueryTableId, rowNumberLimit = None):
    # Checks if the token file exists
    if (not os.path.exists(bigQueryTokenFileName)):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), bigQueryTokenFileName)    

    # Sets the BigQuery access token as an os environment variable
    credentials_path = os.path.abspath(bigQueryTokenFileName)
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
    
    # Sets the table id in the proper format for the BigQuery API
    bigQueryTableId = bigQueryTableId.replace(":", ".")

    # Defines the query
    query = "SELECT * FROM `" + bigQueryTableId + "`"
    if (rowNumberLimit is not None):
        query += " LIMIT " + str(rowNumberLimit)

    # Downloads the data
    client = bigquery.Client()

    result = (
        client.query(query)
        .result()
        .to_dataframe(
            create_bqstorage_client=True,
        )
    )

    return result