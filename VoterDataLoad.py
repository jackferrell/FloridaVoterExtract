import csv
from County import County
#I wrote a couple of classes you can define a county and in the constructor pass the 3 letters that name the text file (dont need the numbers after)
#as an example I loaded duval and printed its stats along with the democratic party's stats from there
duval = County("DUV")
duval.load_data()
duval.process_data()
print("This is statistics of Duval County")
duval.display()
print("Stats of the Dem Party in Duval")
duval.party_affiliations["DEM"].display()