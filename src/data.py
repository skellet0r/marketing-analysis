from os import path

import requests


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
