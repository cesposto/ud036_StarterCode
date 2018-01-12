#Author: Chris Esposto
#Date: Jan 10, 2018

class Movie():
    """The Class contains the title, trailer and poster about movies"""

    def __init__(self, title, trailer_youtube_url, poster_image_url):
       self.title = title
       self.trailer_youtube_url = trailer_youtube_url
       self.poster_image_url = poster_image_url
