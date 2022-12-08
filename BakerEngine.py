from typing import Any

from Baker import Baker
# import pandas as pd
# from scipy.stats import norm
# import matplotlib.pyplot as plt

# For Data Formating
import pandas as pd
import numpy as np
# weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6",
#          "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", ]
# Global Variables
baker_wins = {"Baker 1": 0, "Baker 2": 0, "Baker 3": 0, "Baker 4": 0,
              "Baker 5": 0, "Baker 6": 0, "Baker 7": 0, "Baker 8": 0,
              "Baker 9": 0, "Baker 10": 0, "Baker 11": 0, "Baker 12": 0}
char_arr = []   # Chars for each round
baker_list = []  # List of baker objects
week_vals = []  # List of vals for each week
# CONSTANTS
BAKER_RANKS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8,
               6)         # Weights if each baker in order
CHARS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L')  # Bakers corresponding letter in order


def set_num_wins():
    for baker in baker_list:
        # baker.name -> tuple (e.g) ('Baker 1',) --> Must index tuple
        baker_wins[baker.name[0]] = baker.win_count

def fill_char_arr():
    """Fill list of chars determined by the weight of each baker"""
    char_arr.clear()
    for baker in baker_list_copy:
        for i in range(baker.weight):
            char_arr.append(baker.char)


def set_baker_scores():
    """Find winner of each challenge (Three for each baker removal)"""
    global char_arr
    # Rank is place per challenge (1st, 2nd, 3rd, etc. places)

    # Find range and a char (Each baker has a char that corresponds to it)
    for i in range(0, 13):
        chosen_num = 0
        if(len(char_arr) != 0):
            chosen_num = np.random.randint(0, len(char_arr))
            chosen_char = char_arr[chosen_num]

        # Remove all occurances of char from the list of baker chars (remove baker)
        char_arr = [
            current_char for current_char in char_arr if current_char != char_arr[chosen_num]]
        assign_rank(chosen_char, i)


def assign_rank(chosen_char, current_rank,):
    """Assign a rank to each baker in the baker Object"""
    for baker in baker_list_copy:

        if baker.char == chosen_char:
            baker.cumulative_ranks.append(current_rank)


def find_range() -> int:
    """Find the range of the bakers by adding up all the bakers weight"""
    total = 0
    for baker in baker_list_copy:
        total += baker.weight
    return total - 1


def calc_scores(scores):
    for baker in baker_list_copy:
        for score in baker.cumulative_ranks:
            baker.cumulative_score += score
        scores.append(baker.cumulative_score)


def eliminate_baker(current_week, scores):
    # TODO: Problem: After the baker is eliminated, we cant use that baker to display in DF - EASY FIX!

   # print("MAX: " + str(max(scores)))
   # for baker in baker_list_copy:
   #     print(str(baker.name) + " " + str(baker.cumulative_score))

    for baker in baker_list_copy:
        if baker.cumulative_score == max(scores):
            # print("FOUND: " + str(baker.name))
            real_baker = get_baker(baker)
            if real_baker is None:
                pass
            # print("FOUND REAL: " + str(real_baker.name))
            real_baker.weeks_eliminated["Week " + (str(current_week + 1))] += 1
            baker_list_copy.remove(baker)

    # print(baker_list[0].weeks_eliminated)

    # print("Remaining Bakers" + (str(len(baker_list_copy))))


def get_baker(baker: Baker):
    # print(baker)
    for b in baker_list:
        if b.name is baker.name:
            return b
    return None


def reset_baker_scores():
    for baker in baker_list:
        baker.cumulative_ranks = []


def simulate():
    scores = []

    """Simulate a single trial"""
    global baker_list_copy
    baker_list_copy = baker_list.copy()

    # RUNS UP TO FINAL 3
    # todo DO WHAT IS NEEDED FOR FINAL THREE
    for week in range(9):
        # Runs three times to simulate the three challenges each week
        reset_baker_scores()  # Reset cumulative ranks
        for challenge in range(3):
            # Reset arr for each challenge
            fill_char_arr()  # Fills with 120 chars based on weight
            set_baker_scores()
        calc_scores(scores)  # Calculate cumulative score
        # Eliminate baker with max score of scores
        eliminate_baker(week, scores)
        scores = []
    baker_list_copy[0].win_count += 1

#     FINAL Three




def get_data():
    global all_week_vals
    all_week_vals = [[], [], [], [], [], [], [], [], [], [], [], []]
    for i in range(0, 9):
        for baker in baker_list:
            all_week_vals[i].append(
                baker.weeks_eliminated["Week " + (str(i + 1))])

  #  print(all_week_vals)
    # return temp_week_vals

def simulate_final_round():
    print()

def display_DataFrame():
    """Display the final data for each simulation"""
    print(list(baker_wins.keys()))
    for week in range(12):
        get_data()
    # {"Bakers": list(baker_wins.keys()),
    # Number of wins per bakers
    # "Wins": list(baker_wins.values()),
    # Avg week baker is eliminated
    #   Weeks Eliminated

    print(
        pd.DataFrame({
                     "Bakers": list(baker_wins.keys()),
                       "Wins": list(baker_wins.values()),
                      str(list(baker_list[0].weeks_eliminated.keys())[0]):  all_week_vals[0],
                      str(list(baker_list[1].weeks_eliminated.keys())[1]):  all_week_vals[1],
                      str(list(baker_list[2].weeks_eliminated.keys())[2]):  all_week_vals[2],
                      str(list(baker_list[3].weeks_eliminated.keys())[3]):  all_week_vals[3],
                      str(list(baker_list[4].weeks_eliminated.keys())[4]):  all_week_vals[4],
                      str(list(baker_list[5].weeks_eliminated.keys())[5]):  all_week_vals[5],
                      str(list(baker_list[6].weeks_eliminated.keys())[6]):  all_week_vals[6],
                      str(list(baker_list[7].weeks_eliminated.keys())[7]):  all_week_vals[7],
                      str(list(baker_list[8].weeks_eliminated.keys())[8]):  all_week_vals[8],

                      })
    )


def main():
    """Start of program...!"""
    try:
        i: int = int(input("Please enter the amount of trials to run: "))
    except:
        return
    run(i)


def run(epochs: int):
    """Run the simulation a set amount of times"""

    # Initialze Baker Objects
    for i in range(12):
        baker_list.append(
            Baker(BAKER_RANKS[i], ("Baker " + str(i + 1), ), CHARS[i]))

    # Run each Simulation
    for i in range(1, epochs+1):
        # % Program Finished
        print(str(i) + " | " + "{:.2f}".format((i/epochs)*100) + "%")
        # Run one simulation (Saves output globally)
        simulate()
    set_num_wins()

    # Display data for all the simulations
    display_DataFrame()


if __name__ == '__main__':
    main()


# from scipy.stats import norm
# import matplotlib.pyplot as plt


# For Data Formating

# baker_wins = {"Baker 1": 0, "Baker 2": 0, "Baker 3": 0, "Baker 4": 0, "Baker 5": 0, "Baker 6": 0,
#               "Baker 7": 0, "Baker 8": 0, "Baker 9": 0, "Baker 10": 0, "Baker 11": 0, "Baker 12": 0}
#
# week_elim_count = []
# win_percentages = []
# BAKER_RANKS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8, 6)
# data = pd.DataFrame()
#
#
# def intialize_data(baker_list):
#     temp_week_count = []
#
#     currentWeek = 1
#     # Add Weeks
#
#     print(baker_list[0].weeks_eliminated)
#
#     for baker in baker_list:
#         win_percentages.append(baker.win_percentage)
#
#         # print(baker.weeks_eliminated["Week 1"])
#     for i in range (12):
#         for baker in baker_list:
#             temp_week_count.append(baker.weeks_eliminated["Week " + str(currentWeek)])
#
#         print(temp_week_count)
#         if i < 11:
#             temp_week_count = []
#
#         week_elim_count.append({"Week " + str(currentWeek): temp_week_count})
#         currentWeek += 1
#
#
# def pickVal(weight):
#     return np.random.randint(0, weight)
#
#
# def resetScores(baker_list_copy):
#     for baker in baker_list_copy:
#         baker.currentScore = 0
#
#
# def calc_loss_week(baker_contestents, baker):
#     currentWeek = "Week " + str(12 - len(baker_contestents))
#     baker.weeks_eliminated[currentWeek] += 1
#
#
# def simulate_wins(baker_list: list):
#     currentWeek = 0
#
#     baker_list_copy = baker_list.copy()
#
#     while len(baker_list_copy) > 1:
#         for baker in baker_list_copy:
#             for challenge in range(3):
#                 baker.currentScore += pickVal(baker.weight)
#
#         highest_score = -1
#         highest_score_baker = Baker(-1, "NULL")
#         currentWeek += 1
#
#         for baker in baker_list_copy:
#             if baker.currentScore > highest_score:
#                 highest_score = baker.currentScore
#                 highest_score_baker = baker
#         del baker_list_copy[baker_list_copy.index(highest_score_baker)]
#
#         # Calculate week that baker was elimnated
#         calc_loss_week(baker_list_copy, highest_score_baker)
#
#     # Now that we have one contestent, they're the winner, increment win_count
#     baker_wins[baker_list_copy[0].name] += 1
#
#
# def calc_win_percentile(baker_list, num_epochs):
#     for baker in baker_list:
#         # Rounds to 3 decimals
#         baker.win_percentage = round(
#             (baker_wins[baker.name] / num_epochs) * 100, 3)
#     # baker.probability = baker_wins[baker.name]
#
#
# def display_DataFrame():
#
#     # DYNAMICALLY MAKE ELIM COUNT
#     # print(week_elim_count)[0]
#     # print(str(list(week_elim_count[0].keys())[0]))
#     # print(list(week_elim_count[0].values()))
#     # str(list(week_elim_count[0].keys())[0]): list(week_elim_count[0].values())[0]
#     print(week_elim_count[1])
#
#
#    print(
#         pd.DataFrame({"Bakers": list(baker_wins.keys()),
#                       "Wins": list(baker_wins.values()), "Win-Percentages": win_percentages,
#                       # Num times eliminated in specified week
#                       str(list(week_elim_count[0].keys())[0]): list(week_elim_count[0].values())[0],
#                       str(list(week_elim_count[1].keys())[0]): list(week_elim_count[1].values())[0],
#                       str(list(week_elim_count[2].keys())[0]): list(week_elim_count[3].values())[0],
#                       str(list(week_elim_count[3].keys())[0]): list(week_elim_count[3].values())[0],
#                       str(list(week_elim_count[4].keys())[0]): list(week_elim_count[4].values())[0],
#                       str(list(week_elim_count[5].keys())[0]): list(week_elim_count[5].values())[0],
#                       str(list(week_elim_count[6].keys())[0]): list(week_elim_count[6].values())[0],
#                       str(list(week_elim_count[7].keys())[0]): list(week_elim_count[7].values())[0],
#                       str(list(week_elim_count[8].keys())[0]): list(week_elim_count[8].values())[0],
#                       str(list(week_elim_count[9].keys())[0]): list(week_elim_count[9].values())[0],
#                       str(list(week_elim_count[10].keys())[0]): list(week_elim_count[10].values())[0],
#                       str(list(week_elim_count[11].keys())[0]): list(week_elim_count[11].values())[0],
#                      }
#             ),
#     )
#
# OLD CODE ABOVE
