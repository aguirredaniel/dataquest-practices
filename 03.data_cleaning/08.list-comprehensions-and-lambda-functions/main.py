import json


def del_key(dict_, key):
    """
    Return a copy of our dictionary with the key removed
    """
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict


# - Create an empty list, hn_clean to store the cleaned data set.
# - Loop over the dictionaries in the hn list. In each iteration:
#   - Use the del_key() function to delete the createdAtI key from the dictionary.
#   - Append the cleaned dictionary to hn_clean.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]


if __name__ == '__main__':
    main()
