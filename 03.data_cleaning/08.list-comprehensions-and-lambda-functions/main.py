import json


def del_key(dict_, key):
    """
    Return a copy of our dictionary with the key removed
    """
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict


def get_num_comments(hn_2014) -> int:
    """
    Return Num Comments of  Story in hn_2014.json.
    Args:
        hn_2014:
            hn_2014.json file in python json format (a.k.a dict).

    Returns:
        Num Comments for Story
    """
    return hn_2014['numComments']


# - Create a "key function" that accepts a single dictionary and returns the value from the numComments key.
# - Use the max() function with the "key function" you just created to find the value from the hn_clean list with the
#   most comments:
#   - Assign the result to the variable most_comments.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]

        most_comments = max(hn_clean, key=get_num_comments)
        print(most_comments['title'], most_comments['numComments'], sep=' : ')


if __name__ == '__main__':
    main()
