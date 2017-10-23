# Project: Movie Trailer Website - Savneet Singh

README for a Movie Trailer website.
This Website will display the movie name, box art of the movie and when you 
click on the movie will show the trailer.

## Required Libraries and Dependencies

- Python
 - Install **Python 2.7.14** at https://www.python.org/downloads/ 
 
## How to Run the Project

- Navigate to the folder you downloaded containing the Python files
- Open the `project_entertainment_centre.py` with IDLE and run (F5 on Mac) 
- A webpage should open displaying the movies

## Miscellaneous

- `project_media.py` contains the **class** `Movie()` that stores your favourite movies, 
including movie title, box art URL and a YouTube link to the movie trailer.
 `'project_entertainment_centre.py` is a Python class that creates *multiple instances* 
 to represent your favourite movies  
- `fresh_tomatoes.py` contains the `open_movies_page()` function that will take in your 
list of movies and generate an HTML file including this content, producing a website to
 showcase your favorite movies.
- Ensure `fresh_tomatoes.py` is in the same directory as your `project_media.py` and
 `project_entertainment_centre.py` files
- In `fresh_tomatoes.py`, the `open_movies_page()` and `create_movie_tiles_content()`
 functions need the variable names changing to match the names in `project_media.py` 

## Extra Credit - GitHub

Udacity provides a starter code repository that contains a Python module called
 `fresh_tomatoes.py`

### Follow the steps below to fork this repository to create your own copy in GitHub:
- Create a GitHub account
- Fork this [repository](https://github.com/udacity/ud036_StarterCode) and clone:
 - At the top of this page click on the `Fork` 
 - Click the `Clone or Download` button and copy the URL from the Clone with HTTPS section
 - Open Terminal
 - Change the current working directory to the location where you want the cloned 
 directory to be made
 - Type `git clone` and then paste the URL from the above step
 - Press **Enter**

### To make changes, create a branch and then commit the changes:
- In Terminal do `git checkout -b branchName`
- Make the changes to the files
- `git commit -m "Message about commit" -a` to commit the changes
- Push the changes to **origin** by typing `git push origin branchName`

### Create a **Pull Request** in GitHub:
- In your forked repository *username/ud036_StarterCode* click on **New Pull Request** 
- Ensure the **base fork** and the **head forl** are **your** forked repository
- Compare **master** with **branchName**
- Commit any messages/comments if needed
- Click **Merge Pull Request**
- Click **Confirm Merge**
- Your screen will then say **Pull request successfully merged and closed**mark 

### Get the changes in your local remote repository:
- Change to the **master** branch by typing `git checkout master`
- In the Terminal, do `git fetch` and then `git rebase`


