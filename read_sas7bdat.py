from sas7bdat import SAS7BDAT
from csv import writer


def read_example(
    path_to_read, path_to_save, skip_header=False, sample_size=100
):
    with SAS7BDAT(path_to_read, skip_header=skip_header) as reader:
        with open(path_to_save, "w") as sample_file:
            csv_writer = writer(sample_file)
            for row, row_num in zip(reader, range(sample_size)):
                csv_writer.writerow(row)
