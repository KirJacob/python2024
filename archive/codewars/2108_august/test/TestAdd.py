import unittest
import Add


class TestsAdd(unittest.TestCase):
    def test_add_usual(self):
        assert Add.add(11, 8) == 19

    def test_add_zero(self):
        assert Add.add(1, 0) == 1

    def test_add_two_zeros(self):
        assert Add.add(0, 0) == 0
