'''Imports and sorts dictionaries according to length and amount of unique characters'''

import string

def clean_wordlist(wordlist, messy_chars=None):
    '''Returns word_list with messy_chars stripped out in lowercase'''
    messy_chars = messy_chars if messy_chars else ['\n', ' ']
    return_words = []
    for word in wordlist:
        word = word.lower()
        for char in messy_chars:
            word = word.replace(char, "")
        return_words.append(word)
    return return_words


def filter_words(word_list, required_chars, permissible_chars):
    '''returns word_list without entries that don't have at least 1 REQUIRED_CHARS
    or contains characters not in PERMISSIBLE_CHARS'''
    return_words = []
    for word in word_list:
        if contains_atleast_i_required_chars(word, required_chars):
            if contains_only_permissible_chars(word, permissible_chars):
                return_words.append(word)
    return return_words


def contains_atleast_i_required_chars(word, required_chars, i=1):
    '''Returns True if word contains at least n different required_chars'''
    n_required_chars = 0
    for char in required_chars:
        if char in word:
            n_required_chars += 1
            if n_required_chars >= i:
                return True
    return False


def contains_only_permissible_chars(word, permissible_chars):
    '''True if word only contains of permissible_chars, False otherwise'''
    for letter in word:
        if letter not in permissible_chars:
            return False
    return True


def get_unique_chars(word):
    '''Returns a string with all the unique characters in a word'''
    unique_letters = ""
    for letter in word:
        if letter not in unique_letters:
            unique_letters += letter
    return unique_letters

def main():
    '''TODO: DOCSTRING'''
    dict_in_name = "raw_dictionary.txt"
    dict_out_name = "clean_dictionary.txt"

    # Require at least one vowel in a word for it to count and only allow ascii chars
    required_chars = 'aeiouy'
    permissible_chars = string.ascii_lowercase

    # Open the dictionary
    with open(dict_in_name, "r", encoding="UTF-8") as in_dict:
        raw = in_dict.readlines()

    word_list = clean_wordlist(raw)
    filtered_list = filter_words(word_list, required_chars, permissible_chars)

    with open(dict_out_name, "w+", encoding="UTF-8") as out_dict:
        for word in filtered_list:
            out_dict.write(word + "\n")


if __name__ == "__main__":
    main()
