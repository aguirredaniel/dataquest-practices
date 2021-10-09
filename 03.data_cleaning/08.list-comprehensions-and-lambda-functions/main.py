import json


def del_key(dict_, key):
    """
    Return a copy of our dictionary with the key removed
    """
    modified_dict = dict_.copy()
    del modified_dict[key]
    return modified_dict


# - Use a list comprehension to extract the url value from each dictionary in hn_clean. Assign the result to urls
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)
        hn_clean = [del_key(story, 'createdAtI') for story in hn]

        urls = [story['url'] for story in hn_clean]


if __name__ == '__main__':
    main()
