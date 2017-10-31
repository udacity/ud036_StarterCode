import sys
from fresh_tomatoes import open_movies_page
from entertainment_center import Entertainment


def main(args=None):
    """The movie trailer website's main routine and code executes from here"""
    if args is None:
        args = sys.argv[1:]

    # Project script execution statements starts from below.
    entertainment = Entertainment()
    # calls open_movies_page with a movie list as input from entertainment center, in fresh_tomatoes and opens a html file in browser
    open_movies_page(entertainment.get_movies_list())    

if __name__ == "__main__":
    main()