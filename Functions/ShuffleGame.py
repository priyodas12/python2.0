from random import shuffle

test_list = [0, 1, 0, 0]


def shuffle_list(any_list):
    shuffle(any_list)
    print(any_list)
    return any_list


def start_game(anyList):
    guess_point_string = input(
        "Guess the position, enter any number between 0 to 3::  ")
    game_list = shuffle_list(anyList)
    print(game_list)
    guess_point = int(guess_point_string)
    for num in game_list:
        if game_list.index(1) == guess_point:
            print("Won the game!")
            break
        else:
            print("Lost the game!")
            break


start_game(test_list)
