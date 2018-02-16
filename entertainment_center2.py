#media2 is the formating module for classes
import media2
#fresh_tomatoes is the module to run the web page
import fresh_tomatoes

toy_story = media2.Movie(
                        "Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio",
                        "160",
                        "4.5 of 5!"
                        )
#print(toy_story.storyline)

avatar = media2.Movie(
                     "Avatar",
                     "A marine on an alien planet fights and has alien sex",
                     #"https://ep01.epimg.net/cultura/imagenes/2017/04/23/actualidad/1492982810_329408_1492984569_noticia_normal_recorte1.jpg"
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Avatar_picture.jpg/220px-Avatar_picture.jpg",
                    #"https://zardra.deviantart.com/art/Feel-the-peace-Avatar-148548255",
                      #"http://james-camerons-avatar.wikia.com/wiki/File:Main_Wallpaper.png",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io",
                     "150",
                    "4 of 5!"
                     )
#print(avatar.poster_image_url)

dirty_girl = media2.Movie (
                          "Dirty Girl",
                          "A young girl who is stereotyped goes on a road trip with her overweight alternative lifesyle male friend to discover herself.  Really its a movie about teenage stereo typyes.",
                          "https://media.npr.org/assets/img/2011/10/03/dg_d008_00183r_wide-ea07d599e9d17ee9820019a037a4e635d1e5a785-s900-c85.jpg",
                          #"https://youtu.be/Qy3eAiB5UPo"
                          "https://www.youtube.com/watch?v=3DylhbVj8DY",
                          "139",
                          "0.5 of 5!"
                          )

million_dolar = media2.Movie (
                              "Million Dollar Baby",
                              "A young girl learns how to fight, kicks ass, and breaks her neck because Client Eastwood is slow and lazy",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxNzA1NDQxOV5BMl5BanBnXkFtZTcwNTkyMTIzMw@@._V1_UY1200_CR92,0,630,1200_AL_.jpg",
                              "https://www.youtube.com/watch?v=4B0zmj0-Iac",
                              "Not Enough",
                              "25 of 5!"
                              )
#list of movies from above
movies = [toy_story, avatar, dirty_girl, million_dolar]
#fresh_tomatoes is the script running webpage
fresh_tomatoes.open_movies_page(movies)


#dirty_girl.show_trailer()
#dirty_girl.show_poster()
