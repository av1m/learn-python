import unittest

from exercise.exercise2 import parse_repos



class TestGithub(unittest.TestCase):
    def test_login(self):
        self.assertEqual(parse_repos(username="av1m"), [{"node_id": "MDEwOlJlcG9zaXRvcnkxNzc5NTIwODI=", "avatar_url": "https://avatars2.githubusercontent.com/u/36456709?v=4", "forks": 0},{"node_id": "MDEwOlJlcG9zaXRvcnkxMzQ3MDcyMzA=", "avatar_url": "https://avatars2.githubusercontent.com/u/36456709?v=4", "forks": 0},{"node_id": "MDEwOlJlcG9zaXRvcnkyMzEwNzc1MDA=", "avatar_url": "https://avatars2.githubusercontent.com/u/36456709?v=4", "forks": 1}])
        self.assertEqual(parse_repos(username="rubnet"), [])
        self.assertEqual(parse_repos(username="dylansettbon"), [])
        self.assertEqual(parse_repos(username="k4m4"), [{'node_id': 'MDEwOlJlcG9zaXRvcnkxMjI2MTQ0OTI=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 0}, {'node_id': 'MDEwOlJlcG9zaXRvcnkxMjI1NTA4MTg=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 2}, {'node_id': 'MDEwOlJlcG9zaXRvcnkxMjM2MDQ2NDg=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 3}, {'node_id': 'MDEwOlJlcG9zaXRvcnkxMjMzNTE5NjA=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 3}, {'node_id': 'MDEwOlJlcG9zaXRvcnkxMjI2MTQxODY=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 0}, {'node_id': 'MDEwOlJlcG9zaXRvcnkxMjg2NjY4MjQ=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 22}, {'node_id': 'MDEwOlJlcG9zaXRvcnkxNjU0MDc3NDA=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 0}, {'node_id': 'MDEwOlJlcG9zaXRvcnkxMjM3ODk3MzI=', 'avatar_url': 'https://avatars1.githubusercontent.com/u/8945656?v=4', 'forks': 1}])


if __name__ == "__main__":
    unittest.main()
