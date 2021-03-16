class MyList:
    """ Represent a typical List

      Example:
        list = MyList([1,2,3])
    """

    def __init__(self, initial_data):
        self.data = initial_data

    def append(self, new_item):
        """ Add an element to the end of the list

        Args:
            new_item: item to append in the list

        Example:
            list.append(17)

            The values in the list are:
            [..., 17]
        """
        list_item = [new_item]
        self.data += list_item


# 1. Inside the MyList class, define a new append() method with two arguments:
#  - self: The self-references to the instance.
#  - new_item: The new item that we want to add to the list.
# 2. Implement the append() method so that it appends the provided new_item to the list stored in self.data.
# 3. Outside of the class, create an instance of MyList providing the list [1, 2, 3, 4, 5].
#    Assign it to a variable named my_list.
# 4. Print the value of my_list.data.
# 5. Use the append() method to append value 6 to my_list.
# 6. Print the value of my_list.data. Observe that it now contains the 6 that we added.
def main():
    my_list = MyList([1, 2, 3, 4, 5])
    print(my_list.data)

    my_list.append(6)
    print(my_list.data)


if __name__ == "__main__":
    main()
