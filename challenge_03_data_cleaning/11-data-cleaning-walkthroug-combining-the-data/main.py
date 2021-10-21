from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean


# - Create a new variable called class_size and assign the value of data["class_size"] to it.
# - Filter class_size so the GRADE  column only contains the value 09-12. Note that the name of the GRADE  column has a
#   space at the end; you'll generate an error if you don't include it.
# - Filter class_size so that the PROGRAM TYPE column only contains the value GEN ED.
# - Display the first five rows of class_size to verify.
def main():
    data = read_data()
    data = make_initial_clean(data)

    class_size = data['class_size']
    class_size = class_size[(class_size['GRADE '] == '09-12') & (class_size['PROGRAM TYPE'] == 'GEN ED')]

    print(class_size.head())


if __name__ == '__main__':
    main()
