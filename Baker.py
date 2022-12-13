"""The baker object which has all information about each baker"""


class Baker:
    def __init__(self, weight, name, char):
        self.name = name            # Name of baker ("Baker #")
        self.weight = weight        # Weight of each baker (Constant)
        self.currentScore = 0       # Score for each round
        # Amount of wins a baker has (trial wins not round wins)
        self.win_count = 0
        self.win_percentage = 0     # Percentage of times the baker wins
        self.final_three = 0
        self.avg_week_eliminated = 0
        self.weeks_eliminated = {"Week 1": 0, "Week 2": 0, "Week 3": 0, "Week 4": 0, "Week 5": 0,
                                 "Week 6": 0, "Week 7": 0, "Week 8": 0, "Week 9": 0}
        self.second_place = 0
        self.third_place = 0


        self.char = char            # char which is unique to the baker
        self.num_final_rounds = 0   # Amount of rounds in final (top 3)
        self.num_final_five = 0     # Amount of rounds in top 5
        # The rank for each round (3 rounds per removal)
        self.rank = 0
        # The ranks for each round (Used to see of baker should be removed)
        self.cumulative_ranks = []
        # Cumulative score per ROUND (every 3 challenges)
        self.cumulative_score = 0
