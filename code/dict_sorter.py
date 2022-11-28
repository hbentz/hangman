import collections
import pickle

def get_unique_chars(word):
    '''Returns a string with all the unique characters in a word'''
    unique_letters = ""
    for letter in word:
        if letter not in unique_letters:
            unique_letters += letter
    return unique_letters


def main():
    '''Saves dictionary to files according to the word length and the number of unique letters'''
    dict_in_name = "code/Dictionaries/clean_dictionary.txt"
    with open(dict_in_name, "r+", encoding="UTF-8") as in_dict:
        word_list = in_dict.read()
        word_list = word_list.split('\n')[:-1]

    word_lookup = collections.defaultdict(dict)
    for word in word_list:
        word_lookup[len(word)].append(word)
    pickle.dump(word_lookup, "")
