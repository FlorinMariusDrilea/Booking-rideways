# libraries
import sys
import requests

# get the api
url = "https://techtest.rideways.com/"
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

# functions
def get_item(*items):
    if len(items) == 1:
        item = items[0]
        def o(obj):
            return obj[item]
    else:
        def o(obj):
            return tuple(obj[item] for item in items)
    return o

# error if not all parameteres are inserted
if (len(sys.argv)) < 3:
	print("Error")
	sys.exit(0)
else:
	pickup = sys.argv[1]
	dropoff = sys.argv[2]
	passengers = sys.argv[3]
	
# print the results available
print("Pickup: " + pickup)
print("Dropoff: " + dropoff)
print("Passengers: " + passengers)

# searching through all the possible cars from all the apis
# and keep in mind what is correct in the given order
urlEric = url + suppliers[1] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestEric = requests.get(urlEric, timeout=1)
    jsonEric = requestEric.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
	print("Skipping Eric - ")
	print(e)
	Eric = False
	
urlJeff = url + suppliers[2] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestJeff = requests.get(urlJeff, timeout=1)
    jsonJeff = requestJeff.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
	print("Skipping supplier Jeff - ")
	print(e)
	Jeff = False

urlDave = url + suppliers[0] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestDave = requests.get(urlDave, timeout=1)
    jsonDave = requestDave.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
	print("Skipping Dave - ")
	print(e)
	Dave = False

# get suppliers or get errors for every apis

if Eric:
    if "error" in jsonEric:
        print("Eric api error : " + jsonEric['error'])
        Eric = False
    else:
        optionEric = jsonEric['options']
        for option in optionEric:
            option['supplier'] = "Eric"
        options = options + optionEric

if Jeff:
    if "error" in jsonJeff:
        print("Jeff api error : " + jsonJeff['error'])
        Jeff = False
    else:
        optionJeff = jsonJeff['options']
        for option in optionJeff:
            option['supplier'] = "Jeff"
        options = options + optionJeff

if Dave:
    if "error" in jsonDave:
        print("Dave api error : " + jsonDave['error'])
        Dave = False
    else:
        optionDave = jsonDave['options']
        for option in optionDave:
            option['supplier'] = "Dave"
        options = options + optionDave

# go through all the options that were selected above and arrange them in ascending order
branchSorted = sorted({branch['car_type']:branch for branch in options}.values(), reverse=True, key=get_item("price"))

# print all options possible in ascending order
for option in branchSorted:
    if (int(cars[option['car_type']]) >= int(passengers)):
        print(option['car_type'] + " - " + str(option['supplier']) + " - " + str(option['price']))