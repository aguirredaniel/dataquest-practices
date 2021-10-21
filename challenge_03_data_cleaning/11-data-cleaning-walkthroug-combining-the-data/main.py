import pandas as pd
from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean


# - Write a function that extracts the first two characters of a string and returns them.
# - Apply the function to the DBN column of combined and assign the result to the school_dist column of combined.
# - Display the first few items in the school_dist column of combined to verify the results.
def main():
    data = read_data()
    data = make_initial_clean(data)

    data = data.copy()

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

    print(combined['school_dist'].head())


if __name__ == '__main__':
    main()
