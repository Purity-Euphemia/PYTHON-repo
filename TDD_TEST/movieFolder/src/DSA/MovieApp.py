from datetime import datetime


class MovieApp:
    def __init__(self):
        self.movies = []
        self.rating = []

    def add_movie(self, title):
        if title == "":
            return "no movie"
        if title in self.movies:
            return "already added"
        return self.movies.append({"movie": title, "time": datetime.datetime.now()})

    def rating_movie(self, title,rating):
        if title not in self.movies:
            return "no movie"
        if rating < 1 or rating > 5:
            return "rating must be between 1 and 5"
        self.movies[title]["rating"].append(rating)
        return "success"


    def average_rating(self):
        average = 0
        for movie in self.movies:
            average += movie["rating"]
            average /= len(self.movies)
            return average

    def average_rating_of_movie(self, movie):
        if movie in self.movies:
            return self.movies[movie]["rating"][0] / len(self.movies)
        else:
            return 0

    def exist (self, movie):
        if movie in self.movies:
            return True
        else:
            return False








