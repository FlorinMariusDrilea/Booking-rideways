import sys
import requests
from operator import itemgetter

baseUrl = "https://techtest.rideways.com/"
suppliers = ["dave", "eric", "hef"]

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
	
print("Pickup: " + pickup)
print("Dropoff: " + dropoff)
print("Passengers: " + passengers)
	
urlEric = baseUrl + suppliers[1] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestEric = requests.get(urlEric, timeout=2)
    jsonEric = requestEric.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    print("Skipping Eric - ")
    useEric = False
	print(e)
	
urlJeff = baseUrl + suppliers[2] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestJeff = requests.get(urlJeff, timeout=2)
    jsonJeff = requestJeff.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    print("Skipping supplier Jeff - ")
	useJeff = False
    print(e)

urlDave = baseUrl + suppliers[0] + "?pickup=" + pickup + "&dropoff=" + dropoff

try:
    requestDave = requests.get(urlDave, timeout=2)
    jsonDave = requestDave.json()
except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout) as e:
    print("Skipping Dave - ")
    Dave = False
	print(e)

if useEric:
    if "Error" in jsonEric:
        print("Eric api error : " + jsonEric['error'])
        useEric = False
    else:
        optionEric = jsonEric['options']
        for option in optionEric:
            option['supplier'] = "Eric"
        options = options + optionEric

if useJeff:
    if "Error" in jsonJeff:
        print("Jeff api error : " + jsonJeff['error'])
        useJeff = False
    else:
        optionJeff = jsonJeff['options']
        for option in optionJeff:
            option['supplier'] = "Jeff"
        options = options + optionJeff

if Dave:
    if "Error" in jsonDave:
        print("Dave api error : " + jsonDave['error'])
        Dave = False
    else:
        optionDave = jsonDave['options']
        for option in optionDave:
            option['supplier'] = "Dave"
        options = options + optionDave


branch = {branch['car_type']:branch for branch in options}.values()

branchSorted = sorted(branch, reverse=True, key=itemgetter("price"))

for option in branchSorted:
    if (int(cars[option['car_type']]) >= int(passengers)):
        print(option['car_type'] + " - " + str(option['supplier']) + " - " + str(option['price']))
