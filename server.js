// server.js
// where your node app starts

// init project
var express = require('express');
var app = express();
const fs = require('fs');
var movieArray = [];
const movieImageFolder = __dirname + '/public/images/movies/';

// http://expressjs.com/en/starter/static-files.html
app.use(express.static('public'));

// http://expressjs.com/en/starter/basic-routing.html
app.get("/", function (request, response) {
  response.sendFile(__dirname + '/views/index.html');
});


fs.readdir(movieImageFolder, function (err, files) {
    files.forEach(function (movie) {
        console.log(movie);
		if (movie.substr(-4) === '.png') {
            console.log(movie.slice(0,-4));
            movieArray.push(movie.slice(0,-4));
        }
    });
});

app.get("/movieList", function (request, response) {
    console.log(movieArray);
	response.send(movieArray);
});

// listen for requests :)
var listener = app.listen(process.env.PORT, function () {
  console.log('Your app is listening on port ' + listener.address().port);
});
