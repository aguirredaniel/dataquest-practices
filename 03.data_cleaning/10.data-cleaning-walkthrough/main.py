import pandas as pd
import re


# - Convert the SAT Math Avg. Score, SAT Critical Reading Avg. Score, and SAT Writing Avg. Score columns in the
#   sat_results data set from the object (string) data type to a numeric data type.
#   - Use the pandas.to_numeric() function on each of the columns, and assign the result back to the same column.
#  - Pass in the keyword argument errors="coerce".
# - Create a column called sat_score in sat_results that holds the combined SAT score for each student.
#   - Add up SAT Math Avg. Score, SAT Critical Reading Avg. Score, and SAT Writing Avg. Score, and assign the total to
#     the sat_score column of sat_results.
# - Display the first few rows of the sat_score column of sat_results to verify that everything went okay.
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
    print(hs_directory['lat'])


if __name__ == '__main__':
    main()
