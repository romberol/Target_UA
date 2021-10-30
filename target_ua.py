"""
This module can be used to play raget game in ukrainian
"""
import random

def generate_grid():
    """
    Generates list of letters - i.e. grid for the game.
    e.g. ['з', 'у', 'п', 'ж', 'ф']
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
            for key in dict:
                word = line.split()[0]
                if key in line and len(word)<=5:
                    if word[0] in letters:
                        word_dict[dict[key]].append(word)
                    break
        return word_dict["adverb"]

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Check if user words are correct and belong to correct class.
    """
    pass
# let = generate_grid()
# print(let)
# print(get_words("E:/UCU/OP/ЛР 6/Target_ua/base.lst", let))