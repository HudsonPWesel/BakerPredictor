class Baker:
    def __init__(self, weight, name, char):
        self.name = name
        self.weight = weight
        self.currentScore = 0
        self.winCount = 0
        self.win_percentage = 0
        self.weeks_eliminated = {"Week 1": 0, "Week 2": 0, "Week 3": 0, "Week 4": 0, "Week 5": 0,
                                 "Week 6": 0, "Week 7": 0, "Week 8": 0, "Week 9": 0, "Week 10": 0, "Week 11": 0, "Week 12": 0}
        self.char = char
        self.num_final_rounds = 0
        self.num_final_three = 0
        self.rank = 0
        self.cumulative_ranks = []


