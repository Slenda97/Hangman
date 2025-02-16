def main():
    word = get_word()
    print(word)
    
def get_word():
    word = input("Enter a word: ")
    word = word.lower()
    return word
    

main()