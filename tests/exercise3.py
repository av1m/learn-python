import unittest

from exercise.exercise3 import *


class TestTernaryOperator(unittest.TestCase):
    def test_is_even(self):
        # equal
        self.assertEqual(is_even(3), False)
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(829), False)
        self.assertEqual(is_even(772), True)
        # raise
        self.assertRaises(TypeError, lambda: is_even([2]))
        self.assertRaises(TypeError, lambda: is_even("2"))

    def test_which_case(self):
        # raise
        self.assertRaises(TypeError, lambda: which_case([2]))
        self.assertRaises(TypeError, lambda: which_case(2))
        self.assertRaises(TypeError, lambda: which_case(["hello"]))
        self.assertRaises(TypeError, lambda: which_case("22"))
        # equal
        self.assertEqual(which_case("hello"), 0)
        self.assertEqual(which_case("young_and_beautiful"), 0)
        self.assertEqual(which_case("Y1oung_and"), 1)
        self.assertEqual(which_case("yousdq23ng_anD"), -1)
        self.assertEqual(which_case("Yousdq23ng_anD"), 2)

if __name__ == "__main__":
    unittest.main()
