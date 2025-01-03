import random
def game():
    user = input("What's your choice ! 'r' for rock, 'p' for paper, 's' for scissor \n")
    computer = random.choice(['r','p','s'])
    if user == computer:
        return 'It\'s a tie'
    if win(user,computer):
        return 'You won!' 
    return 'You loss'   
def win (player,opponent):
    #r>s,s>p,p>r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r') :
        return True
print(game())  