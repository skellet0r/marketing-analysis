from os import path

import requests
import click
from xlsx2csv import Xlsx2csv
import pandas as pd

import gzip


@click.group()
def project():
    """Project related commands"""
    pass


def download(url: str, output_dir: str):
    """Download file from url and save to a directory.

    This is a convenience function for downloading large files instead of
    hosting them inside of a git repository. This will reduce the network
    bandwith required on the initial git clone of the repository.

    Args:
        url (str): A valid URL pointing to a file.
        output_dir (str): The directory the file will be saved to.
    """
    resp = requests.get(url, stream=True)
    fp = path.join(output_dir, path.basename(url))
    with open(fp, "wb") as f:
        for chunk in resp.iter_content(chunk_size=2 ** 16):
            f.write(chunk)


@project.command()
def init():
    """Download, extract, and init the project's raw data.

    This function must be called from the root of the project.
    It will download the data, split it into csv files, and then compile
    it into one flat data file.
    """
    click.echo("Starting project initialization ...")
    dataset_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00502/online_retail_II.xlsx"

    # path to the downloaded dataset
    fp = "data/raw/online_retail_II.xlsx"

    # if the data hasn't been downloaded, download it
    if not path.exists(fp):
        click.echo(f"Downloading {path.basename(fp)} to {fp}")
        download(dataset_url, "data/raw")
        click.echo(f"Finished downloading to {fp}")
        xlsx = Xlsx2csv(fp)  # excel to csv object
    if not path.exists("data/raw/txs_2009.csv"):  # create the 2009 txs data csv
        click.echo("Converting 2009 transaction data to csv")
        xlsx.convert("data/raw/txs_2009.csv", sheetid=1)
        click.echo("Finsihed converting 2009 transaction data to csv")
    if not path.exists("data/raw/txs_2010.csv"):  # create the 2010 txs data csv
        click.echo("Converting 2010 transaction data to csv")
        xlsx.convert("data/raw/txs_2010.csv", sheetid=2)
        click.echo("Finsihed converting 2010 transaction data to csv")

    # compile the two separate data sources into one csv file
    click.echo("Starting data compilation")
    tx_2009_df = pd.read_csv("data/raw/txs_2009.csv")
    tx_2010_df = pd.read_csv("data/raw/txs_2010.csv")
    compiled_df = tx_2009_df.append(tx_2010_df)
    click.echo("Finished compiling data")

    # save the compiled data
    compiled_df.to_csv("data/raw/data.csv", index=False)
    click.echo("Saved compiled data to data/raw/data.csv")

    # decompress geojson data
    if not path.exists("data/external/countries.geojson"):
        click.echo("Decompressing countries.geojson")
        with gzip.open("data/external/countries.geojson.gz") as f:
            with open("data/external/countries.geojson", "wb") as g:
                g.write(f.read())
