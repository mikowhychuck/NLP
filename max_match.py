#Max match tokenization algorithm.

import csv

def maxmatch_text_split(text, vocabulary):
    i = 0
    tokens = []
    while i < len(text):
        maxWord = ""
        for j in range(i, len(text)):
            tempWord = text[i:j+1]
            if tempWord in vocabulary and len(tempWord) > len(maxWord):
                maxWord = tempWord
        if maxWord == "":
            maxWord = text[i]
        i += len(maxWord)
        tokens.append(maxWord)
    return tokens

def remove_non_letters(text):
    symbols = [' ', ',', '.', ';', '\n']
    for symbol in symbols:
        text = text.replace(symbol, '')
    return text

if __name__ == '__main__':

    with open('list_of_words.csv', 'r') as file:
        data = csv.reader(file)
        words = []
        for row in data:
            words.append(row[0])

    with open('text1.txt', 'r') as file:
        text1 = file.read()

    with open('text2.txt', 'r') as file:
        text2 = file.read()

    text1 = remove_non_letters(text1)
    text2 = remove_non_letters(text2)

    tokens1 = maxmatch_text_split(text1, words)
    print(tokens1)
    tokens2 = maxmatch_text_split(text2, words)
    print(tokens2)