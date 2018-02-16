# ud036_StarterCode
Source code for a Movie Trailer website.

Purpose of this code is to create a webpage that will allow you to click on a picture and play youtube videos.  

There are 3 primary py files in this grouping:
    media2.py = class formating module for the movies content
    entertainment_center2.py = Execution and content module: listing of the movies, details about the movies, links and corresponding functions
    fresh_tomatoes.py = webpage module.  script that will launch the website with mark up language.  Uses entertainment_center2 as the content module.


#media2.py
    There is 1 parent class and 1 child class in this file.  Intent is to make it modular for it can grow over time.
    There are a total of 6 entries that are standardized across the group
        2 entries are inhereted from the 'Videos' object
        4 are unique to the 'Movies' object
    Youtube is the source of choice when opening a trailer.  I tried secondary sources but the play back would fail often.
    wikimedia is the source of choice for images.  I attempted several other sites and file formats, but hit many errors.


# Areas for improvment.
- Figure out why wikimedia is the only functioning source for images
- Figure out why youtube is the only functioning source for playing movies.

#enterainment_center
- import media2 for class formatting
- import fresh_tomatoes for launching the webpage

- list out your favorite movies and follow the formating from media2 file.
- 'movies' is a variable for an array of the favorite movies
- fresh_tomatoes.open_movies_page is the function launging the website.

# Areas for improvement.
- this is fine for a small list, but a larger list should be in our sourced from a more comprehensive database.

# fresh_tomatoes
Provided code from Udacity to launch the website.

I made changes the to header by adding a little spanish lingo
Also added the details from entertainment_center.py to be included in the web page.  This includes the inhereted instance variables which shows the code is working throughout the environment


Finally I wrote this README cause, you know...I'm having fun with this and want to practice how I plan to play:)
