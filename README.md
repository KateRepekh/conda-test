# conda-test

This project tests packages from https://anaconda.org/krepekh/repo


Feedstocks:
- matplotlib - https://github.com/KateRepekh/matplotlib-feedstock
- sas7bdat - https://github.com/KateRepekh/staged-recipes/tree/sas7bdat


Run the following commands:
```shell
conda env create --file environment.yaml
conda activate conda-test
python run_examples.py
```
