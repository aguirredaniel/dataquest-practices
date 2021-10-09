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


# - Using sorted() and a lambda function, sort the hn_clean JSON list by the number of points (dictionary key points)
#   from highest to lowest:
#   - Check the documentation for sorted() to see how to reverse the order to highest to lowest.
#   - Assign the result to hn_sorted_points.
# - Use a list comprehension to return a list of the five post titles (dictionary key title) that have the most points
#   in our data set:
#   - Assign the result to top_5_titles.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]

        hn_sorted_points = sorted(hn_clean, key=lambda story: story['points'], reverse=True)
        top_5_titles = [story['title'] for story in hn_sorted_points[:5]]

        print(top_5_titles)


if __name__ == '__main__':
    main()
