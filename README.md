# ud036_StarterCode
Source code for a Movie Trailer website.

## What's needed for this code to work
All that's really needed is for you to have an IDLE (preferably `Python`) to run the code. You would also need to have a browser for the code to open in. I use `Google Chrome` as my webbrowser.

## How the code work
In the project, there are several files that work with each other. There's a file called `media.py` which holds the `class Movie()`. The class movie was created so that a user can call it and create instances of their favorite movies. When the user create those instances, the `__init__` function inside the `class Movie()` gets initialize. The `__init__` function takes in the parameters of self, movie_title, movie_storyline, poster_image,  and trailer_youtube. These parameters set the poster image and youtube trailer for your website. There's another function inside the class Movie() that's called an `instance method`. This `instance method` is what opens the webbrowser and go to the youtube trailer on the web. You can create all of your movie instances in the same flie as `media.py` but it's good practice to keep your classes separated. The `entertainment_center.py` file is were all of the movie instances are created. The final file needed to make this code work is a file called `fresh_tomatoes.py`. This file contains the contents of the `html5`, `css`, `JavaScript`, `jQuery`, and `python` code for the functionality and design of the website. This file has a function called `open_movies_page()` which takes in a parameter called `movies`. The `movies` parameter is just an array you'll have to create of all the movie instances you created earlier. Once you create the `movies` array and call it inside of `open_movies_page()` you should be able to create a website with all of your favorite movies.

## Issues
You may run into some issues if you running an old version of python or a newer version. If that's the case make sure you check the documentation to make sure you changes accordingly.
