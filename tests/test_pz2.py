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

class TestPz2(unittest.TestCase):
    '''

    '''
    def setUp(self):
        '''
        setup method for hte unit tests. 
        '''
        self.puzzle = Puzzle('/home/asheller/reynard/data/pz2.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.puzzle)

        
    def testPz2MakeInitialGuess(self):
        agent = Agent(puzzle=self.puzzle)
        agent.makeInitialGuess()
        self.assertGreater(agent.root.utility,0.0)
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)
        print("")
        

        
if __name__ == '__main__':
    unittest.main()