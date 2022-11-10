'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745


tests for the reynard mcts concept
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

class TestPz1(unittest.TestCase):
    '''

    '''
    def setUp(self):
        '''
        setup method for hte unit tests. 
        '''
        self.puzzle = Puzzle('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz1.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.puzzle)

        
    def testPz1MakeInitialGuess(self):
        puzzle = Puzzle('data/pz1.txt')
        agent = Agent(puzzle=puzzle)
        agent.makeInitialGuess()
        self.assertEqual(0.0, agent.root.utility)
        for ltr in ['A','I']:
            agent.assignAorI(agent.root, ltr)
        self.assertEqual(len(agent.root.children),2)
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)
        
if __name__ == '__main__':
    unittest.main()