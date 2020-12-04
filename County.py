import csv
from Party import Party
class County:
    def __init__(self, file_name):
        #Most of the keys here are hard coded, taken straight from the document about which number represents which race, and what the party codes are
        self.file_name = file_name + "_20201027.txt"
        self.races = { "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "9": 0}
        self.party_affiliations = { "CPF": Party(), "DEM": Party(), "ECO": Party(), "GRE": Party(), "IND": Party(), "LPF": Party(), "NPA": Party(), "PSL": Party(), "REF": Party(), "REP": Party()}
        self.genders = { "M": 0, "F": 0, "U": 0}
        self.total_voters = 0
        self.active_voters = 0
        self.race_percentages = { "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 0.0, "8": 0.0, "9": 0.0}
        self.gender_percentages = { "M": 0.0, "F": 0.0, "U": 0.0}
        self.party_percentages = { "CPF": 0.0, "DEM": 0.0, "ECO": 0.0, "GRE": 0.0, "IND": 0.0, "LPF": 0.0, "NPA": 0.0, "PSL": 0.0, "REF": 0.0, "REP": 0.0}

    #loads number of people associated with parties and races, also counts number of total voters and active voters
    def load_data(self):
        with open(self.file_name, "r") as county_file:
            reader = csv.reader(county_file, dialect="excel-tab")
            for row in reader:
                self.total_voters += 1
                if row[19] != "":
                    self.genders[row[19]] += 1
                self.races[row[20]] += 1               
                (self.party_affiliations[row[23]]).num_voters += 1
                (self.party_affiliations[row[23]]).races[row[20]] += 1
                if row[19] != "":
                    (self.party_affiliations[row[23]]).genders[row[19]] += 1
                if row[28] == "ACT":
                    self.active_voters += 1

    #This is not fantastic code (it is repetitive), but it is the simple percentage calculations of the number of different races and parties in the county
    #It also calls a similar function on each of the parties associated with the county
    def process_data(self):
        self.race_percentages["1"] = float(self.races["1"]) / float(self.total_voters) * 100
        self.race_percentages["2"] = float(self.races["2"]) / float(self.total_voters) * 100
        self.race_percentages["3"] = float(self.races["3"]) / float(self.total_voters) * 100
        self.race_percentages["4"] = float(self.races["4"]) / float(self.total_voters) * 100
        self.race_percentages["5"] = float(self.races["5"]) / float(self.total_voters) * 100
        self.race_percentages["6"] = float(self.races["6"]) / float(self.total_voters) * 100
        self.race_percentages["7"] = float(self.races["7"]) / float(self.total_voters) * 100
        self.race_percentages["9"] = float(self.races["9"]) / float(self.total_voters) * 100
        self.gender_percentages["M"] = float(self.genders["M"]) / float(self.total_voters) * 100
        self.gender_percentages["F"] = float(self.genders["F"]) / float(self.total_voters) * 100
        self.gender_percentages["U"] = float(self.genders["U"]) / float(self.total_voters) * 100
        self.party_percentages["CPF"] = float(self.party_affiliations["CPF"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["DEM"] = float(self.party_affiliations["DEM"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["ECO"] = float(self.party_affiliations["ECO"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["GRE"] = float(self.party_affiliations["GRE"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["IND"] = float(self.party_affiliations["IND"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["LPF"] = float(self.party_affiliations["LPF"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["NPA"] = float(self.party_affiliations["NPA"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["PSL"] = float(self.party_affiliations["PSL"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["REF"] = float(self.party_affiliations["REF"].num_voters) / float(self.total_voters) * 100
        self.party_percentages["REP"] = float(self.party_affiliations["REP"].num_voters) / float(self.total_voters) * 100
        self.party_affiliations["CPF"].process_data()
        self.party_affiliations["DEM"].process_data()
        self.party_affiliations["ECO"].process_data()
        self.party_affiliations["GRE"].process_data()
        self.party_affiliations["IND"].process_data()
        self.party_affiliations["LPF"].process_data()
        self.party_affiliations["NPA"].process_data()
        self.party_affiliations["PSL"].process_data()
        self.party_affiliations["REF"].process_data()
        self.party_affiliations["REP"].process_data()

    #This method just takes the format from the .txt and hard codes the prints
    def display(self):
        print("Race Data: " + str(self.races))
        print("Number of Voters: " + str(self.total_voters))
        print("Number of Active Voters: " + str(self.active_voters))
        print("Percentage Race Data: ")
        print("American Indian or Alaskan Native: " + str("{:.2f}".format(self.race_percentages["1"])) + "%")
        print("Asian Or Pacific Islander: " + str("{:.2f}".format(self.race_percentages["2"])) + "%")
        print("Black, Not Hispanic: " + str("{:.2f}".format(self.race_percentages["3"])) + "%")
        print("Hispanic: " + str("{:.2f}".format(self.race_percentages["4"])) + "%")
        print("White, Not Hispanic: " + str("{:.2f}".format(self.race_percentages["5"])) + "%")
        print("Other: " + str("{:.2f}".format(self.race_percentages["6"])) + "%")
        print("Multi-racial: " + str("{:.2f}".format(self.race_percentages["7"])) + "%")
        print("Unknown: " + str("{:.2f}".format(self.race_percentages["9"])) + "%")
        print("Percentage Party Data: ")
        print("Constitution Party of Florida: " + str("{:.2f}".format(self.party_percentages["CPF"])) + "%")
        print("Florida Democratic Party: " + str("{:.2f}".format(self.party_percentages["DEM"])) + "%")
        print("Ecology Party of Florida: " + str("{:.2f}".format(self.party_percentages["ECO"])) + "%")
        print("Green Party of Florida: " + str("{:.2f}".format(self.party_percentages["GRE"])) + "%")
        print("Independent Party of Florida: " + str("{:.2f}".format(self.party_percentages["IND"])) + "%")
        print("Libertarian Party of Florida: " + str("{:.2f}".format(self.party_percentages["LPF"])) + "%")
        print("No Party Affiliation: " + str("{:.2f}".format(self.party_percentages["NPA"])) + "%")
        print("Party for Socialism and Liberation - Florida: " + str("{:.2f}".format(self.party_percentages["PSL"])) + "%")
        print("Reform Party of Florida: " + str("{:.2f}".format(self.party_percentages["REF"])) + "%")
        print("Republican Party of Florida: " + str("{:.2f}".format(self.party_percentages["REP"])) + "%")
        print("Percentage Gender Data: ")
        print("Male: " + str("{:.2f}".format(self.gender_percentages["M"])) + "%")
        print("Female: " + str("{:.2f}".format(self.gender_percentages["F"])) + "%")
        print("Other: " + str("{:.2f}".format(self.gender_percentages["U"])) + "%")