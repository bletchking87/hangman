import random
def random_fruit_selector(fruits):
    word = random.choice(fruits)
    print(word)

favourite_fruits = ["Mango", "Lychee", "Banana", "Pear", "Apple"]

random_fruit_selector(favourite_fruits)


user_guess = input("Enter a letter ")
if len(user_guess) == 0 and user_guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input")