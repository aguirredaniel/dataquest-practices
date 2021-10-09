import json


# - Use the open() function to open the hn_2014.json file as a file object.
# - Use the json.load() function to parse the file object and assign the result to hn.
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)

        print(len(hn))
        print(hn[0].keys())


if __name__ == '__main__':
    main()
