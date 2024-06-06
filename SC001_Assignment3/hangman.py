"""
File: hangman.py
Name: Jessie
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program tries to figure the un-dashed word out.
    """
    lives = N_TURNS
    word = random_word()
    ans = '-'*len(word)
    print('The word looks like: '+ ans)
    print('You have ' + str(lives) + ' wrong guess left. ')
    while lives > 0:
        guess = input('Your guess: ').upper()
        if guess.isalpha():
            ans = display_word(guess, word, ans)
        else:
            print('Illegal format.')
        if '-' not in ans:
            break
        elif guess not in word:
            lives -= 1
            if lives == 0:
                break
            else:
                print('There is no ',guess, "'s in the word. ")
                print('The word looks like: ' + ans)
                print('You have '+ str(lives) + ' wrong guess left. ')
        elif guess in word:
            print('You are correct! ')
            print('The word looks like: ' + ans)
            print('You have ' + str(lives) + ' wrong guess left. ')

    if lives == 0:
        print('There is no ', guess, "'s in the word. ")
        print('You are completely hung :(\nThe answer is: ', word)
    else:
        print('You are correct! ')
        print('You win!!')
        print('The answer is:', word)


def display_word(guess, word, ans):
    current_ans = ''
    for i in range(len(word)):
        letter = word[i]
        if letter == ans[i]:
            current_ans += letter
        else:
            if letter == guess:
                current_ans += letter
            else:
                current_ans += '-'
    return current_ans




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
