# Movie Trailer Website
Create a simple website that showcases all of your favorite movies along with a movie trailer.

## What's Inside

### Fresh Tomatoes
The fresh_tomatoes.py file takes in a list of your favorite movies and turns them into an HTML file, or a website. Take a look at the `def open_movies_page(movies)` at the bottom in particular as this function will really do the magic. You don't have to touch anything inside this file. This is just to show you what's under the hood.

### The Movie Blueprint
The media.py is a class generator of instances of your favorite movies. The `class Movie()` takes four parameters:
`forrest_gump = media.Movie(title, storyline, poster-image, trailer-youtube)`
Have these 4 information for each of your favorite movie ready to go. Again, you don't have to touch this file either, unless you want to change the parameters.

### Entertainment Center
The entertainment_center.py is the python file that will store all of your favorite movies. You can include as many movies as you want. This file will ultimately run your application.


## How to Run It
1. Download [Python](https://www.python.org/the) and the [Repo](https://github.com/robin-yoo/ud036_StarterCode) onto your desktop. There should be 3 different python files:
  - fresh_tomatoes.py
  - media.py
  - entertainment_center.py

2. Open the entertainment_center.py file. This will ultimately run the application.
3. Create a new instance of each of your favorite movie (title, storyline, poster image url, youtube trailer url). To create a new movie, just follow the format already done for you.
```
forrest_gump = media.Movie(
    "Forrest Gump",
    "While not intelligent, Forrest Gump has accidentally been present"
    " at many historic moments, but his true love, Jenny Curran, eludes him.",
    "https://goo.gl/xHzL7o",
    "https://www.youtube.com/watch?v=bLvqoHBptjg")
```
4. Once you have all your movies, store them inside the movie array just like the one done for you in the bottom of the file.
```
movies = [forrest_gump, star_wars,
blade_runner]
```
5. Save the file and run the application to see your website come to life. 🎉


## Special Thanks
Thank you to Udacity for teaching this program and providing fresh_tomatoes.py file to magically create our movie trailer website.

## License
MIT License

Copyright (c) 2017 Robin Yoo

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
