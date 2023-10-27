import random
def random_fruit_selector(fruits):
    word = random.choice(fruits)
    return word

favourite_fruits = ["Mango", "Lychee", "Banana", "Pear", "Apple"]
random_fruit = random_fruit_selector(favourite_fruits)


def check_guess(guess):
    guess = guess.lower()
    if guess in random_fruit:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True: 
        guess = input("Enter a letter ")
        if len(guess) != 1 and not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.") 
        else: 
            print("Valid letter")
            break
        check_guess(guess)

ask_for_input()
