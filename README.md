# Movie Trailer website

This is a project to let user to create a Movie Trailer website.

## Guidelines

Install [Python](https://www.python.org/)(if you don't have one)

Download or clone this repository 

Edit **entertainment_center.py** with the editor you like：
* Create your Movie object like the following example:

```
toy_story = media.Movie("Toy Story",                                              // title
			"A story of a boy and his toys that come to life",        // story line
			"https://upload.wikimedia.com/200px-ToyStory4poster.jpg", // poster image URL
			"https://youtu.be/Bj4gS1JQzjk" //trailer URL )            // trailer URL
```
* Store those Movie object in a list like the following example:
```
movies = [toy_story, avatar, warcraft]
```
* Call open_movies_page() function to take in your list of movies and generate an HTML file including this content, and produce website to showcase your favorite movies.
```
fresh_tomatoes.open_movies_page(movies)
```
* Build entertainment_center.py with python

## License

The content of this repository is licensed under a [MIT License](https://choosealicense.com/licenses/mit/)
