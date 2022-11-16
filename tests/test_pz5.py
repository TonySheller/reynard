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
class TestPz5(unittest.TestCase):
    '''

    '''
    def setUp(self):
        '''
        setup method for the unit tests. 
        '''
        self.puzzle = Puzzle(FILE_PATH+ '/data/pz5.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.puzzle)

        
    def testPz5MakeInitialGuess(self):
        '''
        For puzzle 5 we start with a correct guess of 0.07894
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.makeInitialGuess()
        self.assertGreaterEqual(agent.root.utility,0.0 )
        # 
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)

    def testPz5TwoLtWordBeginsWithAorI(self):
        '''
        For puzzle 5 we start with a correct guess of 0.07894
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.makeInitialGuess()
        #self.assertGreaterEqual(agent.root.utility,0.0 )
        # 
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)        
        agent.twoLtWdsBeginWithAorI()
        for child in agent.root.children:
            self.assertTrue(len(child.children)> 0)

           
    def testPz5OtherTwoLetterWords(self):
        agent = Agent(puzzle=self.puzzle)
        agent.makeInitialGuess()
        self.assertGreaterEqual(agent.root.utility,0.0)
        
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)  
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)
        
        agent.twoLtWdsBeginWithAorI()
        iter = agent.puzzle.pz_word_lengths_freqeuncy[2]
        for i in range(iter):
            agent.recurseDownTryTwoLtWds(agent.root, two_letter_word_frequency)
            print("Pause first")
                
        print("pause")     


if __name__ == '__main__':
    unittest.main()