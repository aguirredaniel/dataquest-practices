import pandas as pd


# - Copy the dbn column in hs_directory into a new column called DBN.
# - Create a new column called padded_csd in the class_size dataset.
#   - Use the pandas.Series.apply() method along with a custom function to generate this column.
#     - Make sure to apply the function along the data["class_size"]["CSD"] column.
# - Use the addition operator (+) along with the padded_csd and SCHOOL CODE columns of class_size, then assign the
#   result to the DBN column of class_size.
# - Display the first few rows of class_size to double check the DBN column.
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

    class_size = data["class_size"]
    class_size['padded_csd'] = class_size['CSD'].apply(
        lambda csd: str(csd) if len(str(csd)) == 2 else f'0{csd}')

    class_size['DBN'] = class_size['padded_csd'] + class_size['SCHOOL CODE']

    print(data["class_size"]['DBN'])


if __name__ == '__main__':
    main()
