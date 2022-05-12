import random
from hangman_words import word_list
from hagman_art import stages, logo



chosen_word = random.choice(word_list)

position = "_"
list_position = []
for j in range(len(chosen_word)):
    list_position.append(position)

#print(chosen_word)

health = 6

print(logo)

#print(chosen_word)

while health > 0 and position in list_position:
    user_letter = input("Guess the letter:").lower()

    if user_letter in list_position:
        print("You have already guessed", user_letter)
    minus_point = 0

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == user_letter:
            list_position[i] = letter
        else:
            minus_point += 1

    if minus_point == len(chosen_word):
        health -= 1

    display = " ".join(list_position)
    print(display)
    kolik_zbyva = len(stages)
    print(stages[-(kolik_zbyva-health)])

if position not in list_position:
    print("YOU WON")
else:
    print("you died. L00SeR")
    print(chosen_word)
