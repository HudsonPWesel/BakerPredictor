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
scores = []
baker_win_percentages = []  # Win percentages of bakers
# CONSTANTS
BAKER_WEIGHTS = (14, 12, 10, 10, 10, 10, 10, 10, 10, 10, 8,
                 6)         # Weights if each baker in order
CHARS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
         'K', 'L')  # Bakers corresponding letter in order


def set_wins(num_epochs: int):
    for baker in baker_list:
        # SET NUMBER OF WINS
        # baker.name -> tuple (e.g) ('Baker 1',) --> Must index tuple
        baker_wins[baker.name[0]] = baker.win_count

        # SET WIN PERCENTAGES
        baker_win_percentages.append(
            round((baker_wins[baker.name[0]] / num_epochs) * 100, 3))


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
        chosen_char = 'Q'
        if(len(char_arr) != 0):
            chosen_num = np.random.randint(0, len(char_arr))
            chosen_char = char_arr[chosen_num]

        # Remove all occurances of char from the list of baker chars (remove baker)
        char_arr = [
            current_char for current_char in char_arr if current_char != char_arr[chosen_num]]
        assign_rank(chosen_char, i)


def calc_scores(scores):
    for baker in baker_list_copy:
        for score in baker.cumulative_ranks:
            baker.cumulative_score += score
        scores.append(baker.cumulative_score)
    # print(scores)


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
    for baker in baker_list_copy:
        baker.cumulative_ranks.clear()
        baker.cumulative_score = 0


def simulate_challenges(scores):
    for challenge in range(3):
        # Reset arr for each challenge
        fill_char_arr()  # Fills with 120 chars based on weight
        set_baker_scores()

        calc_scores(scores)  # Calculate cumulative score


def simulate_round(week, scores):
    simulate_challenges(scores)  # Simulate 3 Challenges
    # Eliminate baker with max score of scores
    eliminate_baker(week, scores)
    for baker in baker_list_copy:
        baker.cumulative_score = 0
        baker.cumulative_ranks = []


def simulate_final_round(scores: list):
    print(len(baker_list_copy))
    simulate_challenges(scores)
    # print(str(scores.clear()))
    third_place_baker = None

    for baker in baker_list_copy:
        # Get real baker in our main list
        real_baker = get_baker(baker)
        real_baker.final_three += 1

        if(len(baker_list_copy)) > 1:
            if real_baker is None:
                pass
            if baker.cumulative_score == max(scores):
                # Is This Round For Third Place?
                if(len(baker_list_copy)) > 2:
                    real_baker.third_place += 1
                else:
                    real_baker.second_place += 1

        elif(len(baker_list_copy)) == 1:
            print("WINNNG BAKER")
            real_baker.win_count += 1
    scores.clear()


def simulate():
    """Simulate a single trial"""
    global baker_list_copy
    baker_list_copy = baker_list.copy()

    # RUNS UP TO FINAL 3
    # todo DO WHAT IS NEEDED FOR FINAL THREE
    for week in range(9):
        # Runs three times to simulate the three challenges each week
        reset_baker_scores()  # Reset cumulative ranks
        simulate_round(week, scores)

    simulate_final_round(scores)
    scores.clear()
    # print("OIEUFWHOIEHJFOIJEWFOIFJE")
    # print(scores)

    # print(scores)

    # week 1 11 | 2 10 | 3 9 | 4 8 | 5 7 | 6 6 | 7 5 | 8 4 | 9 3 | 10

    baker_list_copy[0].win_count += 1


def get_data():
    global all_week_vals
    all_week_vals = [[], [], [], [], [], [], [], [], [], [], [], []]
    for i in range(0, 9):
        for baker in baker_list:
            all_week_vals[i].append(
                baker.weeks_eliminated["Week " + (str(i + 1))])

    global third_place_vals, second_place_vals, final_three_vals
    third_place_vals = []
    second_place_vals = []
    final_three_vals = []

    for baker in baker_list:
        third_place_vals.append(baker.third_place)
        second_place_vals.append(baker.second_place)
        final_three_vals.append(baker.final_three)


def display_DataFrame():
    """Display the final data for each simulation"""

    for week in range(12):
        get_data()
    # {"Bakers": list(baker_wins.keys()),
    # Number of wins per bakers
    # "Wins": list(baker_wins.values()),
    # Avg week baker is eliminated
    #   Weeks Eliminated

    print(
        pd.DataFrame({
                     "Weights": list(BAKER_WEIGHTS),
                     "Bakers": list(baker_wins.keys()),
                     "Win-Percentage": baker_win_percentages,
                     str(list(baker_list[0].weeks_eliminated.keys())[0]):  all_week_vals[0],
                     str(list(baker_list[1].weeks_eliminated.keys())[1]):  all_week_vals[1],
                     str(list(baker_list[2].weeks_eliminated.keys())[2]):  all_week_vals[2],
                     str(list(baker_list[3].weeks_eliminated.keys())[3]):  all_week_vals[3],
                     str(list(baker_list[4].weeks_eliminated.keys())[4]):  all_week_vals[4],
                     str(list(baker_list[5].weeks_eliminated.keys())[5]):  all_week_vals[5],
                     str(list(baker_list[6].weeks_eliminated.keys())[6]):  all_week_vals[6],
                     str(list(baker_list[7].weeks_eliminated.keys())[7]):  all_week_vals[7],
                     str((list(baker_list[8].weeks_eliminated.keys())[8])):  all_week_vals[8],
                     "     " + "Final Three": final_three_vals,
                     "3rd Place Finish": third_place_vals,
                     "2nd Place Finish": second_place_vals,
                     "1st Place Finish": list(baker_wins.values()),

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
            Baker(BAKER_WEIGHTS[i], ("Baker " + str(i + 1), ), CHARS[i]))

    # Run each Simulation
    for i in range(1, epochs+1):
        # % Program Finished
        print(str(i) + " | " + "{:.2f}".format((i/epochs)*100) + "%")
        # Run one simulation (Saves output globally)
        simulate()
    set_wins(epochs)

    # Display data for all the simulations
    display_DataFrame()


if __name__ == '__main__':
    main()
