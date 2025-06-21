# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from random import choice

count = 0

def player(prev_play, opponent_history=[]):

    global count
    
    prev_play = choice(['R','P','S']) if prev_play == '' else prev_play

    opponent_history.append(prev_play)

    #guess = choice(['R','P','S'])

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    non_ideal_response = {'S': 'P', 'P': 'R', 'R': 'S'}

    if count < 1000 or (count >= 3000 and count <4000):

        guess = ideal_response[opponent_history[-1]]

        count+=1

    elif count >= 1000 and count <2000:

        if opponent_history[-1] == opponent_history[-4]:

            guess = ideal_response[opponent_history[-1]]

        else:

            guess = non_ideal_response[opponent_history[-2]]

        count+=1

    elif count >= 2000 and count <3000:

        if opponent_history[-1] == opponent_history[-2]:

            guess = ideal_response[opponent_history[-8]]

        else:

            guess = non_ideal_response[opponent_history[-1]]

        count+=1
        
    return guess
