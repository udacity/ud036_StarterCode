import media
import fresh_tomatoes

forrest_gump = media.Movie("Forrest Gump",
                           "While not intelligent, Forrest Gump has accidentally been present at many historic moments, but his true love, Jenny Curran, eludes him.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

good_will_hunting = media.Movie("Good Will Hunting",
                                "Will Hunting, a janitor at M.I.T., has a gift for mathematics, but needs help from a psychologist to find direction in his life.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BOTI0MzcxMTYtZDVkMy00NjY1LTgyMTYtZmUxN2M3NmQ2NWJhXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,655,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=PaZVjZEFkRs")

pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
                           )

blade_runner = media.Movie("Blade Runner",
                           "A blade runner must pursue and try to terminate four replicants who stole a ship in space and have returned to Earth to find their creator.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=eogpIG53Cis")

star_wars = media.Movie("Star Wars: A New Hope",
                        "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a wookiee and two droids to save the galaxy from the Empire's world-destroying battle-station, while also attempting to rescue Princess Leia from the evil Darth Vader.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYzQ2OTk4N2QtOGQwNy00MmI3LWEwNmEtOTk0OTY3NDk2MGJkL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,664,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=1g3_CFmnU7k")

akira = media.Movie("Akira",
                    "A secret military project endangers Neo-Tokyo when it turns a biker gang"
                    "member into a rampaging psychic psychopath that only two teenagers and a group"
                    "of psychics can stop.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BM2ZiZTk1ODgtMTZkNS00NTYxLWIxZTUtNWExZGYwZTRjODViXkEyXkFqcGdeQXVyMTE2MzA3MDM@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=7G5zQW4TinQ")

drive = media.Movie("Drive",
                    "A mysterious Hollywood stuntman and mechanic moonlights as a getaway"
                    "driver and finds himself in trouble when he helps out his neighbor.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BZjY5ZjQyMjMtMmEwOC00Nzc2LTllYTItMmU2MzJjNTg1NjY0XkEyXkFqcGdeQXVyNjQ1MTMzMDQ@._V1_SY1000_SX675_AL_.jpg",
                    "https://www.youtube.com/watch?v=sY1TLgqfjvw")

mad_max = media.Movie("Mad Max",
                      "A woman rebels against a tyrannical ruler in postapocalyptic Australia in search for her home-land with the help of a group of female prisoners, a psychotic worshipper, and a drifter named Max.",
                      "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyMTE0ODcxNF5BMl5BanBnXkFtZTgwODE4NDQzNTE@._V1_SY1000_CR0,0,687,1000_AL_.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

ex_machina = media.Movie("Ex Machina",
                         "A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=EoQuVnKhxaM")

movies = [pulp_fiction, star_wars, akira, good_will_hunting, blade_runner, drive, mad_max, forrest_gump, ex_machina]
fresh_tomatoes.open_movies_page(movies)
