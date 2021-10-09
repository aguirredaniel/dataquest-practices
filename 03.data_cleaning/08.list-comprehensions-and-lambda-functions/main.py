import json
import pandas as pd


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


# - Use Series.apply() and len() to create a boolean mask based on whether each item in tags has a length of 4.
# - Use the boolean mask to filter tags. Assign the result to four_tags.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]
        hn_df = pd.DataFrame.from_dict(hn_clean)

        tags = hn_df['tags']
        four_tags = tags[tags.apply(len) == 4]

        print(four_tags)


if __name__ == '__main__':
    main()
