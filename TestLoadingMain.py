import csv
import sortedcontainers as smp
from County import County
#I wrote a couple of classes you can define a county and in the constructor pass the 3 letters that name the text file (dont need the numbers after)
#as an example I loaded duval and printed its stats along with the democratic party's stats from there
duval = County("DUV")
duval.load_data()
duval.store_people()
duval.process_data()

duval.search_people_regular("Graham Vaith", "", "8080 timbermill rd")
duval.search_people_sorted("Graham Vaith", "",  "8080 timbermill rd")

