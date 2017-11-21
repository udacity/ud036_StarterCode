import media
import fresh_tomatoes
the_dark_knight = media.Movie("The Dark Knight",
                              "A man protecting his city" +
                              "disguised in bat suite",
                              "https://encrypted-tbn0.gstatic.com/images?" +
                              "q=tbn:ANd9GcT3vVwDZYVjhrZsXQjhLkdZQAT9S6" +
                              "Irp6wSZhjO9S0rZZ-wjjPn",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")
up = media.Movie("UP",
                 "An old man who is on the quest fo fulfilling" +
                 " his dead wife's wishand a kid who is struck around" +
                 "  the old man are doing adventure things",
                 "https://vignette.wikia.nocookie.net/disney/" +
                 "images/a/a6/Up_Poster_Run.jpg/" +
                 "revision/latest?cb=20160202180816",
                 "https://www.youtube.com/watch?v=ZE_V0g9q4g0")
the_impossible = media.Movie("The impossible",
                             "How a family is getting reunited after" +
                             " Tsunami disaster ",
                             "https://upload.wikimedia.org/wikipedia/en" +
                             "/b/b8/The_Impossible.jpg",
                             "https://www.youtube.com/watch?v=Bgw394ZKsis")
harry_potter = media.Movie("The Harry Potter And The Sorcerer's Stone",
                           "A kid famous in wizard world" +
                           " attending wizard school",
                           "https://static.rogerebert.com/uploads/movie" +
                           "/movie_poster/harry-potter-and-the-sorcerers-" +
                           "stone-2001/large_uLGaJ9FgPWf7EUgwjp9RTmHemw8.jpg",
                           "https://www.youtube.com/watch?v=PbdM1db3JbY")
the_zootopia = media.Movie("The Zootopia",
                           "A bunny cop and wolf trying to" +
                           " catch the criminal gang",
                           "https://www.flayrah.com/sites/default/files/u/" +
                           "crossaffliction/zootopialittlegoldenbook.jpg",
                           "https://www.youtube.com/watch?v=jWM0ct-OLsM")
the_lord_of_rings = media.Movie("The_Lord_of_the_Rings:" +
                                "The_Fellowship_of_the_Ring",
                                "The fate of Middle-earth hangs in t" +
                                "he balance as Frodo and eight companions " +
                                " begin who form the Fellowship of the Ring" +
                                "their journey to Mount Doom in ," +
                                "the land of Mordor.",
                                "https://upload.wikimedia.org/wikipedia/en" +
                                "/9/9d/The_Lord_of_the_Rings_The_Fellowship" +
                                "_of_the_Ring_%282001%29_" +
                                "theatrical_poster.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")
movies = [the_dark_knight, up, the_impossible, harry_potter,
          the_zootopia, the_lord_of_rings]

fresh_tomatoes.open_movies_page(movies)
