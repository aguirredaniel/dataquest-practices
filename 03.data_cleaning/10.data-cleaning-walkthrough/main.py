import pandas as pd


# - Loop through each key in data. For each key:
#   - Display the first five rows of the dataframe associated with the key.
def main():
    data_files = [
        "ap_2010.csv",
        "class_size.csv",
        "demographics.csv",
        "graduation.csv",
        "hs_directory.csv",
        "sat_results.csv"
    ]
    data = {}

    for file in data_files:
        file_name = file.split('.')[0]
        data[file_name] = pd.read_csv(f'schools/{file}')

        print(data[file_name].head())


if __name__ == '__main__':
    main()
