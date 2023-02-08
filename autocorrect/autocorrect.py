import sys
import math
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    number_of_dictionary_words, number_of_misspelled_words = (int(val) for val in line.split(SEPARATOR))
    correct_words = []
    words_to_check = []
    for i in range(number_of_dictionary_words):
        correct_words.append(sys.stdin.readline().rstrip())
    for i in range(number_of_misspelled_words):
        words_to_check.append(sys.stdin.readline().rstrip())

    for words in words_to_check:
        which_correct_word = []
        which_correct_word_dictionary = {}
        for correct in correct_words:
            if len(words) == len(correct):
                number_of_wrong_letters = 0
                for i in range(len(words)):
                    if words[i] != correct[i]:
                        number_of_wrong_letters += 1
                which_correct_word.append(number_of_wrong_letters)
                which_correct_word_dictionary.update({number_of_wrong_letters:correct})
        which_correct_word.sort()
        print(which_correct_word_dictionary.get(which_correct_word[0]))

                
        
