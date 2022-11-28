import re
import os
import random

def load_dict(dict_name = "code/Dictionaries/clean_dictionary.txt"):
    '''Returns a list of words contained in newline delimited file'''
    with open(dict_name, "r+", encoding="UTF-8") as in_dict:
        word_list = in_dict.read()
        word_list = word_list.split('\n')[:-1]
    return word_list


def guess_formatter(word, guesses):
    '''Returns a hangman-style string bassed on guesses example: e _ a m p _ e'''
    return_str = "_ " * len(word)
    for guess in guesses:
        hit_ind = [m.start() for m in re.finditer(guess, word)]
        for ind in hit_ind:
            return_str = return_str[: 2 * ind] + guess + return_str[2 * ind + 1:]
    return return_str[:-1]


def main():
    word = random.choice(load_dict())
    tries_left = 6
    guesses = set()
    while tries_left > 0:
        os.system('cls')
        prompt_string = f'{tries_left = }\n{guess_formatter(word, guesses).upper()}\n{guesses = }\n'
        guess = input(prompt_string)
        if guess:
            guess = guess[0]
        else:
            continue
        if guess not in guesses:
            guesses.add(guess)
            if guess not in word:
                tries_left -= 1
        if guesses.issuperset(word):
            break
    
    print(f'{word = }')
        
        
if __name__ == "__main__":
    main()