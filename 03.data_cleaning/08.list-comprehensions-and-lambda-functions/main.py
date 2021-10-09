import json


def del_key(dict_, key):
    """
    Return a copy of our dictionary with the key removed
    """
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict


# - Create a list comprehension representation of the loop from the previous screen:
#   - Call the del_key() function to remove the createdAtI value from each dictionary in the hn list.
#   - Assign the results to a new list, hn_clean.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]


if __name__ == '__main__':
    main()
