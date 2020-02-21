// variables used during the app
var { python-shell } = require('python-shell');
var express = require("express");
var app = express();
var port = 9800;

// create the server on specified port
app.listen(port, () => {
    console.log("Server on port", port);
});

// transform the result into json form
function toJSON(result) {
    var splitting = result.split('-')
    var trimming = splitting.map(result => result.trim())

    return {
        car_type: trimming[0],
        supplier: trimming[1],
        price: parseInt(trimming[2])
    }
}

// verify the parameters that are entered
function verify(pickup, dropoff, passengers) {
    var error = [];
    if (dropoff == null){
        error.push("dropoff cannot be empty")
    }
	if (pickup == null){
        error.push("pickup cannot be empty")
    }
    if (passengers == null){
        error.push("passengers cannot be empty")
    } else if (isNaN(passengers)) {
        error.push("passengers value must be a number")
    }
    return error;
}

// get response from the server
app.get("/", (req, res) => {
    var { pickup, dropoff, passengers } = req.query;
	var goodRes = verify(pickup,dropoff,passengers)
	var options = {
        args: [pickup, dropoff, passengers]
    };
    
	if (goodRes.length >= 1){
        return res.json({ goodRes })
    }

	// send parameters from the server to the first part of the program
    python-shell.run('part2 - working process.py', options, function(error, result) {
        
		if (error) {
            console.log(error)
        }

        result = result.map(toJSON);
        if (result.length >= 1){
            return res.json({ result });
        } else {
            return res.json({Empty:"Nothing found. Sorry!"});
        }
    });
});
