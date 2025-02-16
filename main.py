def main():
    word = get_word()
    num_of_guesses = 8
    list_word = split_word(word)
    word_length = len(list_word)
    guess_word = []
    for i in range(word_length):
        guess_word.append("_")
    for i in range(num_of_guesses):
        print(" ".join(guess_word))
        guess = input("Enter a letter: ")
        if guess in list_word:
            for i in range(word_length):
                if list_word[i] == guess:
                    guess_word[i] = guess
        else:
            num_of_guesses -= 1
            print(f"Incorrect! You have {num_of_guesses} guesses left.")
        if guess_word == list_word:
            print("You win!")
            break
    
        
    
def get_word():
    word = input("Enter a word: ")
    if word == "":
        print("You must enter a word.")
        word = get_word()
    word = word.lower()
    return word

def split_word(word):
    return list(word)
    

main()