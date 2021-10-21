import pandas

from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean
import numpy as np


# - Convert each of the following columns in ap_2010 to numeric values using the pandas.to_numeric() function with the
#   keyword argument errors="coerce".
#   - AP Test Takers
#   - Total Exams Taken
#   - Number of Exams with scores 3 4 or 5
# - Display the column types using the dtypes attribute.
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
        data['ap_2010'][col] = data['ap_2010'][col].apply(lambda score: pandas.to_numeric(score, errors="coerce"))

    print(data['ap_2010'][cols].dtypes)


if __name__ == '__main__':
    main()
