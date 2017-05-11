import webbrowser

class Movie():
    """this is a documentation"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self,
                 movie_title,
                 story_line,
                 poster_image_url,
                 trailer_youtube_url):

        self.title = movie_title
        self.storyline = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)