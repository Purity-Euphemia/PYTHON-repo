import unittest


from DSA.MovieApp import MovieApp


class TestMovieApp(unittest.TestCase):
    def setUp(self):
        self.movies = ["Frozen"]
        self.ratings = [[4, 5]]

    def test_that_movieBox_is_empty(self):
        self.movies = []
        self.assertEqual(0, len(self.movies))


    def test_that_one_movie_is_added(self):
        self.movies.append("SnowWhite")
        self.assertEqual(len(self.movies),2)
        self.assertIn("SnowWhite", self.movies)


    def test_that_two_movie_is_added(self):
        self.movies.append("ShowWhite")
        self.movies.append("Moana")
        self.assertEqual(len(self.movies), 3)
        self.assertIn("ShowWhite",self.movies)
        self.assertIn("Moana", self.movies)


    def test_that_movie_is_insise_the_movie(self):
        self.movies = ["Frozen","Moana","ShowWhite"]
        self.assertEqual(3, len(self.movies))
        self.assertIn("Frozen", self.movies[0])
        self.assertIn("Moana", self.movies[1])
        self.assertIn("ShowWhite", self.movies[2])

    def test_that_movie_is_removed_from_the_movie_app(self):
        self.movies = ["Frozen","Moana","ShowWhite"]
        self.assertEqual(3, len(self.movies))
        self.movies.remove("Frozen")
        self.assertNotIn("Frozen", self.movies)
        self.assertTrue(2, len(self.movies))

    def test_that_add_duplicate_movie(self):
        self.movies.append("Frozen")
        self.movies.append("Frozen")
        self.assertTrue("Frozen" in self.movies)

    def test_that_rating_is_added_to_the_movie(self):
        self.movies.append("Moana")
        self.ratings.append([5])
        self.assertEqual( len(self.movies), 2)
        self.assertEqual(self.ratings[1],[5])
        self.assertIn(5, self.ratings[1])

    def test_that_movie_rating_is_invalid_for_the_movie(self):
        rating = 6
        is_invalid = 1 <= rating <= 5
        self.assertEqual(is_invalid, False)

    def test_that_movie_rating_is_twice(self):
        self.movies.append("Moana")
        self.ratings.append([5, 3])
        self.assertEqual( len(self.movies), 2)
        self.assertEqual(self.ratings[1],[5, 3])
        self.assertIn(3, self.ratings[1])

    def test_the_rating_of_the_movie_is_incremented_by_one(self):
        initial_rating_count = len(self.ratings)
        self.movies.append("Moana")
        self.ratings.append([5, 3])
        self.assertEqual(len(self.ratings), initial_rating_count + 1)
        self.assertEqual(self.ratings[1], [5, 3])















if __name__ == '__main__':
    unittest.main()
