## Hangman Game

import random

# A function to select random word from predifiend list of words
def select_random_word():
    return random.choice(["python","hangman","programming","developer","challange","function"])


#Function to create string representation of word showing correctly guessed letters
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


#Funtion that contains main logic of game
def hangman():
    print("Welcome to Hangman!")

    word= select_random_word()  #calling function to select random word
    guessed_letters = set()  # set to store gussed letters by player
    incorrect_guess = 0  # to keep track of incorrect gusses
    max_attempts = 6  # max attempts a user can use in case of wrong guess
    
    print(f"\n The Word has {len(word)} letters : {display_word(word,guessed_letters)}") #Display initial state of word

    while incorrect_guess < max_attempts:
        guess = input("\nEnter a letter : ").lower()

        if len(guess) !=1 or not guess.isalpha():
            print("Please enter a single valid letter. ")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter!")
            continue
        
        guessed_letters.add(guess)

        if guess in word:
            print("Good Guess!")
        else:
            incorrect_guess += 1
            print(f"Wrong guess ! Attempts left : {max_attempts - incorrect_guess}")

        current_display = display_word(word, guessed_letters)
        print(f"\n Word : {current_display }")

        if "_" not in current_display:
            print("\n Congratulations ! You guessed the word!")
            return
        
    print(f"\nGame Over! The word was : {word}")

def main_menu():
    while True:
        print("\n ===Hangman Game=== ")
        print("1 . Start Game")
        print("0 Exit")
        choice=input("Enter your choice : ")

        if choice == "1":
            hangman()
        elif choice == "0":
            print("Good Bye!!")
            break
        else:
            print("Invalid Choice . Please try again")


if __name__ == "__main__":
    main_menu()

