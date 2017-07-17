# Movie Trailer Center
This project is used to create a website displaying all of your favoite movies. It allows the user to click a movie poster displayed on the site and plays the movie's trailer.

## Geting Started
The instructions given below will help you setup The Movie Trailer project on your local machine. All requirements including software installations needed to run this project will be mentioned in this guide.

### Prerequisites
To run this program, you'll first need to install python. Visit https://www.python.org/ and download the latest version of python.

Once installation is done, type the following command in a command line window: "python". You should see an output like the one below

```
Python 2.7.13 (v2.7.13:, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

### Installing
To get the project's files, you can clone the repo [here](https://github.com/nanatech/Movie_TrailerCenter/tree/movie_branch) or you can download the zip file. 

Once you have the project setup you should have a directory that looks like the following:

>/pics
</br>README.md
</br>entertainment_center.py
</br>fresh_tomatoes.html
</br>fresh_tomatoes.py
</br>fresh_tomatoes.pyc
</br>media.py
</br>media.pyc

## Modifying Files
By default the project is setup to display my favorite movies. To display your favorite movies instead modify the <b>"entertainment_center.py"</b>file in your Python IDLE editor.
> You will notice that this file stores an array of the movies specified at the beginning of the file. This array is then used by the open_movies_page() method. This method is called from the fresh_tomatoes module, which is the file that renders a html page to display all of your favorite movies.

If your are familiar with HTML and would like to chnage the style of the HTML page rendered from the fresh_tomatoes.py module, feel free to modify this file as well.

## Running the Program
Now that you have added your favorite movies in the <b>entertainment_center.py</b> file, go ahead and run the program by clicking <b>Run --> Run Module</b> or by clicking F5 on the keyboard in your python IDLE.

## Acknowledgments
Thanks to Udacity Nanodegree program for providing a starter code repository that contains the main code to generate the movie site. Repository found [here](https://github.com/adarsh0806/ud036_StarterCode)