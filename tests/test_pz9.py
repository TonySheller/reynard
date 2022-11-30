'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745


tests for the reynard Reasoning over Cryptograms Project
'''
import sys,os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import unittest
import math

from reynard_constants import *
from agent import Agent
from puzzle import Puzzle
import threading
from itertools import combinations, permutations


FILE_PATH = '../reynard'
class TestPz9(unittest.TestCase):
    '''

    '''
    def setUp(self):
        '''
        setup method for hte unit tests. 
        '''
        self.puzzle = Puzzle(FILE_PATH+ '/data/pz9.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.puzzle)

        
    def testPz9MakeInitialGuess(self):
        '''
        For puzzle 8 there are no one letter words
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
        self.assertGreaterEqual(agent.root.utility,0.0 )
        # 
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),0)

        
    def testPz9TwoLtWdsBeginWithAorI(self):
        '''
        For puzzle 8 there are no one letter words
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
        self.assertGreaterEqual(agent.root.utility,0.0 )
        # 
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),0)
        agent.twoLtWdsBeginWithAorI()
        

        
if __name__ == '__main__':
    unittest.main()