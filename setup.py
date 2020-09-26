import setuptools

setuptools.setup(
    name="src",
    version="1.0.0",
    url="https://github.com/Skellet0r/retail-forecast",
    author="Edward Amor",
    license="GPL-3.0",
    author_email="edward.amor3@gmail.com",
    packages=["src"],
    install_requires=[
        "pandas",
        "xlrd",
        "scipy",
        "numpy",
        "matplotlib",
        "seaborn",
        "plotly",
        "scikit-learn",
        "statsmodels",
        "keras",
        "click",
        "requests",
        "xlsx2csv @ git+https://github.com/dilshod/xlsx2csv#egg=xlsx2csv",
    ],
    entry_points={
        "console_scripts": [
            "project=src.data:project",
        ]
    },
)
