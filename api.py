import requests 

def search_movie(name):
    url = f"http://www.omdbapi.com/?t={name}&apikey=4937dc67"
    response = requests.get(url)
    return response.json()

def search_movies(name):
    url = f"http://www.omdbapi.com/?s={name}&apikey=4937dc67"
    response = requests.get(url)
    return response.json()

def search_movie_id(imdb_id):
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey=4937dc67"
    response = requests.get(url)
    return response.json()