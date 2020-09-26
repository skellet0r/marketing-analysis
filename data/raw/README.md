# List of Raw Datasets

The original, immutable data dump.

|        Raw Dataset Name |                                                                  Link to the Full Raw Dataset | Full Dataset Size (MB) |
| ----------------------: | --------------------------------------------------------------------------------------------: | ---------------------: |
| online_retail_II.xlsx 1 | [link](https://archive.ics.uci.edu/ml/machine-learning-databases/00502/online_retail_II.xlsx) |                     45 |


This dataset can be downloaded using the utility `download` function found in the `src.data` module. Provide the download URL and output directory to have the file downloaded.

```python
from src.data import download

download("https://archive.ics.uci.edu/ml/machine-learning-databases/00502/online_retail_II.xlsx", "data/raw")
```