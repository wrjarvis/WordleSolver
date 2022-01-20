from main import *
import random
import statistics


def test(word_list):
    guess_word = random.choice(word_list)
    print(f"Guessing: {guess_word}")
    n_guesses = 1
    while True:
        new_word = find_new_word(word_list)
        print(f'Next Guess: {new_word}')
        result = compare_words(new_word, guess_word)
        print(result)
        if result == 'xxxxx':
            print(f'SOLVED! It took {n_guesses} guesses')
            break
        n_guesses = n_guesses + 1
        word_list = reduce_word_list(word_list, new_word, result)
    return n_guesses


WordFileName = 'ukenglish.txt'
WordList = read_word_file(WordFileName, 5)

NGuesses = []
for i in range(100):
    NGuesses.append(test(WordList))
print(f'Mean Guesses: {statistics.mean(NGuesses)}')

