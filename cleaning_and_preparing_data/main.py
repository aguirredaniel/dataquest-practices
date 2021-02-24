def _open_data_set(file):
    """
    Open file and return a list of list (dataset).
    file it needs to be a csv file
    """
    from csv import reader
    with open(file) as opened_file:
        read_file = reader(opened_file)
        return list(read_file)


# We have created a variable, age1, containing the string "I am thirty-one years old".
#
# Use the str.replace() method to create a new string, age2:
# The new string should have the value "I am thirty-two years old".
def main():
    age1 = "I am thirty-one years old"
    age2 = age1.replace('one', 'two')
    print(age2)


if __name__ == "__main__":
    main()
