import io
import pandas as pd
import requests
import os

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    urls = [
        "https://raw.githubusercontent.com/chintandevputers/pipeline/main/upload_csv/customer_data.csv",
        "https://raw.githubusercontent.com/chintandevputers/pipeline/main/upload_csv/destination_data.csv",
        "https://raw.githubusercontent.com/chintandevputers/pipeline/main/upload_csv/booking_data.csv"
    ]
    dfs = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            filename = url.split('/')[-1]  # Extracting filename from URL
            directory = "download_csv"
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory, filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename} successfully!")
            
            df = pd.read_csv(io.StringIO(response.text), sep=',')
            dfs.append(df)
        else:
            print(f"Failed to download data from {url}. Status code: {response.status_code}")
    return dfs
    # return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
