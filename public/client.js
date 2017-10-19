// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
$(document).on('click', '.movie-tile', function (event) {
    var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
    var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
      'id': 'trailer-video',
      'type': 'text-html',
      'src': sourceUrl,
      'frameborder': 0
    }));
});
// Animate in the movies when the page loads
$(document).ready(function () {
  $('.movie-tile').hide().first().show("fast", function showNext() {
    $(this).next("div").show("fast", showNext);
  });
});

        
const imgDIR = '/images/movies/';

console.log('IMPORTANT: Please run the command "npm install" and ' +
    'then "heroku local web" in the source directory');

// GET request to get movie items from the server and call movieListController function
httpGetAsync('/movieList', movieListController);


/*
 * MVC design pattern
 * This design pattern makes sure there is no direct connection between
 * model(app data) and the view (rendered content/ DOM)
 * This allows the ease of changing model/view without affecting the other
 */

/***********************************************************************************************************************
 *              MODEL
 **********************************************************************************************************************/

var movies = [];

/**
 * Push another element into movies Array
 * @param name      - stores name of the movie
 * @param imgURL  - stores imgURL of the movie
 */
function addMovie(name, imgURL) {
    movies[name] = imgURL;
}

/**
 * Convert array (inside a string )to actual JavaScript array
 * Reason: response from back-end is in the form of string.
 *          Evem an array returned from back-end is inside a string.
 *          TODO: Look into how to recieve an actual array
 * @param str - contains the array in string form
 */
function stringToArray(str) {
    return JSON.parse("[" + str + "]");
}

/**
 * Sets movie list information in movies
 * @param movieList - Array of movies recieved from back-end in string form
 * @returns {Array} - List of movie in JavaScript Array form
 */
function initializeMovieList(movieList) {
    var temp = stringToArray(movieList);

    temp[0].forEach(function (movie) {
        var mName = movie;
        var mImgURL = "../images/" + movie + ".png";

        addMovie(mName, mImgURL);
    });
    return movies;
}

/***********************************************************************************************************************
 *              CONTROLLER
 **********************************************************************************************************************/

/**
 * Asynchronous GET request
 * @param theUrl    - url of the request
 * @param callback  - callback function for the request
 */
function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
            callback(xmlHttp.response);
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

/**
 * Controller function for movie list
 * Callback function that recieves movie list from back-end
 * @param navMenuList
 */
function movieListController(movieList) {
    initializeMovieList(movieList); // model function
    renderMovieList();                // view function
}

/***********************************************************************************************************************
 *              VIEW
 **********************************************************************************************************************/

/**
 * Helper function to create DOM elements
 * @param   {string}  tagName       - HTML tag name (e.g. div, li, span, etc)
 * @param   {JSON}    attrArray     - list of attributes for the new DOM element
 * @returns {Element} newNode       - the new DOM element created
 */
function createNewNode(tagName, attrArray) {
    var newNode = document.createElement(tagName);
    var keys = Object.keys(attrArray);

    // iterates through all atrributes to be given to the new DOM element
    for (var i = 0; i < keys.length; i++) {
        switch (keys[i]) {
            case 'class':       newNode.className = attrArray[keys[i]]; break;
            case 'id':          newNode.id = attrArray[keys[i]];        break;
            case 'src':         newNode.src = attrArray[keys[i]];       break;
            case 'innerHTML':   newNode.innerHTML = attrArray[keys[i]]; break;
            case 'data-trailer-youtube-id':
                var att = document.createAttribute("data-trailer-youtube-id");
                att.value = attrArray[keys[i]];
                newNode.setAttributeNode(att);
                break;
            case 'data-toggle':
                var att = document.createAttribute("data-toggle");
                att.value = attrArray[keys[i]];
                newNode.setAttributeNode(att);
                break;
            case 'data-target':
                var att = document.createAttribute("data-target");
                att.value = attrArray[keys[i]];
                newNode.setAttributeNode(att);
                break;
            case 'target':
                var att = document.createAttribute("target");
                att.value = attrArray[keys[i]];
                newNode.setAttributeNode(att);
                break;
            default:            console.log('weird: ' + keys[i]);
        }
    }

    
    return newNode;
}

/*
 * Structure for a movie div:
 *
 *   movie div
 *       - image
 *       - name
 */

/**
 * Renders the movies
 */
function renderMovieList() {

    for (var movie in movies) {
        var mDiv        = createNewNode('div',{'class':'col-md-6 col-lg-4 movie-tile text-center', 'id':movie, 'data-trailer-youtube-id':'https://www.youtube.com/watch?v=Ned-VBaRriI', 'data-toggle':"modal", 'data-target':"#trailer"});
        var mImage      = createNewNode('img',{'class':'img-rounded','src':imgDIR+movie+'.png'});
        var mH2         = createNewNode('h2',{'innerHTML':movie});

        mDiv.appendChild(mImage);
        mDiv.appendChild(mH2);

        var movieDisplayArea = document.getElementById('movieList');
        movieDisplayArea.appendChild(mDiv);
    }
}