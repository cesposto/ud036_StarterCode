# Author: Chris Esposto
# Date: Jan 10, 2018

import media
import fresh_tomatoes

# Creating list of movies
batman_begins = media.Movie("Batman Begins",
                            "https://www.youtube.com/watch?v=3ohiQ6cLRsE",
                            "https://upload.wikimedia.org/wikipedia/en/a/" +
                            "af/Batman_Begins_Poster.jpg")
the_dark_knight = media.Movie("The Dark Knight",
                              "https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
                              "https://upload.wikimedia.org/wikipedia/en/8/" +
                              "8a/Dark_Knight.jpg")
the_dark_knight_rises = media.Movie("The Dark Knight Rises",
                                    "https://www.youtube.com/" +
                                    "watch?v=g8evyE9TuYk",
                                    "https://upload.wikimedia.org/wikipedia/" +
                                    "en/8/83/Dark_knight_rises_poster.jpg")
inception = media.Movie("Inception",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Ince" +
                        "ption_%282010%29_theatrical_poster.jpg")
interstellar = media.Movie("Interstellar",
                           "https://www.youtube.com/watch?v=827FNDpQWrQ",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/" +
                           "Interstellar_film_poster.jpg")
the_prestige = media.Movie("The Prestige",
                           "https://www.youtube.com/watch?v=o4gHCmTQDVI",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/" +
                           "Prestige_poster.jpg")

movies_list = [batman_begins, the_dark_knight, the_dark_knight_rises,
               inception, interstellar, the_prestige]

# Passing list to function to create html page
fresh_tomatoes.open_movies_page(movies_list)
