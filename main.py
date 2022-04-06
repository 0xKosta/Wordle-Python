##MADE BY Buxx0-github.com/Buxx0###
###################################
###____####################___#####
##|  _ \                  / _ \ ###
##| |_) |_   ___  ____  _| | | |###
##|  _ <| | | \ \/ /\ \/ / | | |###
##| |_) | |_| |>  <  >  <| |_| |###
##|____/ \__,_/_/\_\/_/\_\\___/####
###################################
###################################

import random
import platform

file = open('words.txt')
content = file.readlines()
word = content[random.randint(0, 5756)]
word = word[0:5]
word = word.upper()

def show(guess):
    print("---------------------")
    for i in range(len(guess)):
        print("|", end = '')
        for k in range(len(guess[0])):
            print(" " + guess[i][k] + " |", end = '')
        print()
        print("---------------------")


def check(guess_deconstruct):
    green = []
    yellow = []
    for i in range(len(guess_deconstruct)):
        for k in range(len(guess_deconstruct)):
            if i == k:
                if guess_deconstruct[k] == word[i]:
                    green.append(k)
            elif guess_deconstruct[k] == word[i]:
                yellow.append(k)
    return green, yellow

def color(guess_deconstruct):
    green, yellow = check(guess_deconstruct)
    if platform.system() == "Linux" or platform.system() == "Darwin":
        for i in green:
            guess_deconstruct[i] = "\u001b[42;1m" + guess_deconstruct[i] + "\u001b[0m"
        for i in yellow:
            guess_deconstruct[i] = "\u001b[43;1m" +guess_deconstruct[i] + "\u001b[0m"
    elif platform.system() == "Windows":
        for i in green:
            guess_deconstruct[i] = "\u001b[32m" + guess_deconstruct[i] + "\u001b[0m"
        for i in yellow:
            guess_deconstruct[i] = "\u001b[33m" +guess_deconstruct[i] + "\u001b[0m"

empty = " "
guess = [
[empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty],
[empty, empty, empty, empty, empty]
]

guessword = ""
guesses = 0
show(guess)
print("What is your guess?")
guessword = input().upper()
while len(guessword) != 5:
    print("Invalid entry, please retry.")
    guessword = input().upper()
guess_deconstruct = []
for i in range(len(word)):
    guess_deconstruct.append(guessword[i])
color(guess_deconstruct)
guess[guesses] = guess_deconstruct
while word != guessword and guesses < 5:
    guesses += 1
    show(guess)
    print("What is your guess?")
    guessword = input().upper()
    while len(guessword) != 5:
        print("Invalid entry, please retry.")
        guessword = input().upper()
    guess_deconstruct = []
    for i in range(len(word)):
        guess_deconstruct.append(guessword[i])
    color(guess_deconstruct)
    guess[guesses] = guess_deconstruct
    if word == guessword:
        break
show(guess)
if word == guessword:
    if guesses + 1 == 1:
        print("First try! Nice job!")
    else:
        print("You managed to guess the word in", guesses + 1, "tries! Good job!")
else:
    print("You didn't manage to guess correctly! The word was:", word , "Better luck next time!")
print("\n\nPress enter to close the game.")
close = input()