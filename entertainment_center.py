import media
import fresh_tomatoes


# List of movies with details


amelie = media.Movie(
    "Amelie",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Amelie_poster.jpg",
    "https://www.youtube.com/watch?v=2UT5xaAfxWU"
    )

# Tests during creation of instances
# print(amelie.movie_title)
# amelie.show_trailer()

best_in_show = media.Movie(
    "Best in Show",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5OTc0NDU1MF5BMl5BanBnXkFtZTYwNzk1OTI3._V1_.jpg",
    "https://www.youtube.com/watch?v=yeifMjqpsg0"
    )

cuckoo = media.Movie(
    "One Flew Over the Cuckoo's Nest",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZjA0OWVhOTAtYWQxNi00YzNhLWI4ZjYtNjFjZTEyYjJlNDVlL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=oUobWmLF9WQ"
    )


forrest_gump = media.Movie(
    "Forrest Gump",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",
    "https://www.youtube.com/watch?v=2WSyJgydTsA"
    )


twelve_angry_men = media.Movie(
    "12 Angry Men",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMWU4N2FjNzYtNTVkNC00NzQ0LTg0MjAtYTJlMjFhNGUxZDFmXkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_SY1000_CR0,0,649,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=Dosg0p7LAB4"
    )


west_side_story = media.Movie(
    "West Side Story",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM0NDAxOTI5MF5BMl5BanBnXkFtZTcwNjI4Mjg3NA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=NF1L3NorO3E"
    )


unforgiven = media.Movie(
    "Unforgiven",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BODM3YWY4NmQtN2Y3Ni00OTg0LWFhZGQtZWE3ZWY4MTJlOWU4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=XDAXGILEdro"
    )

# create array with movies from above

movies = [amelie, best_in_show, cuckoo, forrest_gump, twelve_angry_men, west_side_story, unforgiven]


# give open_movies_pages function (in fresh_tomatoes file) the list of the above movies

fresh_tomatoes.open_movies_page(movies)
