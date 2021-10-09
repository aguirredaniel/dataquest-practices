import json


def del_key(dict_, key):
    """
    Return a copy of our dictionary with the key removed
    """
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict


# - Use list comprehension to create a new list, thousand_points:
#   - The list should contain values from hn_clean where the points key has a value greater than 1000.
# - Count the number of values in thousand_points and assign the result to num_thousand_points.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]

        urls = [story['url'] for story in hn_clean]

        thousand_points = [story for story in hn_clean if story['points'] > 1000]
        num_thousand_points = len(thousand_points)
        print(num_thousand_points)


if __name__ == '__main__':
    main()
