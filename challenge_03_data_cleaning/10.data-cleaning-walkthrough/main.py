import re
import pandas as pd
from challenge_03_data_cleaning.nyc_high_school_data import read_data


def main():
    data = read_data()

    survey = data['survey']

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


if __name__ == '__main__':
    main()
