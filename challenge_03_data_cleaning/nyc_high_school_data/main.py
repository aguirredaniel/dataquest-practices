import pandas as pd
import re
import os


def read_data() -> dict:
    """
        Helper function to read datasets use in course 'Data Cleaning Project Walkthrough'
        The datasets work with at:
         - ap_2010.csv
         - class_size.csv
         - demographics.csv
         - graduation.csv
         - hs_directory.csv
         - sat_results.csv
    Returns:
        Dict with name files as keys and pd.DataFrame as values.
    """
    data_files = [
        "ap_2010.csv",
        "class_size.csv",
        "demographics.csv",
        "graduation.csv",
        "hs_directory.csv",
        "sat_results.csv"
    ]
    data = {}

    cur_path = os.path.dirname(__file__)
    data_path = cur_path + '/schools/'
    for file in data_files:
        file_name = file.split('.')[0]
        data[file_name] = pd.read_csv(data_path + file)

    all_survey = pd.read_csv(data_path + 'survey_all.txt', delimiter='\t', encoding='windows-1252')
    d75_survey = pd.read_csv(data_path + 'survey_d75.txt', delimiter='\t', encoding='windows-1252')

    survey = pd.concat([all_survey, d75_survey])

    data['survey'] = survey
    return data


def make_initial_clean(nyc_data: dict) -> dict:
    data = nyc_data.copy()
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

    hs_directory.rename(columns={'dbn': 'DBN'}, inplace=True)
    return data


def merge_data(nyc_data: dict) -> pd.DataFrame:
    data = nyc_data.copy()

    class_size = data['class_size']
    class_size = class_size[(class_size['GRADE '] == '09-12') & (class_size['PROGRAM TYPE'] == 'GEN ED')]

    class_size_dbn = class_size.groupby('DBN').mean()
    class_size = class_size_dbn.reset_index()

    data['class_size'] = class_size

    demographics = data["demographics"]
    demographics = demographics[demographics['schoolyear'] == 20112012]
    data["demographics"] = demographics

    graduation = data['graduation']
    graduation = graduation[(graduation['Cohort'] == '2006') & (graduation['Demographic'] == 'Total Cohort')]
    data['graduation'] = graduation

    cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

    for col in cols:
        data['ap_2010'][col] = pd.to_numeric(data['ap_2010'][col], errors="coerce")

    combined = data["sat_results"]

    combined = pd.merge(combined, data['ap_2010'], on="DBN", how='left')
    combined = pd.merge(combined, data['graduation'], on="DBN", how='left')

    for df in ['class_size', 'demographics', 'survey', 'hs_directory']:
        combined = pd.merge(combined, data[df], on='DBN', how='inner')

    combined = combined.fillna(combined.mean())
    combined = combined.fillna(0)

    combined['school_dist'] = combined['DBN'].str[:2]

    return combined
