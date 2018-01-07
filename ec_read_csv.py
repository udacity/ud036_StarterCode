# ---------------------------------------------------------------------#
#  Udacity Course: Full Stack Web Developer
#  Proj #1: Movie Website
#  Purpose: Read CSV format file containing movie information that is
#            suitable for use by entertainment_center. Future
#            enhancement is to make this real db on server side,
#            and allow website user to pick some of the movies.
#            -- what happens if text file more than 6 movies?
#            -- if file not exist, catch in calling code 
#  File:    ec_read_csv
# 
# ---------------------------------------------------------------------
#  PPC | 01/06/2018 | Original code.
# ---------------------------------------------------------------------
# Std lib code for handling CSV files. See https://docs.python.org/2/library/csv.html 
import csv

# Movie Title,
# Movie Storyline,
# Movie Poster Graphic,
# YouTube Movie Trailer
# a_col = 4
# a_row = 6
# my_movie_list = [[" " for x in range(a_col)] for y in range(a_row)]
my_movie_list = []

def read_movie_csv():
    with open('ec_movie_list.csv', 'rb') as csvfile:
        moviereader = csv.reader(csvfile, delimiter=',', quotechar='"')

        # Advance to line 1 = header
        csv_header = moviereader.next()

        # Can now add more columns to movie "db" w/o changing code
        mov_Title_Index = csv_header.index("Movie Title")
        mov_SL_Index = csv_header.index("Storyline")
        mov_Graphic_Index = csv_header.index("Movie Poster Graphic")
        mov_Trailer_Index = csv_header.index("YouTube Movie Trailer")

        # Now we know header column numbers, so go read actual movie records
        for movie_row in moviereader:
            # Assumes each row is identically formatted (data in same column) 
            one_Title = movie_row[mov_Title_Index]
            one_SL = movie_row[mov_SL_Index]
            one_Graphic = movie_row[mov_Graphic_Index]
            one_Trailer = movie_row[mov_Trailer_Index]

            # Fill list with this one row of data
            my_movie_list.append([one_Title, one_SL, one_Graphic, one_Trailer])

        # print(my_movie_list[0][0]) 
        return my_movie_list

# read_movie_csv()
# print(find_movie_csv("Avengers"))
# print(my_movie_list[4])

