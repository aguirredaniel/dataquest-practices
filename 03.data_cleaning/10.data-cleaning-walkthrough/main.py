import pandas as pd
import re


# - Write a function that:
#   - Takes in a string.
#   - Uses the regular expression on the previous screen to extract the coordinates.
#   - Uses string manipulation functions to pull out the longitude.
#   - Returns the longitude.
# - Use the Series.apply() method to apply the function across the Location 1 column of hs_directory. Assign the result
#   to the lon column of hs_directory.
# - Use the to_numeric() function to convert the lat and lon columns of hs_directory to numbers.
#   - Specify the errors="coerce" keyword argument to handle missing values properly.
# - Display the first few rows of hs_directory to verify the results.
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

    sat_results = data['sat_results']
    sat_results_columns = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']
    for column in sat_results_columns:
        sat_results[column] = sat_results[column].apply(lambda x: pd.to_numeric(x, errors="coerce"))

    sat_results['sat_score'] = sat_results.loc[:, sat_results_columns].sum(axis=1)

    pattern = r"\((.+),.+\)"
    hs_directory = data['hs_directory']
    hs_directory['lat'] = hs_directory['Location 1'].str.extract(pattern, expand=False, flags=re.I)

    pattern = r"\(.+,(.+)\)"
    hs_directory['lon'] = hs_directory['Location 1'].str.extract(pattern, expand=False, flags=re.I)

    for column in ['lat', 'lon']:
        hs_directory[column] = hs_directory[column].apply(lambda x: pd.to_numeric(x, errors="coerce"))

    print(hs_directory.head())

    sat_results['hs_directory'] = hs_directory


if __name__ == '__main__':
    main()
