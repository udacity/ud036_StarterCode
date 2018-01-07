# ---------------------------------------------------------------------#
#  Udacity Course: Full Stack Web Developer
#  Proj #1: Movie Website
#  Purpose: Create CSV format file with movie information that is
#            suitable for use by entertainment_center. Future
#            enhancement is to make this real db on server side,
#            and allow website user to pick some of the movies.
#  File:    ec_create_csv
# 
# ---------------------------------------------------------------------
#  PPC | 01/06/2018 | Original code.
# ---------------------------------------------------------------------
# Std lib code for handling CSV files. See https://docs.python.org/2/library/csv.html 
import csv

def create_movie_csv():
    with open('ec_movie_list.csv', 'wb') as csvfile:
        moviewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)
        # Use standard header on these files -- needed by ec_reader_csv
        moviewriter.writerow(['Movie Title',
                              'Storyline',
                              'Movie Poster Graphic', 
                              'YouTube Movie Trailer'])
        # Actual Movie Information
        moviewriter.writerow(['Toy Story',
                              'A story of a boy and his toys that come to life.',
                              'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg', 
                              'https://www.youtube.com/watch?v=VwyZH85NQC4'])
        moviewriter.writerow(['Avatar',
                              'A marine on an alien planet',
                              'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg', 
                              'https://www.youtube.com/watch?v=5PSNL1qE6VY'])
        moviewriter.writerow(['Ender\'s Game',
                              'Future defense of Earth depends on brilliant young commander.',
                              'https://upload.wikimedia.org/wikipedia/en/8/8c/Ender%27s_Game_poster.jpg', 
                              'https://www.youtube.com/watch?v=vP0cUBi4hwE'])
        moviewriter.writerow(['School of Rock',
                              'Using rock music to learn.',
                              'https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg', 
                              'https://www.youtube.com/watch?v=3PsUJFEBC74'])
        moviewriter.writerow(['Avengers',
                              'Alien invasion stopped by team of superheros.',
                              'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg', 
                              'https://www.youtube.com/watch?v=E-84FIZ8-Ow'])
        moviewriter.writerow(['Jesus of Nazareth',
                              'The greatest story ever told.',
                              'https://upload.wikimedia.org/wikipedia/en/c/c0/Jesus_of_nazareth.jpg', 
                              'https://pureflix.com/videos/253280294866/play'])

# create_movie_csv()


