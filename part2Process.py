# libraries
import requests
import sys
from operator import itemgetter

# get the api
baseUrl = "https://techtest.rideways.com/"
suppliers = ["dave", "eric", "jeff"]

# all possible cars + number of people
cars = {
    'STANDARD' : 4,
    'EXECUTIVE' : 4,
    'LUXURY' : 4,
    'PEOPLE_CARRIER' : 6,
    'LUXURY_PEOPLE_CARRIER' : 6,
    'MINIBUS' : 16,
}

# variables
Dave = True
Eric = True
Jeff = True
options = []

# error if not all parameteres are inserted
if (len(sys.argv)) < 3:
    print("Error")
    sys.exit(0)
else:
    pickup = sys.argv[1]
    dropoff = sys.argv[2]
    passengers = sys.argv[3]

# searching through all the possible cars from all the apis
# and keep in mind what is correct in the given order

formedUrlEric = baseUrl + suppliers[1] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestEric = requests.get(formedUrlEric, timeout=1)
    jsonEric = requestEric.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    Eric = False

formedUrlDave = baseUrl + suppliers[0] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestDave = requests.get(formedUrlDave, timeout=1)
    jsonDave = requestDave.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    Dave = False

formedUrlJeff = baseUrl + suppliers[2] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestJeff = requests.get(formedUrlJeff, timeout=1)
    jsonJeff = requestJeff.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    Jeff = False

# get suppliers or get errors for every apis
if Eric:
    if "error" in jsonEric:
        Eric = False
    else:
        optionsEric = jsonEric['options']
        for option in optionsEric:
            option['supplier'] = "Eric"
        options = options + optionsEric

if Dave:
    if "error" in jsonDave:
        Dave = False
    else:
        optionsDave = jsonDave['options']
        for option in optionsDave:
            option['supplier'] = "Dave"
        options = options + optionsDave

if Jeff:
    if "error" in jsonJeff:
        Jeff = False
    else:
        optionsJeff = jsonJeff['options']
        for option in optionsJeff:
            option['supplier'] = "Jeff"
        options = options + optionsJeff


# go through all the options that were selected above
branch = {branch['car_type']:branch for branch in options}.values()

# arrange them in ascending order
branchSorted = sorted(branch, reverse=True, key=itemgetter("price"))

# print all options possible in ascending order
for option in branchSorted:
    if (int(cars[option['car_type']]) >= int(passengers)):
        print(option['car_type'] + " - " + str(option['supplier']) + " - " + str(option['price']))