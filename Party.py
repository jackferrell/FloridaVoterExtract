class Party:
    #Fairly similar to the county class, but only keeps track of race and gender
    def __init__(self):
        self.races = { "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "9": 0}
        self.genders = { "M": 0, "F": 0, "U": 0}
        self.num_voters = 0
        self.race_percentages = { "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 0.0, "8": 0.0, "9": 0.0}
        self.gender_percentages = { "M": 0.0, "F": 0.0, "U": 0.0}

    def process_data(self):
        self.race_percentages["1"] = float(self.races["1"]) / float(self.num_voters) * 100
        self.race_percentages["2"] = float(self.races["2"]) / float(self.num_voters) * 100
        self.race_percentages["3"] = float(self.races["3"]) / float(self.num_voters) * 100
        self.race_percentages["4"] = float(self.races["4"]) / float(self.num_voters) * 100
        self.race_percentages["5"] = float(self.races["5"]) / float(self.num_voters) * 100
        self.race_percentages["6"] = float(self.races["6"]) / float(self.num_voters) * 100
        self.race_percentages["7"] = float(self.races["7"]) / float(self.num_voters) * 100
        self.race_percentages["9"] = float(self.races["9"]) / float(self.num_voters) * 100
        self.gender_percentages["M"] = float(self.genders["M"]) / float(self.num_voters) * 100
        self.gender_percentages["F"] = float(self.genders["F"]) / float(self.num_voters) * 100
        self.gender_percentages["U"] = float(self.genders["U"]) / float(self.num_voters) * 100

    def display(self):
        print("Race Data: " + str(self.races))
        print("Number of Voters: " + str(self.num_voters))
        print("Percentage Race Data: ")
        print("American Indian or Alaskan Native: " + str("{:.2f}".format(self.race_percentages["1"])) + "%")
        print("Asian Or Pacific Islander: " + str("{:.2f}".format(self.race_percentages["2"])) + "%")
        print("Black, Not Hispanic: " + str("{:.2f}".format(self.race_percentages["3"])) + "%")
        print("Hispanic: " + str("{:.2f}".format(self.race_percentages["4"])) + "%")
        print("White, Not Hispanic: " + str("{:.2f}".format(self.race_percentages["5"])) + "%")
        print("Other: " + str("{:.2f}".format(self.race_percentages["6"])) + "%")
        print("Multi-racial: " + str("{:.2f}".format(self.race_percentages["7"])) + "%")
        print("Unknown: " + str("{:.2f}".format(self.race_percentages["9"])) + "%")
        print("Percentage Gender Data: ")
        print("Male: " + str("{:.2f}".format(self.gender_percentages["M"])) + "%")
        print("Female: " + str("{:.2f}".format(self.gender_percentages["F"])) + "%")
        print("Other: " + str("{:.2f}".format(self.gender_percentages["U"])) + "%")


