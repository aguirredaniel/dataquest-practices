class MyList:
    """ Represent a typical List

      Example:
        list = MyList([1,2,3])
    """

    def __init__(self, initial_data):
        self.data = initial_data

        # Calculate the initial length
        self.length = 0
        for item in self.data:
            self.length += 1

    def append(self, new_item):
        """ Add an element to the end of the list

        Args:
            new_item: item to append in the list

        Example:
            list.append(17)

            The values in the list are:
            [..., 17]
        """
        self.data += [new_item]
        # Update the length
        self.length += 1


# 1. The MyList class from the previous screen is provided. We've added code in the __init__()
#    method that initializes the list length.
# 2. Inside the append() method, add one line of code that updates the length attribute of the list.
# 3. Outside of the class, create an instance of MyList providing the list [1, 1, 2, 3, 5].
#    Assign it to a variable named my_list.
# 4. Print the length attribute of my_list.
# 5. Use the append() method to append value 8 to my_list.
# 6. Print the length attribute of my_list. Observe that it was updated when a new value was added.
def main():
    my_list = MyList([1, 1, 2, 3, 5])
    print(my_list.length)

    my_list.append(8)
    print(my_list.length)


if __name__ == "__main__":
    main()
