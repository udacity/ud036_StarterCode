# Project: Movie Trailer Website - Savneet Singh

README for a Movie Trailer website.
This Website will display the movie name, box art of the movie and when you 
click on the movie will show the trailer.

## Required Libraries and Dependencies

- Python
  - Install **Python 2.7.14** at https://www.python.org/downloads/ 
 
## How to Run the Project

- Navigate to the folder you downloaded containing the Python files
- Open the `project_entertainment_centre.py` with IDLE and run the module (F5 key on Mac) 
- A webpage should open displaying the movies

## Code Explained

- `project_media.py` contains the **class** `Movie()` that stores your favourite movies, 
including movie title, box art URL and a YouTube link to the movie trailer.

- `project_entertainment_centre.py` is a Python class that creates *multiple instances* 
 to represent your favourite movies  
 
- Udacity provides a starter code repository that contains a Python module called
 `fresh_tomatoes.py`
 
- `fresh_tomatoes.py` contains the `open_movies_page()` function that will take in your 
list of movies and generate an HTML file including this content, producing a website to
 showcase your favorite movies.
 
 ## Miscellaneous 
 
- Ensure `fresh_tomatoes.py` is in the **same directory** as your `project_media.py` and
 `project_entertainment_centre.py` files
 
- In `fresh_tomatoes.py`, the `open_movies_page()` and `create_movie_tiles_content()`
 functions need the *variable names changing* to match the names in `project_media.py`. 
 In this case, `movie.trailer_youtube_url` was changed to `movie.youtube_trailer_url` to match 
 the *instance variable* in class `Movie()`





