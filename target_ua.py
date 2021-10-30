"""
This module can be used to play raget game in ukrainian
"""
import random

def generate_grid():
    """
    Generates list of letters - i.e. grid for the game.
    e.g. ['з', 'у', 'п', 'ж', 'ф']
    """
    grid = []
    ua_letters = [1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083,
    1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097,
    1100, 1102, 1103, 1108, 1110, 1111, 1169]
    while len(grid)!=5:
        letter = random.randint(1072, 1169)
        if letter in ua_letters and chr(letter) not in grid:
            grid.append(chr(letter))
    return grid

def get_words(file_name, letters):
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(file_name, encoding = 'utf-8') as file:
        correct_dict = {"/n":"noun", "noun":"noun", "/v":"verb", "verb":"verb",
        "/adj":"adjective", "adj":"adjective", "adv":"adverb"}
        word_list = []
        for line in file:
            for key, value in correct_dict.items():
                word = line.split()[0]
                if key in line and len(word)<=5:
                    if word[0] in letters and word not in word_list:
                        word_list.append((word, value))
                    break
        return word_list

def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    Check if user words are correct and belong to correct class.
    """
    for word in user_words:
        if word[0] not in letters:
            del user_words[user_words.index(word)]
    correct_words = []
    for word in user_words:
        if (word, language_part) in dict_of_words:
            correct_words.append(word)
    missed_words= []
    for word in dict_of_words:
        if word[0] not in user_words and word[1]==language_part:
            missed_words.append(word[0])
    return correct_words, missed_words


def main():
    """
    Main function
    """
    grid = generate_grid()
    print(grid)
    language_part = random.choice(['noun', 'verb', 'adjective', 'adverb'])
    print("Your category:", language_part)
    user_words = list(input('Enter words: ').split())
    dict_words = get_words("E:/UCU/OP/ЛР 6/Target_ua/base.lst", grid)
    correct_words, missed_words = check_user_words(user_words, language_part, grid, dict_words)
    print("Your correct words:", correct_words)
    print("Your missed words:", missed_words)

if __name__=="__main__":
    main()
