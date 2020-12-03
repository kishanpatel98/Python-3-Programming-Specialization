# Python Data Collection And Processing Course Project

Final Project of the Data Collection and Processing with Python course which is a part of the Python 3 Programming Specialization offered by University of Michigan on Coursera. More information can be found at: https://www.coursera.org/learn/data-collection-processing-python/home/welcome

## About It
This project will take you through the process using REST APIs to combine data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

The documentation for the API is at: https://tastedive.com/read/api

The documentation for the API is at: https://www.omdbapi.com/

## Functions
#### `def get_movies_from_tastedive(title):`
Takes in the title of a movie and returns a dictionary of 5 movies and related details which are similar to the movie being queried. The 5 movies are stored under key 'Similar'.

#### `def extract_movie_titles(info):`
Takes in a dictionary of 5 movies and returns just movie titles.

#### `def get_related_titles(movies):`
Takes in a movie title, uses `get_movies_from_tastedive()` function to retrieve 5 movies which are similar and then returns the titles of those movies with `extract_movie_titles()` function.

#### `def get_movie_data(title):`
Takes in the title of a movie and returns a dictionary with the data of the movie.

#### `def get_movie_rating(info):`
Takes in a dictionary from `def get_movie_data():` function and extracts the Rotten Tomatoes rating from the data. Returns 0 if a rating isn't found.

#### `get_sorted_recommendations(movies):`
Takes in list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the `get_movie_rating()` function. Ties are listed in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
