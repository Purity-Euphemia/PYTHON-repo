import unittest


from DSA.MovieApp import MovieApp


class TestMovieApp(unittest.TestCase):
    def setUp(self):
        self.movies = ["Frozen"]
        self.ratings = [[4,5]]

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












if __name__ == '__main__':
    unittest.main()
