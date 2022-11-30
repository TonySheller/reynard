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
from time import time,sleep
from datetime import timedelta

FILE_PATH = '../reynard'

class TestPz4(unittest.TestCase):
    '''

    '''
    def setUp(self):
        '''
        setup method for hte unit tests. 
        '''
        self.puzzle = Puzzle(FILE_PATH + '/data/pz4.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.puzzle)


        
    def testPz4_1_MakeInitialGuess(self):
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
        self.assertEqual(len(agent.root.children),0)
        agent.twoLtWdsBeginWithAorI()  
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)
        
        print("Completed Test 1 for Puzzle 4")
        
    def testPz4_2_WordsBeginWithAorI(self):
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
        self.assertGreaterEqual(agent.root.utility,0.0)
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),0)  
        agent.twoLtWdsBeginWithAorI()
        for child in agent.root.children:
            self.assertTrue(len(child.children)>= 0)
        print("Completed test 2 for puzzle 4.")
                            
    def testPz4_4_ThreeLetterWords(self):
        '''
        Test to evaluate three letter words
        '''
        
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
        self.assertEqual(0.0, agent.root.utility)
        self.agent = agent
        agent.VERBOSE = False
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),0)
        agent.twoLtWdsBeginWithAorI()  
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)

        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            if len(agent.root.children) == 0:
                agent.processTwoLetterWords(agent.root,0,14)
            
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("Puzzle 4 -- Execution time for two letter words is {}".format(elapsedTwo))  
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("Puzzle 4 -- Maximum Utility is {}".format(round(maxVal,3)))
            print("Puzzle 4  -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue =False) 
        if agent.puzzle.wordsOfLength(3):
            startTime = time()
            agent.processThreeLetterWords(agent.root, 0, 7)
 

            endTime = time()
            elapsed = endTime - startTime
            elapsedThree = str(timedelta(seconds=elapsed))
            print("Puzzle 4 -- Execution time for three letter words is {}".format(elapsedTwo))  
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("Puzzle 4 -- Maximum Utility is {}".format(round(maxVal,3)))
            print("Puzzle 4  -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue =False)


    def evaluateChildrenForKey(self,node,returnValue):
        '''
        Helper function for the tests 
        '''
        if len(node.children) > 0: 
            for child in node.children:
                self.evaluateChildrenForKey(child,returnValue)
        else:
           returnValue = self.checkkeyTwoLetters(node)
        return returnValue

    def evaluateChildrenForKeyThree(self,node,returnValue):
        '''
        Helper function for the tests 
        '''
        if len(node.children) > 0: 
            for child in node.children:
                self.evaluateChildrenForKeyThree(child,returnValue)
        else:
           returnValue = self.checkkeyMoreLetters(node)
        return returnValue       

    def checkkeyTwoLetters(self,node):
        '''
        Helper function for the tests
        '''
        returnVal = False
        if all([k in list(node.letter.keys()) for k in list('CLMXE') ]):

            if node.letter['M'] == 'T':
                if node.letter['X'] == 'O':
                    print("\n\tKey {} :: \n\tUtility of {} present in the puzzle\n".format(node.letter,round(node.utility,3)))
                    self.agent.showProgressPuzzle(node)
        # Leaving the system stack and not finding what we want
        return returnVal

    def checkkeyMoreLetters(self,node):
        '''
        Helper function for the tests
        '''
        returnVal = False
        if all([k in list(node.letter.keys()) for k in list('MXPL') ]):
            if node.letter['M'] == 'T':
                if node.letter['X'] == 'O':
                    if node.letter['P'] == 'H':
                        if node.letter['L'] == 'E':
                            print("\n\tKey {} :: \n\tUtility of {} present in the puzzle\n".format(node.letter,round(node.utility,3)))
                            self.agent.showProgressPuzzle(node)
        # Leaving the system stack and not finding what we were
        return returnVal

    def getHighestUtility(self,node,maxVal=[]):
        '''
        What is the highest utility in the tree
        '''
        if len(node.children) > 0: 
            for child in node.children:
                self.getHighestUtility(child,maxVal)    
        else:
            maxVal.append(node.utility)
        return maxVal




if __name__ == '__main__':
    unittest.main()