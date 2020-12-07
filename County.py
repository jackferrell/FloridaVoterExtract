import csv
import time
import sortedcontainers as smp
from Party import Party
from Person import Person
class County:
    def __init__(self, file_name):
        #Most of the keys here are hard coded, taken straight from the document about which number represents which race, and what the party codes are
        self.countycode = file_name
        self.file_name = file_name + "_20201027.txt"
        self.races = { "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "9": 0}
        self.party_affiliations = { "CPF": Party(), "DEM": Party(), "ECO": Party(), "GRE": Party(), "IND": Party(), "LPF": Party(), "NPA": Party(), "PSL": Party(), "REF": Party(), "REP": Party()}
        self.genders = { "M": 0, "F": 0, "U": 0}
        self.total_voters = 0
        self.active_voters = 0
        self.race_percentages = { "1": 0.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0, "6": 0.0, "7": 0.0, "8": 0.0, "9": 0.0}
        self.gender_percentages = { "M": 0.0, "F": 0.0, "U": 0.0}
        self.party_percentages = { "CPF": 0.0, "DEM": 0.0, "ECO": 0.0, "GRE": 0.0, "IND": 0.0, "LPF": 0.0, "NPA": 0.0, "PSL": 0.0, "REF": 0.0, "REP": 0.0}
        self.people_dict = {}
        self.people_sorted_dict = smp.SortedDict()

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

    #stores the people in two dictionaries
    def store_people(self):
        with open(self.file_name, "r") as county_file:
            reader = csv.reader(county_file, dialect="excel-tab")
            for row in reader:
                #loads in everything lowercase to make search easier
                name = row[4] + " " + row[2]
                name = name.lower()
                temp_person = Person(row[4].lower(), row[2].lower())
                temp_person.set_middle_name(row[5].lower())
                temp_person.set_suffix(row[3].lower())
                temp_person.set_address_l1(row[7].lower())
                temp_person.set_address_l2(row[8].lower())
                temp_person.set_city(row[9].lower())
                temp_person.set_precinct(row[24].lower())
                temp_person.set_dob(row[21].lower())
                temp_person.set_zipcode(row[11])
                temp_person.set_county(self.countycode)
                if row[28] == "ACT":
                    temp_person.set_active(True)
                else:
                    temp_person.set_active(False)
                if self.people_dict.get(name, False) == False:
                    self.people_dict[name] = []
                self.people_dict[name].append(temp_person)
                self.people_sorted_dict.setdefault(name, [])
                self.people_sorted_dict[name].append(temp_person)
    

    #this is assuming name is "<First Name>" + " " + "<Last Name>"
    #Address is also assumed to be "<line 1>" + " " + "<line 2>"
    #returns precinct number
    #returns -1 if not found
    def search_people_regular(self, name,  address):
        input_time = 0
        name = name.lower()
        address = address.lower()
        #correction for 3 spaces in address from data
        address_arr = address.split(" ", 1)
        number = address_arr[0] + "   "
        address = number + address_arr[1] + " "
        start_time = time.time()
        #check if voter exists
        if self.people_dict.get(name, False) == False:
             print("Error: Voter not found")
             time_taken = time.time() - start_time
             print("Search took " + str(time_taken) + " seconds for the HashMap")
             return -1
        #voter's name is in the map    
        else:
            for person in self.people_dict[name]:
                #check for if they don't have a second line in their address
                #this caused a bug at first with the extra space
                if(person.address_l2 == " "):
                    if (person.address_l1) == address:
                        #check to see if birthday is right
                        time_taken = time.time()- start_time
                        print(person.dob)
                        #input time is tracked to correct the search time to not include how long it took to get user input
                        input_time_first = time.time()
                        correct = input("Is this your date of birth? y/n ")
                        input_time = time.time() - input_time_first
                        if(correct == "y"):
                            print("Voter found.")
                            print("Search took " + str(time_taken) + " seconds for the HashMap")
                            return person
                else:
                    total_address = str(person.address_l1 + person.address_l2 + " ")
                    if (total_address) == address:
                        time_taken = time.time()- start_time
                        print(person.dob)
                        #input time is tracked to correct the search time to not include how long it took to get user input
                        input_time_first = time.time()
                        correct = input("Is this your date of birth? y/n ")
                        input_time = time.time() - input_time_first
                        if(correct == "y"):
                            print("Voter found.")
                            print("Search took " + str(time_taken) + " seconds for the HashMap")
                            return person
        #voter name found but no matching address
        print("Error: Voter not found")
        time_taken = time.time() - start_time - input_time
        print("Search took " + str(time_taken) + " seconds for the HashMap")
        return -1
    
    #same method but for the sorted dictionary
    def search_people_sorted(self, name, address):
        input_time = 0
        name = name.lower()
        address = address.lower()
        #correction for 3 spaces in address from data
        address_arr = address.split(" ", 1)
        number = address_arr[0] + "   "
        address = number + address_arr[1] + " "
        start_time = time.time()
        #check if voter exists
        if self.people_sorted_dict.get(name, False) == False:
             print("Error: Voter not found")
             time_taken = time.time() - start_time
             print("Search took " + str(time_taken) + " seconds for the tree based Map")
             return -1
        #voter's name is in the map    
        else:
            for person in self.people_sorted_dict[name]:
                #check for if they don't have a second line in their address
                #this caused a bug at first with the extra space
                if(person.address_l2 == " "):
                    if (person.address_l1) == address:
                        #check to see if birthday is right
                        time_taken = time.time()- start_time
                        print(person.dob)
                        #input time is tracked to correct the search time to not include how long it took to get user input
                        input_time_first = time.time()
                        correct = input("Is this your date of birth? y/n ")
                        input_time = time.time() - input_time_first
                        if(correct == "y"):
                            print("Voter found.")
                            print("Search took " + str(time_taken) + " seconds for the tree based Map")
                            return person
                else:
                    total_address = str(person.address_l1 + person.address_l2 + " ")
                    if (total_address) == address:
                        time_taken = time.time()- start_time
                        print(person.dob)
                        #input time is tracked to correct the search time to not include how long it took to get user input
                        input_time_first = time.time()
                        correct = input("Is this your date of birth? y/n ")
                        input_time = time.time() - input_time_first
                        if(correct == "y"):
                            print("Voter found.")
                            print("Search took " + str(time_taken) + " seconds for the tree based Map")
                            return person
        #voter name found but no matching address
        print("Error: Voter not found")
        time_taken = time.time() - start_time - input_time
        print("Search took " + str(time_taken) + " seconds for the tree based Map")
        return -1
        
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

    def create_file(self):
        f = open("statistics.txt", "a")
        f.write(str(self.countycode) + "\t")
        f.write("Number of Voters: " + str(self.total_voters) + "\t")
        f.write("Number of Active Voters: " + str(self.active_voters) + "\t")
        f.write("American Indian or Alaskan Native: " + str("{:.2f}".format(self.race_percentages["1"])) + "%" + "\t")
        f.write("Asian Or Pacific Islander: " + str("{:.2f}".format(self.race_percentages["2"])) + "%" + "\t")
        f.write("Black, Not Hispanic: " + str("{:.2f}".format(self.race_percentages["3"])) + "%" + "\t")
        f.write("Hispanic: " + str("{:.2f}".format(self.race_percentages["4"])) + "%" + "\t")
        f.write("White, Not Hispanic: " + str("{:.2f}".format(self.race_percentages["5"])) + "%" + "\t")
        f.write("Other: " + str("{:.2f}".format(self.race_percentages["6"])) + "%" + "\t")
        f.write("Multi-racial: " + str("{:.2f}".format(self.race_percentages["7"])) + "%" + "\t")
        f.write("Unknown: " + str("{:.2f}".format(self.race_percentages["9"])) + "%" + "\t")
        f.write("Constitution Party of Florida: " + str("{:.2f}".format(self.party_percentages["CPF"])) + "%" + "\t")
        f.write("Florida Democratic Party: " + str("{:.2f}".format(self.party_percentages["DEM"])) + "%" + "\t")
        f.write("Ecology Party of Florida: " + str("{:.2f}".format(self.party_percentages["ECO"])) + "%" + "\t")
        f.write("Green Party of Florida: " + str("{:.2f}".format(self.party_percentages["GRE"])) + "%" + "\t")
        f.write("Independent Party of Florida: " + str("{:.2f}".format(self.party_percentages["IND"])) + "%" + "\t")
        f.write("Libertarian Party of Florida: " + str("{:.2f}".format(self.party_percentages["LPF"])) + "%" + "\t")
        f.write("No Party Affiliation: " + str("{:.2f}".format(self.party_percentages["NPA"])) + "%" + "\t")
        f.write("Party for Socialism and Liberation - Florida: " + str("{:.2f}".format(self.party_percentages["PSL"])) + "%" + "\t")
        f.write("Reform Party of Florida: " + str("{:.2f}".format(self.party_percentages["REF"])) + "%" + "\t")
        f.write("Republican Party of Florida: " + str("{:.2f}".format(self.party_percentages["REP"])) + "%" + "\t")
        f.write("Male: " + str("{:.2f}".format(self.gender_percentages["M"])) + "%" + "\t")
        f.write("Female: " + str("{:.2f}".format(self.gender_percentages["F"])) + "%" + "\t")
        f.write("Other: " + str("{:.2f}".format(self.gender_percentages["U"])) + "%" + "\t")
        f.write("\n")
        f.close()