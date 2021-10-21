from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean
import numpy as np


# - Filter graduation, only select rows where the Cohort column equals 2006.
# - Filter graduation, only select rows where the Demographic column equals Total Cohort.
# - Display the first few rows of data["graduation"] to verify that everything worked properly.
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


if __name__ == '__main__':
    main()
