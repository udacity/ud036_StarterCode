import media
import fresh_tomatoes

"""The entertainment center module is used to initalize instance of the Movie class"""


toy_story = media.Movie("Toy Story",
                        "A story of a boy and hist toys that come to life",
                        "pics//toystory.jpeg","https://youtu.be/KYz2wyBy3kc")

home_alone = media.Movie("Home Alone",
           "An eight-year-old is accidentally left home alone by his family",
           "pics//homeAlone.jpg", "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

princess_frog = media.Movie("Princess & The Frog",
                            "A story of a disnet princess and a prince frog",
                            "pics//PAF.jpg", "https://www.youtube.com/watch?v=uQBy6jqbmlU")
it = media.Movie("IT", "Stephen Kings horror Classic",
                            "pics//It.JPG", "https://www.youtube.com/watch?v=FnCdOQsX5kc")
think_like_a_man = media.Movie("Think Like A Man",
                            "Based on Steve Harvey's best selling book 'Think Like A Man' ",
                            "pics//thinkLAM.jpg", "https://www.youtube.com/watch?v=F7VmU8aHAtw")
scream = media.Movie("Scream","A horror classic.","pics//scream.jpg",
                     "https://www.youtube.com/watch?v=AWm_mkbdpCA")

#Create an array of the movie objects created 
movies = [toy_story, home_alone, princess_frog, it, think_like_a_man, scream]

# This method passes the movie array as an argument to the
# open_movies_page() method. This method is called from the
# fresh_tomatoes module which which will create a HTML file
# that will display all movies listed in the movie array
fresh_tomatoes.open_movies_page(movies)

