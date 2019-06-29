import unittest
from finder import *

class RunewordTest(unittest.TestCase):
    def test_doubleRunes(self):
        rw = findRuneworts(['tir','tir','vex'])
        self.assertEqual(rw, ['dummyDoppelt'])

    def test_tripleRunes(self):
        rw = findRuneworts(['um','um','um'])
        self.assertEqual(rw,['dummyUmUmUm'])

    def test_tripleRunesPlusOne(self):
        rw = findRuneworts(['um','um','um', 'uh'])
        self.assertEqual(rw,['dummyUmUmUm'])

    def test_casing(self):
        rw = findRuneworts(['TIR','SoL','etH'])
        self.assertEqual(rw, ['dummyGross'])

    def test_singleRune(self):
        rw = findRuneworts(['ral'])
        self.assertEqual(rw, [])

    def test_twoRunes(self):
        rw = findRuneworts(['ral','ort'])
        self.assertEqual(rw, [])

if __name__ == '__main__':
    unittest.main()