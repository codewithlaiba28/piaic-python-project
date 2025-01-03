
import random
import string

words=["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tomato", "ugli", "vanilla",
    "watermelon", "xylophone", "yellow", "zucchini", "abacus", "brilliant", "candy", "dog", "elephant", "flower",
    "giraffe", "happy", "ice", "jungle", "kangaroo", "lemonade", "mango", "ninja", "octopus", "parrot",
    "queen", "rabbit", "snake", "tiger", "unicorn", "vulture", "whale", "xenon", "yarn", "zebra",
    "antelope", "butterfly", "cucumber", "dolphin", "eagle", "fox", "goat", "hippopotamus", "ink", "jellyfish",
    "koala", "lion", "monkey", "noodles", "owl", "penguin", "quail", "rocket", "sunflower", "tree",
    "umbrella", "vulture", "wolf", "xerox", "yak", "zinnia", "art", "book", "cat", "dog",
    "elephant", "fox", "guitar", "house", "island", "jackal", "kite", "lemon", "moon", "notebook",
    "orange", "pencil", "quilt", "rose", "star", "turtle", "up", "vase", "wind", "xmas",
    "yellow", "zebra", "ape", "berry", "cloud", "dove", "eagle", "flame", "gold", "hop",
    "ink", "jack", "key", "lava", "match", "nest", "oak", "petal", "quack", "rain"]

def get_valid_word(words):
    word = random.choice(words)
    return word.upper()  
def hangman():
    word = get_valid_word(words)  
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)  
    used_letters = set()  
    incorrect_guesses = 0  
    max_incorrect_guesses = 10  
    while len(word_letters) > 0 and incorrect_guesses < max_incorrect_guesses:
        print(f"\nYou have used these letters: {' '.join(sorted(used_letters))}")  
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: " + ' '.join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
    
        if user_letter in alphabet - used_letters: 
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  
            else:
                incorrect_guesses += 1
                print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} attempts left.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please enter a valid letter (A-Z).")
    # End of game condition
    if len(word_letters) == 0:
        print(f"Congratulations! You've guessed the word: {word}")
    else:
        print(f"Game Over! The word was: {word}")

# Call the hangman function to start the game
hangman()
