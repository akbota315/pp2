#1
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#2
def is_good_movie(movie):
    return movie["imdb"] > 5.5
print(is_good_movie(movies[0]))

#3
def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
print(movies_above_5_5(movies))

#4
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"].lower() == category.lower()]
print(movies_by_category(movies, "Romance"))

#5
def average_imdb_score(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
print(average_imdb_score(movies))

#6
def average_imdb_score_by_category(movies, category):
    category_movies = [movie for movie in movies if movie["category"].lower() == category.lower()]
    if category_movies:
        total_score = sum(movie["imdb"] for movie in category_movies)
        return total_score / len(category_movies)
    return 0
print(average_imdb_score_by_category(movies, "Romance"))