#!/usr/bin/env python

#importing necessary modules and packages
import base_movie_trailer_web
from media import Movie
    
#interstellar is an object of class Movie and arguments passed are movie name, 
#movie story line, poster image and youtube trailer link
interstellar = Movie("Interstellar", "Professor Brand (Michael Caine), \
                        a brilliant NASA physicist, is working on plans to save \
                        mankind by transporting Earth's population to a \
                        new home via a wormhole.", \
                        "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", \
                        "https://www.youtube.com/watch?v=Lm8p5rlrSkY")

#bajirao_mastani is an object of class Movie and arguments passed are movie name, 
#movie story line, poster image and youtube trailer link
bajirao_mastani = Movie("Bajirao Mastani", "The heroic Peshwa Bajirao, \
                             married to Kashibai, falls in love with Mastani, \
                             a warrior princess in distress. They struggle to make \
                             their love triumph amid opposition from his conservative family.", \
                             "https://upload.wikimedia.org/wikipedia/en/5/52/Bajirao_Mastani_Poster_2.jpg",\
                             "https://www.youtube.com/watch?v=eHOc-4D7MjY")

#titanic is an object of class Movie and arguments passed are movie name,
#movie story line, poster image and youtube trailer link
titanic = Movie("Titanic", "'Titanic' is an epic, action-packed romance set \
                    against the ill-fated maiden voyage of the R.M.S. Titanic; \
                    the pride and joy of the White Star Line and, at the time, \
                    the largest moving object ever built. She was the most luxurious \
                    liner of her era -- the 'ship of dreams' -- which ultimately \
                    carried over 1,500 people to their death in the ice cold waters \
                    of the North Atlantic in the early hours of April 15, 1912.", \
                    "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",\
                    "https://www.youtube.com/watch?v=2e-eXJ6HgkQ")

#inception is an object of class Movie and arguments passed are movie name, 
#movie story line, poster image and youtube trailer link
inception = Movie("Inception", "Dom Cobb (Leonardo DiCaprio) is a thief with the rare \
                    ability to enter people's dreams and steal their secrets from their \
                    subconscious. His skill has made him a hot commodity in the world of \
                    corporate espionage but has also cost him everything he loves. \
                    Cobb gets a chance at redemption when he is offered a seemingly \
                    impossible task: Plant an idea in someone's mind. \
                    If he succeeds, it will be the perfect crime, but a dangerous \
                    enemy anticipates Cobb's every move.", \
                    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",\
                    "https://www.youtube.com/watch?v=8hP9D6kZseM")

#orphan is an object of class Movie and arguments passed are movie name, 
#movie story line, poster image and youtube trailer link
orphan = Movie("Orphan", "Devastated by the loss of their unborn baby, Kate (Vera Farmiga) \
                    and John (Peter Sarsgaard) decide to adopt a child. \
                    At the orphanage, both feel drawn to a little girl (Isabelle Fuhrman) \
                    named Esther, and soon the couple take their new daughter home. \
                    But when a dangerous series of events unfolds, Kate begins to suspect \
                    that there is something evil lurking behind the child's angelic exterior.",\
                    "https://upload.wikimedia.org/wikipedia/en/thumb/4/47/Orphanposter.jpg/220px-Orphanposter.jpg",\
                    "https://www.youtube.com/watch?v=WgxVIB2WuHU")

#p_s_i_love_u is an object of class Movie and arguments passed are movie name, 
#movie story line, poster image and youtube trailer link
p_s_i_love_u = Movie("P.S. I love U", "When Gerry (Gerard Butler), the husband of \
                    Holly Kennedy (Hilary Swank),dies from an illness, she loses the \
                    love of her life. Knowing how hard Holly will take his death, \
                    Gerry plans ahead. Beginning on her 30th birthday, she receives \
                    the first in a series of letters written by him, designed to ease \
                    her grief and encourage her to move forward to a new life.", \
                    "https://upload.wikimedia.org/wikipedia/en/7/7f/PS_I_Love_You_%28film%29.jpg",\
                    "https://www.youtube.com/watch?v=CZzW6_hR068")

def main():
    """Main function of the application"""
    #movies are list of instances which is created from class Movie
    movies = [interstellar, bajirao_mastani, titanic, inception, orphan, p_s_i_love_u]

    #open_movies_page is a function for displaying content in the web browser
    base_movie_trailer_web.open_movies_page(movies)

#Execution start from here
if __name__=='__main__':
    main()
