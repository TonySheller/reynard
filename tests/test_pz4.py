'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745


tests for the reynard concept
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

class TestPz4(unittest.TestCase):
    '''

    '''
    def setUp(self):
        '''
        setup method for hte unit tests. 
        '''
        self.puzzle = Puzzle(FILE_PATH+ '/data/pz4.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.puzzle)

        
    def testPz4MakeInitialGuess(self):
        '''
        pz4 does not have a one letter word in it
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.makeInitialGuess()
        self.assertEqual(0.0, agent.root.utility)
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),0)
        print("")
        
    def testPz4TwoLtWdsBeginWithAorI(self):

        agent = Agent(puzzle=self.puzzle)
        agent.makeInitialGuess()
        self.assertEqual(0.0, agent.root.utility)
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),0)
        agent.twoLtWdsBeginWithAorI()
        for child in agent.root.children:
            self.assertTrue(len(child.children)> 0)        

    
           
    def testPz4OtherTwoLetterWords(self):
        agent = Agent(puzzle=self.puzzle)
        agent.makeInitialGuess()
        self.assertGreaterEqual(agent.root.utility,0.0)
        
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),0)  
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)
        
        agent.twoLtWdsBeginWithAorI()
        iter = agent.puzzle.pz_word_lengths_freqeuncy[2]
        for i in range(10):
            agent.recurseDownTryTwoLtWds(agent.root, two_letter_word_frequency)
            print("Iteration {}".format(i))
                

        for node in agent.high_node:
            print("word {} to {}".format(node.word,node.word_pz))
        
        print("pause") 

        
if __name__ == '__main__':
    unittest.main()