import random

def generate_grid():
    """
    Generates list of letters - i.e. grid for the game.
    """
    letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    grid = []
    while len(grid)!=5:
        letter = random.choice(letters)
        if letter not in grid:
            grid.append(letter)
    return grid

def get_words(f, letters):
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, encoding = 'utf-8') as file:
        dict = {"/n":"noun", "noun":"noun", "/v":"verb", "verb":"verb", "/adj":"adjective", "adj":"adjective", "adv":"adverb"}
        word_dict = {"noun":[], "verb":[], "adjective":[], "adjective":[], "adverb":[]}
        for line in file:
            # print(line.split()[0])
            for key in dict:
                if key in line and len(line.split()[0])<=5:
                    word_dict[dict[key]].append(line.split()[0])
                    break
        return word_dict["adverb"][:100]

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    """
    pass
