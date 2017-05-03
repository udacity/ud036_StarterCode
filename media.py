#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser


class Movie:
    """
    It provides a way to store the movie relation information.
    """

    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image_url,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    @staticmethod
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
