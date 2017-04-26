import media
import fresh_tomatoes

elite_squad = media.Movie("Elite Squad", "Elite Squad in Rio de Janeiro fighting a drug lord",
                          "https://images-na.ssl-images-amazon.com/images/M"
                          "/MV5BMTI1Mzc5NjI4Nl5BMl5BanBnXkFtZTcwNzYyMTQ5MQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=cb-rUfBTQ1g")

city_of_god = media.Movie("City of God", "Two boys growing up in a violent neighborhood of Rio de Janeiro take "
                                         "different paths: one becomes a photographer, the other a drug dealer.",
                          "https://images-na.ssl-images-amazon.com/images/M"
                          "/MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3._V1_.jpg",
                          "https://www.youtube.com/watch?v=yJdW1TevoyA")

the_matrix = media.Movie("The Matrix", "A computer hacker learns from mysterious rebels about the true nature of his "
                                       "reality and his role in the war against its controllers.",
                         "https://images-na.ssl-images-amazon.com/images/M"
                         "/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY"
                         "@._V1_SY1000_CR0,0,665,1000_AL_.jpg", "https://www.youtube.com/watch?v=vKQi3bBA1y8")

snatch = media.Movie("Snatch", "Inescrupulous boxing promoters, violent bookmakers, a Russian gangster, incompetent "
                               "amateur robbers, and supposedly Jewish jewelers fight to track down a priceless stolen "
                               "diamond.",
                     "https://images-na.ssl-images-amazon.com/images/M"
                     "/MV5BMTA2NDYxOGYtYjU1Mi00Y2QzLTgxMTQtMWI1MGI0ZGQ5MmU4XkEyXkFqcGdeQXVyNDk3NzU2MTQ"
                     "@._V1_SY1000_SX684_AL_.jpg", "https://www.youtube.com/watch?v=ni4tEtuTccc")

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker, looking for a way to change his life, crosses paths "
                         "with a devil-may-care soap maker, forming an underground fight club that "
                         "evolves into something much, much more.",
                         "https://images-na.ssl-images-amazon.com/images/M"
                         "/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_.jpg",
                         "https://www.youtube.com/watch?v=_XgQA9Ab0Gw")

inglourious_basterds = media.Movie("Inglourious Basterds", "In Nazi-occupied France during World War II, a plan to "
                                                           "assassinate Nazi leaders by a group of Jewish U.S. "
                                                           "soldiers coincides with a theatre owner's vengeful plans "
                                                           "for the same.",
                                   "https://images-na.ssl-images-amazon.com/images/M"
                                   "/MV5BOTJiNDEzOWYtMTVjOC00ZjlmLWE0NGMtZmE1OWVmZDQ2OWJhXkEyXkFqcGdeQXVyNTIzOTk5ODM"
                                   "@._V1_SY1000_SX675_AL_.jpg", "https://www.youtube.com/watch?v=c9AXOq4an3Y")

movies = [elite_squad, city_of_god, the_matrix, snatch, fight_club, inglourious_basterds]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)
