[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Skellet0r/[repo-name]/master)

# [Insert Project Title]

[Insert Project brief overview/background]

## Components

- [Charter](docs/project/charter.md): the project charter was the first step when starting this project,
  and is a sort of outline of this project. It clarifies who our stakeholders are, what we aim to do, and
  how we intend to complete this project. If this is your first time looking at this project, the project
  charter is the best place to start.
- [Conclusion/Exit Report](docs/project/exit-report.md): an outline of this project's end results, it provides
  an overview mainly for a technical audience at the conclusion of the project.
- [Data](data/): this is typically where data used in this project is stored. For large datasets which can't
  be stored within the repository due to their massive size, steps will be given to import the data.
- [Data Dictionaries](docs/data_dictionaries): any custom or client delivered data dictionaries can be found here.
- [Notebooks](notebooks/): this is where all the jupyter notebooks for this project are stored.
  Instead of having one behemoth of a jupyter notebook, there are multiple distinct notebooks each
  focusing on a different phase of the project. A majority of the notebooks focus on modeling and using different
  classifiers. Each notebook is numbered in the order they were completed, this keeps everything in a linear order.
- [Source Code](src/): this is were custom python functions/variables are stored that are used throughout the project.
  It is installed into the conda environment when you first create the environment, and any changes automagically appear.
- [Project Environment](environment.yml): to enable reproducibility of the project environment I recommend you use the
  environment.yml file along with anaconda. However there is also an alternative requirements.txt file in the event
  that one is unable to access/install anaconda. Reproducing the same environment allows for consistent results.

## Quick Start

If you want your own local instance of this project follow the steps below.

1. Clone this repository

```shell
$ git clone [Insert Project Github URL]
```

2. Initialize the environment

```shell
$ cd ./[Insert Project Name]
$ conda env create -f environment.yml
```

3. Activate the environment

```shell
$ conda activate [Insert Project Name]
```

4. Enjoy 😃

> If you'd like to interactively inspect this project, and don't have access to a terminal, anaconda, or pip.
  Click the `launch binder` tag.

## Findings

[Insert Findings]

## Recommendations

[Insert Project Recommendations]

## Next Steps

[Insert Next Steps]

