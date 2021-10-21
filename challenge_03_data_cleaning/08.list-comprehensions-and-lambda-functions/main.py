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


# - Use Series.apply() and a lambda function to extract the tag data from tags:
#   - Where the item is a list with length four, return the last item.
#   - In all other cases, return None.
#   - Assign the result to cleaned_tags.
# - Assign the cleaned_tags series to the tags column of the hn_df dataframe.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]
        hn_df = pd.DataFrame.from_dict(hn_clean)

        tags = hn_df['tags']

        cleaned_tags = tags.apply(lambda tag: tag[-1] if len(tag) == 4 else None)
        hn_df['tags'] = cleaned_tags
        

if __name__ == '__main__':
    main()
