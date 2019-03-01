import unittest
from .test_trie_memoize import TestMemoize


def main():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMemoize)
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    main()