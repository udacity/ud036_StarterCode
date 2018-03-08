m# moviesite

Program in Python that use fresh_tomatoes for generating site that provides posters and
trailers for your favorite movies. If you want to add your favorite movies you have to
put them in entertainment_center like I did(you can see my movies there),in parenthesis 
you have to put title, link to the poster and link to trailer. Then just put your movies 
in brackets at the bottom movies=[yourmovie1, yourmovie2, ....]. When you put all your 
favorite movies there simply save the file, and run entertainment_center. 
It should generate site with your favorite movies. You can find url's of movie data manually 
or use my findPoster&etc if you are more advanced user.

This program is in python. You should download python 2.7.14 from https://www.python.org/downloads/
for running this program. 


For finding movie data I used API https://www.themoviedb.org/documentation/api.
There are comments on how it works in the file called findPoster&etc.
This was my first time with API and Im sure that there are better ways for getting the movie data.
If you want to use this code first you need register on https://www.themoviedb.org and get 
API-KEY from there. And simply past it in findPoster&etc - tmdb.API_KEY = 'your-key-here'.
I found this tmdbsimple wraper on github it hellped me a lot to understand how can i use API.
Special effect on movie site word found on http://freefrontend.com/css-text-effects/.


