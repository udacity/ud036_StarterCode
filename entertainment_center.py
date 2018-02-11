# coding=utf-8
import fresh_tomatoes
import media

# dragonballz is an instance of class Movie()
dragonballz = media.Movie(
    'DBZ Resurrection of F',
    '''Goku and Vegeta must protect Earth from the resurrected Frieza and his army
    of soldiers.''',
    'https://upload.wikimedia.org/wikipedia/en/6/6a/DBZ_THE_MOVIE_NO._15.png',
    'https://www.youtube.com/watch?v=5z_nWwKBiRw')

# the town is an instance of class Movie()
the_town = media.Movie(
    'The Town',
    '''Doug MacRay (Ben Affleck) leads a band of ruthless bank robbers and has no
    real attachments except for James (Jeremy Renner), who -- despite his
    dangerous temper -- is like a brother. Everything changes for Doug when
    James briefly takes a hostage, bank employee Claire Keesey. Learning that
    she lives in the gang\'s neighborhood, Doug seeks her out to discover what
    she knows, and he falls in love. As the romance deepens, he wants out of
    his criminal life, but that could threaten Claire.''',
    'https://upload.wikimedia.org/wikipedia/en/d/da/The_Town_Poster.jpg',
    'https://www.youtube.com/watch?v=WcXt9aUMbBk')

# den of thieves is an instance of class Movie()
den_of_thieves = media.Movie(
    'Den of Thieves',
    '''Nick O\'Brien is the hard-drinking leader of the Regulators, an elite unit
    of the Los Angeles County Sheriff\'s Department. Ray Merrimen is the
    recently paroled leader of the Outlaws, a gang of ex-military men who use
    their expertise and tactical skills to evade the law. O\'Brien, Merrimen
    and their crews soon find themselves on a direct collision course as the
    criminals hatch an elaborate plan for a seemingly impossible heist -- the
    city\'s Federal Reserve Bank.''',
    'https://i2.wp.com/teaser-trailer.com/wp-content/uploads/Den-of-Thieves-movie-poster-2.jpg?ssl=1',  # noqa
    'https://www.youtube.com/watch?v=HusPt_1-qto')

# avatar is an instance of class Movie()
avatar = media.Movie(
    'Avatar',
    '''On the lush alien world of Pandora live the Na\'vi, beings who appear
    primitive but are highly evolved. Because the planet\'s environment is
    poisonous, human/Na\'vi hybrids, called Avatars, must link to human minds
    to allow for free movement on Pandora. Jake Sully (Sam Worthington), a
    paralyzed former Marine, becomes mobile again through one such Avatar and
    falls in love with a Na\'vi woman (Zoe Saldana). As a bond with her grows,
    he is drawn into a battle for the survival of her world''',
    'http://cdn1-www.comingsoon.net/assets/uploads/2009/08/file_57684_0_avatarhiresposter.jpg',  # noqa
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

# boruto the movie is an instance of class Movie()
boruto_the_movie = media.Movie(
    'Boruto The Movie',
    '''Several years after the end of the Shinobi War, Naruto\'s son Boruto is
    about to enter the Chûnin exams alongside Sarada Uchiha and the mysterious
    Mitsuki.''',
    'https://vignette.wikia.nocookie.net/naruto/images/5/50/Boruto_the_Movie_poster_2.png/revision/latest?cb=20161117222759',  # noqa
    'https://www.youtube.com/watch?v=Qyonn5Vbg7s')

# hitch is an instance of class Movie()
hitch = media.Movie(
    'Hitch',
    '''Dating coach Alex "Hitch" Hitchens (Will Smith) mentors a bumbling
    client, Albert (Kevin James), who hopes to win the heart of the glamorous
    Allegra Cole (Amber Valletta). While Albert makes progress, Hitchens faces
    his own romantic setbacks when proven techniques fail to work on Sara Melas
    (Eva Mendes), a tabloid reporter digging for dirt on Allegra Cole\'s love
    life. When Sara discovers Hitchens\' connection to Albert -- now Allegra\'s
    boyfriend -- it threatens to destroy both relationships.''',
    'https://images-na.ssl-images-amazon.com/images/I/419kSwDKlYL.jpg',
    'https://www.youtube.com/watch?v=dMaq_pfxs-0')

# avengers is an instance of class Movie()
avengers = media.Movie(
    'Avengers: Age of Ultron',
    '''When Tony Stark (Robert Downey Jr.) jump-starts a dormant peacekeeping
    program, things go terribly awry, forcing him, Thor (Chris Hemsworth), the
    Incredible Hulk (Mark Ruffalo) and the rest of the Avengers to reassemble.
    As the fate of Earth hangs in the balance, the team is put to the ultimate
    test as they battle Ultron, a technological terror hell-bent on human
    extinction. Along the way, they encounter two mysterious and powerful
    newcomers, Pietro and Wanda Maximoff.''',
    'http://static.tvtropes.org/pmwiki/pub/images/avengers_age_of_ultron.jpg',
    'https://www.youtube.com/watch?v=JAUoeqvedMo')

# transformer is an instance of class Movie ()
transformer = media.Movie(
    'Transformer: The Last Knight',
    '''Humans are at war with the Transformers, and Optimus Prime is gone. The
    key to saving the future lies buried in the secrets of the past and the
    hidden history of Transformers on Earth. Now, it\'s up to the unlikely
    alliance of inventor Cade Yeager, Bumblebee, an English lord and an Oxford
    professor to save the world.''',
    'https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg',  # noqa
    'https://www.youtube.com/watch?v=6Vtf0MszgP8')

# ninja assassin is an instance of class Movie ()
ninja_assassin = media.Movie(
    'Ninja Assassin',
    '''Trained in methods of killing from an early age, Raizo (Rain) is a member
    of the secret clan of assassins known as the Ozunu. After the Ozunu kill
    his friend, however, Raizo breaks free from them and vanishes. Meanwhile,
    Europol agent Mika Coretti (Naomie Harris) discovers a money trail linking
    the the group to murders. Raizo saves Mika from his former comrades and
    joins forces with her to bring down the Ozunu forever.''',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTcxNDYzMjU1Ml5BMl5BanBnXkFtZTcwMTYzOTM3Mg@@._V1_UY1200_CR90,0,630,1200_AL_.jpg',  # noqa
    'https://www.youtube.com/watch?v=NhYH26KTNbQ')

movies = [
    dragonballz,
    the_town, den_of_thieves,
    avatar, boruto_the_movie,
    hitch, avengers, transformer,
    ninja_assassin]
fresh_tomatoes.open_movies_page(movies)
