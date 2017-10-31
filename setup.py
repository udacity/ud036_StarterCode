from setuptools import setup

setup(name='movie trailer website',
      version='0.0.2',
      packages=['movie_trailer'],
      entry_points={
          'console_scripts': [
              'movie_trailer = movie_trailer.entertainment_center:main'
          ]
          },
      )