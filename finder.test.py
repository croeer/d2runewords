import unittest
from finder import *

class RunewordTest(unittest.TestCase):
    def test_doubleRunes(self):
        rw = findRuneworts(['tir', 'tir'])
        self.assertEqual(rw, ['Spirit'])

    def test_tripleRunes(self):
        rw = findRuneworts(['um','um','um'])
        self.assertEqual(rw, ['Spirit'])

    def test_casing(self):
        rw = findRuneworts(['oRt','Sol'])
        self.assertEqual(rw, ['Spirit'])

if __name__ == '__main__':
    unittest.main()