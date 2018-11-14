# import for Class Movie
import media
# import to display class instances on web page
import fresh_tomatoes

# Each inctance of Class Movie defined below
major_league = media.Movie("Major League",
                          "The new owner of the Cleveland Indians puts together a purposely horrible team so they'll lose and she can move the team. But when the plot is uncovered, they start winning just to spite her.",
                          "http://www.gstatic.com/tv/thumb/v22vodart/11561/p11561_v_v8_aa.jpg",
                          "https://www.youtube.com/watch?v=K_ILz9bC-VU")

good_will_hunting = media.Movie("Good Will Hunting",
                                "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
                                "https://m.media-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=z02M3NRtkAA")

la_vita_e_bella = media.Movie("Life Is Beautiful",
                              "When an open-minded Jewish librarian and his son become victims of the Holocaust, he uses a perfect mixture of will, humor, and imagination to protect his son from the dangers around their camp. ",
                              "https://m.media-amazon.com/images/M/MV5BYmJmM2Q4NmMtYThmNC00ZjRlLWEyZmItZTIwOTBlZDQ3NTQ1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_SX670_AL_.jpg",
                              "https://www.youtube.com/watch?v=4MpZyOdx4cs")
                              
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                       "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg",
                                       "https://www.youtube.com/watch?v=6hB3S9bIaco")
                                       

sleepers = media.Movie("Sleepers",
                       "After a prank goes disastrously wrong, a group of boys are sent to a detention center where they are brutalized. Over ten years later, they get their chance for revenge.",
                       "https://m.media-amazon.com/images/M/MV5BMTc4OTUzNzc0MV5BMl5BanBnXkFtZTgwMjE4ODYxMTE@._V1_.jpg",
                       "https://www.youtube.com/watch?v=sVdiN_4gBWk")

the_hustler = media.Movie("The Hustler",
                          "An up-and-coming pool player plays a long-time champion in a single high-stakes match.",
                          "https://m.media-amazon.com/images/M/MV5BNjhjODI2NTItMGE1ZS00NThiLWE1MmYtOWE3YzcyNzY1MTJlXkEyXkFqcGdeQXVyNTc1NTQxODI@._V1_.jpg",
                          "https://www.youtube.com/watch?v=n7aFFqz2bXU")

american_history_x = media.Movie("American History X",
                                 "A former neo-nazi skinhead tries to prevent his younger brother from going down the same wrong path that he did.",
                                 "https://m.media-amazon.com/images/M/MV5BZjA0MTM4MTQtNzY5MC00NzY3LWI1ZTgtYzcxMjkyMzU4MDZiXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_.jpg",
                                 "https://www.youtube.com/watch?v=XfQYHqsiN5g")


# List of Class instances for fresh_tomatoes.py
movies = [major_league, good_will_hunting, sleepers, the_shawshank_redemption, the_hustler, la_vita_e_bella, american_history_x]
fresh_tomatoes.open_movies_page(movies)

# print class documentation to console
print("###classMovie: " + media.Movie.__doc__)