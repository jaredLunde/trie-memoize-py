import unittest
from trie_memoize import memoize


class TestMemoize(unittest.TestCase):
    def setUp(self):
        self.seen = False

    def test_one(self):
        @memoize(dict)
        def add10(a):
            self.seen = True
            return a + 10

        self.assertEqual(add10(1), 11)
        self.assertEqual(self.seen, True)
        self.seen = False
        self.assertEqual(add10(1), 11)
        self.assertEqual(self.seen, False)
        self.assertEqual(add10(2), 12)
        self.assertEqual(self.seen, True)

    def test_two(self):
        @memoize(dict, dict)
        def add(a, b):
            self.seen = True
            return a + b

        self.assertEqual(add(1, 1), 2)
        self.assertEqual(self.seen, True)
        self.seen = False
        self.assertEqual(add(1, 1), 2)
        self.assertEqual(self.seen, False)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(self.seen, True)
        self.assertEqual(add(2, 2), 4)

    def test_four(self):
        @memoize(dict, dict, dict, dict)
        def add(*args):
            self.seen = True
            return sum(args)

        self.assertEqual(add(1, 1, 1, 1), 4)
        self.assertEqual(self.seen, True)
        self.seen = False
        self.assertEqual(add(1, 1, 1, 1), 4)
        self.assertEqual(self.seen, False)
        self.assertEqual(add(1, 1, 1, 2), 5)
        self.assertEqual(self.seen, True)
        self.assertEqual(add(1, 1, 2, 2), 6)
        self.assertEqual(add(1, 2, 2, 2), 7)
        self.assertEqual(add(2, 2, 2, 2), 8)


def main():
    TestMemoize().run()


if __name__ == '__main__':
    main()