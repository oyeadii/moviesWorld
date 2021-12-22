from flask import Flask, render_template
import config
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_movies():
    url = "https://api.themoviedb.org/3/movie/now_playing?api_key="+config.TMDB_API_KEY+'&language=en-US'
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    url2= "https://api.themoviedb.org/3/movie/popular?api_key="+config.TMDB_API_KEY+'&language=en-US'
    response2 = urllib.request.urlopen(url2)
    data2 = response2.read()
    dict2 = json.loads(data2)
    return render_template ("index.html", movies=dict["results"], movies2=dict2["results"], title=dict2['results'][0]['title'] )

@app.route("/movies")
def get_movies_list():
    url = "https://api.themoviedb.org/3/movie/popular?api_key="+config.TMDB_API_KEY+'&language=en-US'

    response = urllib.request.urlopen(url)
    movies = response.read()
    dict = json.loads(movies)

    movies = []

    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movies.append(movie)

    return {"results": movies}

if __name__ == '__main__':
    app.run(debug=True)