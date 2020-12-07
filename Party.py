class Party:
    #Fairly similar to the county class, but only keeps track of race and gender
    def __init__(self):
        self.races = { "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "9": 0}
        self.genders = { "M": 0, "F": 0, "U": 0}
        self.num_voters = 0
        self.race_percentages = { "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 0.0, "9": 0.0}
        self.gender_percentages = { "M": 0.0, "F": 0.0, "U": 0.0}

    #similar process data function to the county class, just calculates the percentage makeup of the genders and races
    def process_data(self):
        #check in case some counties had no members of a certain party
        if self.num_voters > 0:
            for key in self.race_percentages:
                self.race_percentages[key] = float(self.races[key]) / float(self.num_voters) * 100
            for key in self.gender_percentages:
                self.gender_percentages[key] = float(self.genders[key]) / float(self.num_voters) * 100

    #prints all the data
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


