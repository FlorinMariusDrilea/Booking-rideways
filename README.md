# Booking-rideways

## Setup

For the setup I used python with no other dependencies + in the second part I used node.js with the help of npm installation.

## Part 1 

The file part1.py contains all is needed to make exercise 1 work.

It can be run using the command prompt console and with the command : "python part1.py <pickup> <dropoff> <passengers>"

Sometimes at the first part it could show some internal errors for the apis.

## Part 2

For the second part I used node.js.
You need to install it to use the packages used for this part.

First : "npm install"

Second : "npm install python-shell" - an interpeter to run the code from the first part on the server

Third : "npm install express" - it is a web framework for node 

The server is running with the command prompt of node.js with the comand "node index.js".
It will open a local server with the port of 9800.

To make it run on the server you need to put the parameters into the link like this.
"http://localhost:9800/?pickup=57.231020,-0.263295&dropoff=2.710632,-2.127533&passengers=2"
