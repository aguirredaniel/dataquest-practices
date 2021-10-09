import json


# - Import the json module.
# - Use json.loads() to convert world_cup_str to a Python object. Assign the result to world_cup_obj
def main():
    with open('hn_2014.json') as file:
        hn = json.load(file)

        print(len(hn))
        print(hn[0].keys())


if __name__ == '__main__':
    main()
