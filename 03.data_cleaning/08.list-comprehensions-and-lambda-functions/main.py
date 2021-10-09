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


# - In the display code, we have defined (in comments) a function multiply() using traditional syntax.
# - Create a lambda function that performs the same operation. Assign it to the variable name multiply.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]

        # def multiply(a, b):
        #    return a * b

        multiply = lambda a, b: a * b


if __name__ == '__main__':
    main()
