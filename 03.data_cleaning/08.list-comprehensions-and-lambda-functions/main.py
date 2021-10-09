import json


# - Import the json module.
# - Use json.loads() to convert world_cup_str to a Python object. Assign the result to world_cup_obj
def main():
    world_cup_str = """
    [
        {
            "team_1": "France",
            "team_2": "Croatia",
            "game_type": "Final",
            "score" : [4, 2]
        },
        {
            "team_1": "Belgium",
            "team_2": "England",
            "game_type": "3rd/4th Playoff",
            "score" : [2, 0]
        }
    ]
    """

    world_cup_obj = json.loads(world_cup_str)

    print(world_cup_obj)


if __name__ == '__main__':
    main()
