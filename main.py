from os import read
import csv, random

def main():
    word = get_word()
    num_of_guesses = 8
    max_guesses = 20
    list_word = split_word(word)
    word_length = len(list_word)
    guess_word = []
    for i in range(word_length):
        guess_word.append("_")
    for i in range(max_guesses):
        print(" ".join(guess_word))
        guess = guess_letter()
        if len(guess) > 1:
            print("You must enter a single letter.")
            break
        else:
            if guess in list_word:
                for i in range(word_length):
                    if list_word[i] == guess:
                        guess_word[i] = guess
            else:
                num_of_guesses -= 1
                if num_of_guesses > 0:
                    print(f"Incorrect! You have {num_of_guesses} guesses left.")
                else:
                    print(f"You lose! The correct word was {word}.")
                    break
        if guess_word == list_word:
            print("You win!")
            break
    
def guess_letter():
    guess = input("Enter a letter: ")
    return guess    
    
def get_word():
    word = read_file()
    if word == "":
        print("You must enter a word.")
        word = get_word()
    word = word.lower()
    return word

def split_word(word):
    return list(word)

def read_file():
    with open("words.csv", "r") as file:
        reader = csv.reader(file)
        words = list(reader)
        choice = random.choice(words)
    return choice[0]
        

main()