import json
import tmdbsimple as tmdb

tmdb.API_KEY = ''

'''
    function that finds movie with the phrase
    and prints url of poster and trailer
    just write title in title
    This function also prints other movies that have
    phrase that is in the title.
    So you can find posters and trailers of other movies.
'''

title = "The Godfather"
search = tmdb.Search()


def get_movie(title):

        dataBase = search.movie(query=title)
        number = dataBase['results'][0]['id']
        movie = tmdb.Movies(number)
        print ('https://www.youtube.com/watch?v=' +
               movie.videos()['results'][0]['key'])
        print ('https://image.tmdb.org/t/p/w500' +
               dataBase['results'][0]['poster_path'])
        for s in search.results:
                print(s['title'])

get_movie(title)
#Adding closing option on enter#
input('Press Enter to exit')
