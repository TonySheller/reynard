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

from itertools import combinations, permutations
from time import time,sleep
from datetime import timedelta


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

        
    def testPz5_1_MakeInitialGuess(self):
        '''
        For puzzle 5 we start with a correct guess of 0.07894
        '''
        print("Puzzle 5")
        print("Puzzle")
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
        self.assertGreaterEqual(agent.root.utility,0.0 )
        # 
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)

    def testPz5_2_TwoLtWordBeginsWithAorI(self):
        '''
        For puzzle 5 we start with a correct guess of 0.07894
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.startPuzzle()
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

         
    def testPz1_2_TwoLetterWords(self):
        '''
        This tries other two letter words
        '''
        agent = Agent(puzzle=self.puzzle)
        agent.VERBOSE = True
        self.agent = agent
        agent.startPuzzle()
        self.assertEqual(0.0, agent.root.utility)
        print("Puzzle 5 -- Test 2 -- Two Letter Words")
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(agent.root, ['A','I'])
        self.assertEqual(len(agent.root.children),2)
        agent.twoLtWdsBeginWithAorI()  
        for child in agent.root.children:
            self.assertTrue(child.utility >= agent.root.utility)
        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            for child in agent.root.children:
                agent.processTwoLetterWords(child,0,5)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("Puzzle 1 -- test 2 -- Execution time for two letter words is {}".format(elapsedTwo))  
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("Puzzle 1 -- test 2 -- Maximum Utility is {}".format(round(maxVal,3)))
            print("Puzzle 1 -- test 2 -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue =False)

        if agent.puzzle.wordsOfLength(3):
            startTime = time()
            for child in agent.root.children:
                agent.processThreeLetterWords(child,0,5)
            endTime = time()
            elapsed = endTime - startTime
            elapsedThree = str(timedelta(seconds=elapsed))
            print("Puzzle 3 -- test 4 -- Execution time for Three letter words is {}".format(elapsedTwo))  
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("Puzzle 3 -- test 4 -- Maximum Utility is {}".format(round(maxVal,3)))
            print("Puzzle 3 -- test 4 -- Node Count at {}".format(agent.node_count))
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
        if all([k in list(node.letter.keys()) for k in list('CG') ]):

            if node.letter['C'] == 'I':
                if node.letter['G'] == 'T':
                    print("\n\tKey {} :: \n\tUtility of {} present in the puzzle\n".format(node.letter,round(node.utility,3)))
                    self.agent.showProgressPuzzle(node)
        # Leaving the system stack and not finding what we want
        return returnVal

    def checkkeyMoreLetters(self,node):
        '''
        Helper function for the tests
        '''
        returnVal = False
        if all([k in list(node.letter.keys()) for k in list('CGRM') ]):
            if node.letter['C'] == 'I':
                if node.letter['G'] == 'T':
                    if node.letter['R'] == 'A':
                        if node.letter['M'] == 'N':
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