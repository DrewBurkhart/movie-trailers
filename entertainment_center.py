# Importing media to create instances of my movie class
import media
# Importing fresh_tomatoes to use the open_movies_page function
import fresh_tomatoes

# Instantiating my movie class instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # NOQA
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

social_network = media.Movie("The Social Network",
                             "The founding of Facebook",
                             "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg", # NOQA
                             "https://www.youtube.com/watch?v=lB95KLmpLR4")

blackhat = media.Movie("Blackhat",
                             "A hacker trying to save the world",
                             "https://upload.wikimedia.org/wikipedia/en/5/58/Blackhat_poster.jpg", # NOQA
                             "https://www.youtube.com/watch?v=jZ1ZDlLImF8")

wargames = media.Movie("Wargames",
                             "A hacker may end the world",
                             "https://upload.wikimedia.org/wikipedia/en/2/29/Wargames.jpg", # NOQA
                             "https://www.youtube.com/watch?v=xogbyv108kI")

friends_with_benefits = media.Movie("Friends With Benefits",
                             "Blah Blah Blah",
                             "https://upload.wikimedia.org/wikipedia/en/4/4e/Friends_with_benefits_poster.jpg", # NOQA
                             "https://www.youtube.com/watch?v=iJS-wWqVAyk")


# Filling my movie list with the instances I've created
movies = [toy_story, avatar, social_network, blackhat, wargames, friends_with_benefits] # NOQA
fresh_tomatoes.open_movies_page(movies)
