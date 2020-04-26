import unittest

from exercise.exercise1 import parse_github


class TestGithub(unittest.TestCase):
    def test_login(self):
        self.assertEqual(parse_github(username="av1m"), ["MDQ6VXNlcjM2NDU2NzA5", 36456709, "Avi Mimoun"])
        self.assertEqual(parse_github(username="rubnet"), ["MDQ6VXNlcjIwMjg5NDY2", 20289466, None])
        self.assertEqual(parse_github(username="dylansettbon"), ["MDQ6VXNlcjMyODMyNjg2", 32832686, "dylansettbon"])


if __name__ == '__main__':
    unittest.main()
