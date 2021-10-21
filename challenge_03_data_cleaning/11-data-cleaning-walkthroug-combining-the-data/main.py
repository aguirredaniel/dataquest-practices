from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean
import numpy as np


# - Filter demographics, only selecting rows in data["demographics"] where schoolyear is 20112012.
#   - schoolyear is actually an integer, so be careful about how you perform your comparison.
# - Display the first few rows of data["demographics"] to verify that the filtering worked.
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
    print(demographics)

    if __name__ == '__main__':
        main()
