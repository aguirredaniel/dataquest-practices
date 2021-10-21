import pandas as pd
from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean


# - Use the pandas pandas.DataFrame.merge() method to merge the ap_2010 dataset into combined.
#   - Make sure to specify how="left" as a keyword argument to indicate the correct join type.
#   - Make sure to assign the result of the merge operation back to combined.
# - Use the pandas df.merge() method to merge the graduation dataset into combined.
#   - Make sure to specify how="left" as a keyword argument to get the correct join type.
#   -Make sure to assign the result of the merge operation back to combined.
# - Display the first few rows of combined to verify that the correct operations occurred.
# - Use the pandas.DataFrame.shape attribute to display the shape of the dataframe and see how many rows now exist.
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

    combined = pd.merge(combined, data['ap_2010'], how='left')
    combined = pd.merge(combined, data['graduation'], how='left')

    print(combined, combined.shape, sep='\n')
    print(combined.shape)


if __name__ == '__main__':
    main()
