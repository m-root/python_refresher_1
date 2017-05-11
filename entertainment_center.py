# import fresh_tomatoes
import media


toy_story = media.Movie("Red 2",
                         "Story of a death squad",
                         "http://www.youtube.com",
                         "http://www.wiwkipedia.com")


# print(toy_story.poster_image_url)


avatar = media.Movie("AVATAR",
                     "Story of Avatar",
                     "http://www.youtube.com",
                     "http://www.wiwkipedia.com")

print(avatar.storyline)
# avatar.show_trailer()


dead = media.Movie("DEAD",
                   "Story of a dead ",
                   "http://www.youtube.com",
                   "http://www.wiwkipedia.com")

# movies = [toy_story, avatar, dead]
# fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)