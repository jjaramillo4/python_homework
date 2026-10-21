#Task 4
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        display = ""
        guesses.append(letter)
        for char in secret_word:
            if (char in guesses):
                display += char
            else: 
                display+= '_'
        if(display == secret_word):
            print(f"You got it! {display}")
            return True
        else:
            print(display)
            return False
    return hangman_closure

user_secret = input("what's the secret word?: " )
play = make_hangman(user_secret)

while True:
    letter = input("guess a letter: ")
    result = play(letter)
    if result == True:
        break
