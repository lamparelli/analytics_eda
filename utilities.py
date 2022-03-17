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

"""
Returns a list of strings containing the names of the columns with dict-type data
"""
def getListOfObjectColumns(dataframe):
    return list(filter(lambda col: isNestedObjectSeries(dataframe[col]), dataframe.columns))

"""
Returns True if the first non-empty value of a series is a type dict, False otherwise
"""
def isNestedObjectSeries(series):
    sampleItemIndex = series.first_valid_index()
    if (sampleItemIndex is None):
        # In case of series with all empty values
        return False
    return type(series[sampleItemIndex]) == dict

"""
Creates a new column for every property in the nested objects, and deletes the original object column
"""
def extractNestedObjectData(dataframe, column):
    # Extracts to list of keys in the first non-empty object of the column (works if every object has the same keys)
    colData = dataframe[column]
    sampleDataIndex = colData.first_valid_index()
    if (sampleDataIndex is None):
        return
    sampleData = colData[sampleDataIndex]
    keys = list(sampleData.keys())

    # Creates a new column for each property in the objects
    columnIndex = list(dataframe.columns).index(column)
    for (index, key) in enumerate(keys):
        newColIdx = columnIndex+index+1
        newColName = column + "_" + key
        newColData = dataframe[column].map(lambda val: val[key])
        dataframe.insert(loc=newColIdx, column=newColName, value=newColData)

    # Eliminates the original column
    dataframe.drop(columns=[column], inplace=True)