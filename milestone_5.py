import random
class Hangman:

    #Constructor 
    def __init__(self, word_list, num_lives=5):

        """These are the attributes that are initialised in the class""" 
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    #Check guess method:
    """
    The check guess methods
    
    Takes the guess of the user as input and checks whether in the word. 
    it doesn't return anything just yet. 
    
    """
    def check_guess(self, guess):
            guess = guess.lower()
            if guess in self.word:
                print(f'Good guess! {guess} is in the word.')
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        self.word_guessed[i] = guess
                self.num_letters -= 1 
            else:
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word.")
                print(f"You have {self.num_lives} lives left")
                

            self.word_guessed.replace("_", )


                
    
    
    
    #Ask for input method:
    """
    This method takes no input, and asks the user to give an input.
    
    The way it works is by asking 
    """
    def ask_for_input(self):
        while True: 
            guess = input("Enter a letter ")
            if len(guess) != 1 and not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


animals = Hangman(["cows", "pigs"])





def play_game(word_list):
    num_lives = 5
    game = animals
    game(word_list, num_lives)
    while True: 
        if num_lives == 0: 
            print("You lost!")
            break 
        elif len > 0:
            animals.ask_for_input()
        else:
            print("Congratulations. You won the game!")

