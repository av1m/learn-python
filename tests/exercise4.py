import unittest

from exercise.exercise4 import *


class TestInline(unittest.TestCase):
    def test_long_word(self):
        # equal
        self.assertEqual(long_words(3, ['hey', 'how', 'test', 'my best']), {"3": ["hey", "how", "test"]})
        self.assertEqual(long_words("3", ['hey', 'how', 'test', 'my best']), {"3": ["hey", "how", "test"]})
        self.assertEqual(long_words(4, ['hey', 'how', 'test', 'my best']), {})
        self.assertEqual(long_words(4, ['hey', 'how', 'test', 'ok', 'my best']), {"2": ["ok"]})
        # raise ValueError
        self.assertRaises(ValueError, lambda: long_word(2, 2))
        self.assertRaises(ValueError, lambda: long_word(2, "salut"))
        self.assertRaises(ValueError, lambda: long_word(2, {"x": "y"}))
        self.assertRaises(ValueError, lambda: long_word(2, {0: ['you', 'are', 'wrong']}))
        # raise TypeError
        self.assertRaises(TypeError, lambda: long_word("test", ['hey', 'brother']))
        self.assertRaises(TypeError, lambda: long_word([22, 22], ['hey', 'brother']))
        self.assertRaises(TypeError, lambda: long_word({3: False}, ['hey', 'brother']))

if __name__ == "__main__":
    unittest.main()
