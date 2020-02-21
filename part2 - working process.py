import requests
import sys
from operator import itemgetter

baseUrl = "https://techtest.rideways.com/"
suppliers = ["dave", "eric", "jeff"]
cars = {
    'STANDARD' : 4,
    'EXECUTIVE' : 4,
    'LUXURY' : 4,
    'PEOPLE_CARRIER' : 6,
    'LUXURY_PEOPLE_CARRIER' : 6,
    'MINIBUS' : 16,
}
Dave = True
Eric = True
Jeff = True
options = []

if (len(sys.argv)) < 3:
    print("Error")
    sys.exit(0)
else:
    pickup = sys.argv[1]
    dropoff = sys.argv[2]
    passengers = sys.argv[3]

formedUrlDave = baseUrl + suppliers[0] + "?pickup=" + pickup + "&dropoff=" + dropoff
try:
    requestDave = requests.get(formedUrlDave, timeout=2)
    jsonDave = requestDave.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    Dave = False


formedUrlEric = baseUrl + suppliers[1] + "?pickup=" + pickup + "&dropoff=" + dropoff
try:
    requestEric = requests.get(formedUrlEric, timeout=2)
    jsonEric = requestEric.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    Eric = False

formedUrlJeff = baseUrl + suppliers[2] + "?pickup=" + pickup + "&dropoff=" + dropoff
try:
    requestJeff = requests.get(formedUrlJeff, timeout=2)
    jsonJeff = requestJeff.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    Jeff = False

if Dave:
    if "error" in jsonDave:
        Dave = False
    else:
        optionsDave = jsonDave['options']
        for option in optionsDave:
            option['supplier'] = "Dave"
        options = options + optionsDave

if Eric:
    if "error" in jsonEric:
        Eric = False
    else:
        optionsEric = jsonEric['options']
        for option in optionsEric:
            option['supplier'] = "Eric"
        options = options + optionsEric

if Jeff:
    if "error" in jsonJeff:
        Jeff = False
    else:
        optionsJeff = jsonJeff['options']
        for option in optionsJeff:
            option['supplier'] = "Jeff"
        options = options + optionsJeff

pruned = {pruned['car_type']:pruned for pruned in options}.values()

prunedSort = sorted(pruned, reverse=True, key=itemgetter("price"))

for option in prunedSort:
    if (int(cars[option['car_type']]) >= int(passengers)):
        print(option['car_type'] + " - " + str(option['supplier']) + " - " + str(option['price']))