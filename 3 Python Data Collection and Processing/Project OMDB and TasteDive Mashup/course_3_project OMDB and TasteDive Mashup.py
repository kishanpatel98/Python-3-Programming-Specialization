import json
import requests_with_caching

# Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

def get_movies_from_tastedive(title):
    endpoint = 'https://tastedive.com/api/similar'
    param = {}
    param['q'] = title
    param['type'] = 'movies'
    param['limit'] = 5

    response = requests_with_caching.get(endpoint, params = param)
    #print(response.url)
    #print(response.text)
    return json.loads(response.text)

get_movies_from_tastedive("Bridesmaids")
get_movies_from_tastedive("Black Panther")


# Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.
def extract_movie_titles(info):
    #print(info)
    #print(info['Similar']['Results'])
    #print([movie['Name'] for movie in info['Similar']['Results']])
    return [movie['Name'] for movie in info['Similar']['Results']]

extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
extract_movie_titles(get_movies_from_tastedive("Black Panther"))

# Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.
def get_related_titles(movies):
    related = []
    #print(movies)

    for movie in movies:
        temp = extract_movie_titles(get_movies_from_tastedive(movie))
        #print(temp)

        for new_movie in temp:
            if new_movie not in related:
                #print(new_movie)
                related.append(new_movie)
                #print(related)

    #print (related)
    return related

get_related_titles(["Black Panther", "Captain Marvel"])
get_related_titles([])

# Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

# Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.
def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'

    response = requests_with_caching.get(endpoint, params = param)
    #print(response.url)
    #print(response.text)
    return json.loads(response.text)

get_movie_data("Venom")
get_movie_data("Baby Mama")

# Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.
import json
import requests_with_caching

def get_movie_data(title):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = title
    param['r'] = 'json'

    response = requests_with_caching.get(endpoint, params = param)
    #print(response.url)
    #print(response.text)
    return json.loads(response.text)

def get_movie_rating(info):
    #print("INFO: " + str(info))
    for movie in info['Ratings']:
        #print("RATINGS" + str(movie))
        if movie['Source'] == 'Rotten Tomatoes':
            #print(int(movie['Value'][:-1]))
            return int(movie['Value'][:-1]) #gets rid of % at end of rating value
    return 0

get_movie_rating(get_movie_data("Deadpool 2"))

# Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

def get_sorted_recommendations(movies):
    # ratings = {}
    #
    # for movie in get_related_titles(movies):
    #     rating = get_movie_rating(get_movie_data(movie))
    #     ratings[movie] = rating
    #     #print(sorted(ratings.items(), key = lambda movie: (movie[1], movie[0]), reverse = True))
    # return [titles[0] for titles in sorted(ratings.items(), key = lambda movie: (movie[1], movie[0]), reverse = True)]

    return sorted(get_related_titles(movies), key = lambda title: (get_movie_rating(get_movie_data(title)), title), reverse = True)



get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
