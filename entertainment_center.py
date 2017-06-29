import media
import fresh_tomatoes

# Create instances of movie. Max 79 characters for each line, except for links/URL.
forrest_gump = media.Movie("Forrest Gump",
                           "While not intelligent, Forrest Gump has accidentally been present"
                           " at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "https://goo.gl/xHzL7o",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

good_will_hunting = media.Movie("Good Will Hunting",
                                "Will Hunting, a janitor at M.I.T., has a gift for mathematics,"
                                " but needs help from a psychologist to find direction in his life.",
                                "https://goo.gl/dZ7AiS",
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's wife,"
                           " and a pair of diner bandits intertwine in four tales of"
                           " violence and redemption.",
                           "https://goo.gl/qj2F7e",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

blade_runner = media.Movie("Blade Runner",
                           "A blade runner must pursue and try to terminate four"
                           "replicants who stole a ship in space and have returned" 
                           " to Earth to find their creator.",
                           "https://goo.gl/zjQizv",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")

star_wars = media.Movie("Star Wars: A New Hope",
                        "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot,"
                        " a wookiee and two droids to save the galaxy from the Empire's"
                        " world-destroying battle-station, while also attempting to rescue"
                        " Princess Leia from the evil Darth Vader.",
                        "https://goo.gl/YSG3rv",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

akira = media.Movie("Akira",
                    "A secret military project endangers Neo-Tokyo when it turns a biker gang"
                    "member into a rampaging psychic psychopath that only two teenagers and a group"
                    "of psychics can stop.",
                    "https://goo.gl/RoyCwv",
                    "https://www.youtube.com/watch?v=7G5zQW4TinQ")

drive = media.Movie("Drive",
                    "A mysterious Hollywood stuntman and mechanic moonlights as a getaway"
                    " driver and finds himself in trouble when he helps out his neighbor.",
                    "https://goo.gl/Q7KoLR",
                    "https://www.youtube.com/watch?v=sY1TLgqfjvw")

mad_max = media.Movie("Mad Max",
                      "A woman rebels against a tyrannical ruler in postapocalyptic Australia"
                      " in search for her home-land with the help of a group of female prisoners,"
                      " a psychotic worshipper, and a drifter named Max.",
                      "https://goo.gl/CmWvHV",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

ex_machina = media.Movie("Ex Machina",
                         "A young programmer is selected to participate in a"
                         " ground-breaking experiment in synthetic intelligence by"
                         " evaluating the human qualities of a breath-taking humanoid A.I.",
                         "https://goo.gl/vkB8MH",
                         "https://www.youtube.com/watch?v=EoQuVnKhxaM")

movies = [pulp_fiction, star_wars, akira, good_will_hunting, blade_runner, drive, mad_max, forrest_gump, ex_machina]
#List all the movies inside an array
fresh_tomatoes.open_movies_page(movies)
#Pass movies as the argument to open_movies_page from fresh_tomatoes
