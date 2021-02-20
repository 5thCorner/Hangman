import random

lst = ('python', 'java', 'kotlin', 'javascript')
rand_word = random.choice(lst)
word_lst = list('-' * (len(rand_word)))
attempt_lst = list()
count = 8


def output_word():
    print('\n' + ''.join(word_lst))


def input_letter():
    letter = str(input('Input a letter: '))
    return letter


def check_letter(letter):
    global rand_word, word_lst
    for j in range(len(rand_word)):
        if rand_word[j] == letter:
            word_lst[j] = letter
    win_game()
    output_word()


def in_all_lst(letter):
    global count
    if letter in attempt_lst or letter in word_lst:
        print("You've already guessed this letter")
    else:
        attempt_lst.append(letter)
        if letter not in rand_word:
            print("That letter doesn't appear in the word")
            count -= 1


def check_end_game():
    global count
    if count == 0:
        print('You lost!' + '\n')
        quit()


def win_game():
    if rand_word == ''.join(word_lst):
        print('You guessed the word!')
        print('You survived!' + '\n')
        quit()


print('H A N G M A N')
start = str(input('Type "play" to play the game, "exit" to quit: '))
if start == 'exit':
    quit()
elif start == 'play':
    output_word()

    while True:
        win_game()
        new_letter = input_letter()
        if len(new_letter) != 1 or len(new_letter) == 0:
            print('You should input a single letter')
            output_word()
            continue
        elif not new_letter.islower():
            print('Please enter a lowercase English letter.')
            output_word()
            continue
        in_all_lst(new_letter)
        check_end_game()
        check_letter(new_letter)
