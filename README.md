# Movie Trailer Website
Create a simple website that showcases all of your favorite movies along with a movie trailer.

## How to
Download the repo onto your desktop. There should be 3 different python files:
- fresh_tomatoes.py
- media.py
- entertainment_center.py

### Fresh Tomatoes
The fresh_tomatoes.py file takes in a list of your favorite movies and turns them into an HTML file, or a website. Take a look at the `def open_movies_page(movies)` at the bottom in particular as this function will really do the magic. You don't have to touch anything inside this file. This is just to show you what's under the hood.

### The Movie Blueprint
The media.py is a class generator of instances of your favorite movies. The `class Movie()` takes four parameters:
`forrest_gump = media.Movie(title, storyline, poster-image, trailer-youtube)`
Have these 4 information for each of your favorite movie ready to go. Again, you don't have to touch this file either, unless you want to change the parameters.

### Entertainment Center
The entertainment_center.py is the python file that will store all of your favorite movies. You can include as many movies as you want. To create a new movie, just follow the format already done for you.
```
forrest_gump = media.Movie("Forrest Gump",
                           "While not intelligent, Forrest Gump has accidentally been present"
                           " at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")
```
Once you have all your movies, store them inside the movie array just like the one done for you in the bottom.
```
movies = [forrest_gump, star_wars, blade_runner]
```
The next line of code,
```
fresh_tomatoes.open_movies_page(movies)
```
will take in your list of movies and generate an HTML page of your movie trailer website. Run this file and watch your website come to life! :+1:

## Special Thanks
Thank you to Udacity for teaching this program and providing fresh_tomatoes.py file to magically create our movie trailer website.

## License
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.







