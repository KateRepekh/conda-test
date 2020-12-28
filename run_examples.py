from pathlib import Path
from os import path

from plot import plot_example
from read_sas7bdat import read_example


if __name__ == "__main__":
    results_dir = "results"
    Path(results_dir).mkdir(exist_ok=True)

    plot_path = path.join(results_dir, "plot_example.png")
    plot_example(plot_path)

    sas7bdat_path = path.join("data", "skinproduct_attributes_seg.sas7bdat")
    csv_path = path.join(results_dir, "sample.csv")
    read_example(sas7bdat_path, csv_path)
