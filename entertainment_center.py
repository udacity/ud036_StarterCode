import media
import fresh_tomatoes
import httplib
import json


# Make sure user apply their own API_KEY
'''while True:
    try:
        API_KEY = raw_input("API_KEY:")
    except ValueError:
        print("Please provide a valide TMDb API_KEY.")
        # Back to the loop to prompt user's API_KEY
        continue
    else:
        # Pass the test
        break'''

API_KEY = "5e0d551fc0e7ff087a1f4460c4f7ebb0"


conn = httplib.HTTPSConnection("api.themoviedb.org")

payload = "{}"

# Get the upcoming movie's id, title, poster_path, through request url
conn.request("GET", "/3/movie/upcoming?page=1&language=en-US&api_key="+API_KEY, payload)


res = conn.getresponse()
data = res.read()

# JSON the results of the data of all movies
informations = data.decode("utf-8")
json_informations = json.loads(informations)


#print(json_informations)
#print(json_informations["results"][1]["poster_path"])
#print(len(json_informations["results"])) 


# iterate data of all movies to obtain their'id, title, poster_path
movies = []
i = 0
for i in range(0,len(json_informations["results"])):
    dictionary_movie= {"title": json_informations["results"][i]["title"],
                       "id" : json_informations["results"][i]["id"],
                        "poster_image_url": json_informations["results"][i]["poster_path"]}
    movies.append(dictionary_movie)
    print(movies[i])
    dictionary_movie ={}
    i += 1

#print(movies[1])
    







