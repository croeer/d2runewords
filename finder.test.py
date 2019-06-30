import unittest
from finder import *

class RunewordTest(unittest.TestCase):
    def test_doubleRunes(self):
        rw = findRunewords(['sol','um','um'])
        self.assertEqual(rw, [{'Bone': "['Sol', 'Um', 'Um']"}])

    def test_doubleRunesPlusOne(self):
        rw = findRunewords(['sol','um','um','shael'])
        self.assertEqual(rw, [{'Bone': "['Sol', 'Um', 'Um']"}])

    def test_casing(self):
        rw = findRunewords(['NeF','tiR'])
        self.assertEqual(rw, [{'Nadir': "['Nef', 'Tir']"}])

    def test_singleRune(self):
        rw = findRunewords(['ral'])
        self.assertEqual(rw, [])

    def test_twoRunes(self):
        rw = findRunewords(['ral','ort'])
        self.assertEqual(rw, [])

if __name__ == '__main__':
    unittest.main()