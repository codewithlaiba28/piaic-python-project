import random
def guess():
    random_no = random.randint(1 , 100)
    user_guess = 0
    while user_guess != random_no:
        user_guess = int(input(" Guess a number 1 to 100: "))
        if user_guess > random_no:
            print("SORRY, Guess Again. Too Low: ")
        elif user_guess < random_no:
            print("SORRY, Guess Again. Too High: ")  
    print(f"Congrates, you have guess the number {random_no} Correctly !")   
guess()  