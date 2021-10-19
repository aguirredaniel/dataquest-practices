import pandas as pd


# - Read in survey_all.txt.
#   - Use the pandas.read_csv() function to read survey_all.txt into the variable all_survey. Recall that this file is
#     located in the schools folder.
#     - Specify the keyword argument delimiter="\t".
#     - Specify the keyword argument encoding="windows-1252".
# - Read in survey_d75.txt.
#   - Use the pandas.read_csv() function to read schools/survey_d75.txt into the variable d75_survey. Recall that this
#     file is located in the schools folder.
#     - Specify the keyword argument delimiter="\t".
#     - Specify the keyword argument encoding="windows-1252".
# - Combine d75_survey and all_survey into a single dataframe.
#   - Use the pandas concat() function with the keyword argument axis=0 to combine d75_survey and all_survey into the
#     dataframe survey.
#   - Pass in all_survey first, then d75_survey when calling the pandas.concat() function.
# - Display the first five rows of survey using the pandas.DataFrame.head() function.
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

    all_survey = pd.read_csv('schools/survey_all.txt', delimiter='\t', encoding='windows-1252')
    d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')

    survey = pd.concat([all_survey, d75_survey])

    print(survey.head())


if __name__ == '__main__':
    main()
