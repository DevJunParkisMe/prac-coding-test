import unittest
from src.dfs import ice
from src.bfs_words import word_conversion
from src.bfs import shortest
class TestDFSBFS(unittest.TestCase):
    def test_ice(self):
        m = [[0,0,1,1,0],
             [0,0,0,1,1],
             [1,1,1,1,1],
             [0,0,0,0,0]]
        
        self.assertEqual(ice(m),3)

    def test_word_conversion(self):
        begin = "hit"
        target = "cog"
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(word_conversion(begin,target,words), 4)

    def test_short(self):
        n = 6
        edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
        self.assertEqual(shortest(n, edge),3)