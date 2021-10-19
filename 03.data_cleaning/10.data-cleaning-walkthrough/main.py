import pandas as pd


# - Copy the data from the dbn column of survey into a new column in survey called DBN.
# - Filter survey so it only contains the columns we listed above. You can do this using pandas.DataFrame.loc[].
#   - Remember that we renamed dbn to DBN; be sure to change the list of columns we want to keep accordingly.
# - Assign the dataframe survey to the key survey in the dictionary data.
# - When you're finished, the value in data["survey"] should be a dataframe with 23 columns and 1702 rows.
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

    survey_columns = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11",
                      "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11",
                      "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
    survey['DBN'] = survey['dbn']

    survey = survey.loc[:, survey_columns]
    data['survey'] = survey

    assert survey.shape, (23, 1702)


if __name__ == '__main__':
    main()
