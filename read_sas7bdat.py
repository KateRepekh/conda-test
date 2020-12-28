from sas7bdat import SAS7BDAT


def read_example(path_to_read, path_to_save, skip_header=False):
    with SAS7BDAT(path_to_read, skip_header=skip_header) as reader:
        df = reader.to_data_frame()
        df.iloc[:100].to_csv(path_to_save)
