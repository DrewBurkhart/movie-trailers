import webbrowser

class Movie():
    """The Movie() class will create the framework for each individual movie
    on the resulting web page. The instances are defined in 
    entertainment_center.py"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): # NOQA
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
