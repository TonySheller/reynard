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
from string import ascii_uppercase
FILE_PATH = '../reynard'

class TestPz1(unittest.TestCase):
    '''

    '''
    def setUp(self):
        '''
        setup method for The unit tests. 
        This runs before each test
        '''
        self.puzzle = Puzzle(FILE_PATH + '/data/pz1.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.puzzle)

        
    def testPz1MakeInitialGuess(self):
        '''
        We should have a root node and two children nodes
        who don't have any children.
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
        self.assertEqual(0.0, agent.root.utility)
        
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)
        agent.twoLtWdsBeginWithAorI()  
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)
        a=1
        
        
    def testPz1OtherTwoLetterWords(self):
        '''
        This tries other two letter words but its not useful
        becasue pz2's only two letter words begin with I (IS, IN)
        
        Thre 
        '''
        
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
        self.assertEqual(0.0, agent.root.utility)
        
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)
        agent.twoLtWdsBeginWithAorI()  
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)
        for i in range(4): 
            agent.traverseTree(agent.root, two_letter_word_frequency)
            self.checkChildren(agent.root)
        
        print("pause")    

    def checkChildren(self,node):
        '''
        Method to check that the first moves have not been overwritten down
        the tree some where.
        '''
        if node.parent == None and len(node.children) > 0:
            for child in node.children:
                self.checkChildren(child)
        elif node.parent.parent == None and len(node.children) > 0:
            for child in node.children:
                self.checkChildren(child)
        else:
            for i in range(len(node.parent.game_state)):
                if node.parent.game_state[i] in ascii_uppercase:
                    self.assertEqual(node.parent.game_state[i],node.game_state[i])
    

            

            
                

if __name__ == '__main__':
    unittest.main()