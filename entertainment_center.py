import fresh_tomatoes
import media
import imdb

youtube_prepend = 'https://www.youtube.com/watch?v='
my_movies_list = []
imdb_data = imdb.IMDb()

#Dictionary to store IMDb movie Id and trailer links in separate keys
movies_dict = {
        'Toy Story': {'id': '0114709', 'trailer':'KYz2wyBy3kc'},
        'avatar': {'id':'0499549', 'trailer':'5PSNL1qE6VY'},
        'the_avengers': {'id':'0848228', 'trailer':'hIR8Ar-Z4hw'},
        'i_robot': {'id':'0343818', 'trailer':'s0f3JeDVeEo'},
        'empire_of_the_sun': {'id':'0092965', 'trailer':'i_WiDVA1kLY'},
        'lord_of_the_rings':{'id':'0120737', 'trailer': 'V75dMMIW2B4'}
    }


#Loop to iterate over movie keys to create instances of Movie class
for x in movies_dict:
    val = movies_dict[x]
    val2 = movies_dict[x].values()
    movie_data = imdb_data.get_movie(val2[0])
    movie_trailer = youtube_prepend+val2[1]
    movie = media.Movie(movie_data['title'],movie_data['plot outline'], movie_data['cover url'],movie_trailer)
    my_movies_list.append(movie)
                        
    
        
    

fresh_tomatoes.open_movies_page(my_movies_list)


