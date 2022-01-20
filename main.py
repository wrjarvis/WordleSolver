def read_word_file(filename, word_length):
    word_list = []
    with open(filename, 'r') as f:
        for line in f:
            if len(line.strip().lower()) == word_length:
                word_list.append(line.strip().lower())
    return word_list


def compare_words(word1, word2):
    word1 = list(word1)
    word2 = list(word2)
    results = ['_', '_', '_', '_', '_']
    for i, char1 in enumerate(word1):
        if char1 == word2[i]:
            results[i] = 'x'
            word2[i] = '_'
    for i, char1 in enumerate(word1):
        for j, char2 in enumerate(word2):
            if char1 == char2:
                results[i] = '0'
                word2[j] = '_'
    return ''.join(results)


def find_new_word(word_list):
    new_word = word_list[0]
    new_score = 0
    for word1 in word_list:
        word_score = 0
        for word2 in word_list:
            word_score += find_score(compare_words(word1, word2))
        if word_score > new_score:
            new_score = word_score
            new_word = word1
    return new_word


def find_score(result):
    score = 0
    for i in result:
        if i == 'x':
            score = score + 2
        elif i == 'o':
            score = score + 1
    return score


def reduce_word_list(word_list, guess_word, results):
    new_word_list = []
    for word in word_list:
        if results == compare_words(guess_word, word):
            new_word_list.append(word)
    return new_word_list


def get_input():
    results = str(input('Please enter result: '))
    return results


if __name__ == '__main__':

    print('Welcome to the Wordle Guessing Helper!!')

    WordFileName = 'ukenglish.txt'
    WordList = read_word_file(WordFileName, 5)

    NGuesses = 1

    while True:

        NewWord = find_new_word(WordList)
        print(f'Next Guess: {NewWord}')
        Result = get_input()

        if Result == 'xxxxx':
            print(f'SOLVED! It took {NGuesses} guesses')
            break
        NGuesses = NGuesses + 1

        WordList = reduce_word_list(WordList, NewWord, Result)

        if not WordList:
            print('No solution found')
            break
