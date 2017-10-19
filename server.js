// server.js
// where your node app starts

// init project
var express = require('express');
var app = express();
const fs = require('fs');
var movieArray = [];
const movieImageFolder = __dirname + '/images/movies/';

// we've started you off with Express, 
// but feel free to use whatever libs or frameworks you'd like through `package.json`.

// http://expressjs.com/en/starter/static-files.html
app.use(express.static('public'));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});

app.get("/dreams", function (request, response) {
  response.send(dreams);
});

// could also use the POST body instead of query string: http://expressjs.com/en/api.html#req.body
app.post("/dreams", function (request, response) {
  dreams.push(request.query.dream);
  response.sendStatus(200);
});

fs.readdir(movieImageFolder, function (err, files) {
    files.forEach(function (movie) {
        console.log(movie);
		if (movie.substr(-4) === '.png') {
            console.log(movie.slice(0,-4));
            movieArray.push(movie.slice(0,-4));
        }

        //console.log(arr);
    });
});

app.get("/movieList", function (request, response) {
    console.log(movieArray);
	response.send(movieArray);
});

// Simple in-memory store for now
var dreams = [
  "Find and count some sheep",
  "Climb a really tall mountain",
  "Wash the dishes"
];

// listen for requests :)
var listener = app.listen(process.env.PORT, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
