import numpy as np
import pandas as pd
from Baker import Baker
# import matplotlib.pyplot as plt


# For Data Formating
baker_names = []
baker_probabilities = []
baker_wins = {"Baker 1":0,"Baker 2":0,"Baker 3":0,"Baker 4":0,"Baker 5":0,"Baker 6":0,
               "Baker 7":0,"Baker 8":0,"Baker 9":0,"Baker 10":0,"Baker 11":0,"Baker 12":0}

BAKER_RANKS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8, 6)
data = pd.DataFrame()


def intialize_data(baker_list):
    for baker in baker_list:
        # Only names
        baker_names.append(baker.name)
        
        # Only probabilites
        baker_probabilities.append(baker.probability)
        

        
def pickVal(weight):
    return np.random.randint(0,weight)


def resetScores(baker_list_copy):
    for baker in baker_list_copy:
        baker.currentScore = 0
        
    
    
def simulate_wins(baker_list:list):
    baker_list_copy = baker_list.copy()
    
    while len(baker_list_copy) > 1:
        for baker in baker_list_copy:
            for challenge in range(3):
                baker.currentScore += pickVal(baker.weight)
          
        highest_score = -1
        highest_score_baker = Baker(-1, "NULL")
        
        for baker in baker_list_copy:
            if baker.currentScore > highest_score:
                highest_score = baker.currentScore
                highest_score_baker = baker
        del baker_list_copy[baker_list_copy.index(highest_score_baker)]
    print(baker_list_copy[0].name)
    baker_wins[baker_list_copy[0].name] += 1



def calcProbabilities(baker_list, num_epochs):
    for winner in baker_list:
        winner.probability = (int) (winner.score / num_epochs)

        
        
def display_DataFrame():

    print(
        baker_wins.values()
        # pd.DataFrame({"Bakers": baker_names, "Wins": baker_wins})
    )
def main():
    try:
        i:int = int(input("Please enter the amount of trials to run: "))
    except:
        return

    run(i)


def run(epochs:int):
    baker_list = []
    
    for i in range(12):
        baker_list.append(Baker(BAKER_RANKS[0],("Baker " + str(i + 1))))
        
    for i in range(epochs):
        simulate_wins(baker_list)
    # intialize_data(baker_list)
    display_DataFrame()

    





if __name__ == '__main__':
    main()