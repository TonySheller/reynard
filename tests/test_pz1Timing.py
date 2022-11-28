'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745


Tests For Reynard
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
from time import time,sleep
from datetime import timedelta

FILE_PATH = '../reynard'

class TestPz1Timing(unittest.TestCase):
    '''
    One set of tests for Puzzle 1

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
   
    def testPz1_4_TwoLetterWords(self):
        '''

        '''
        agent = Agent(puzzle=self.puzzle)
        #print("Turning off verbosity for timing measurements")
        if agent.VERBOSE:
            agent.VERBOSE = not agent.VERBOSE
        print("\n4 Words")
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
        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            for child in agent.root.children:
                agent.processTwoLetterWords(child,0,4)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("4 Words -- Execution time for two letter words is {}".format(elapsedTwo))  
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("4 Words -- Maximum Utility is {}".format(round(maxVal,3)))
            print("4 Words -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, returnValue = False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue =False)

    def testPz1_5_TwoLetterWords(self):
        '''
        '''
        agent = Agent(puzzle=self.puzzle)
        #print("Turning off verbosity for timing measurements")
        if agent.VERBOSE:
            agent.VERBOSE = not agent.VERBOSE
        print("\n5 Words")
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
        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            for child in agent.root.children:
                agent.processTwoLetterWords(child,0,5)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("5 Words -- Execution time for two letter words is {}".format(elapsedTwo))  

            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("5 Words -- Maximum Utility is {}".format(round(maxVal,3)))
            print("5 Words -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue =False)

    def testPz1_6_TwoLetterWords(self):
        '''
        This tries other two letter

        '''
        agent = Agent(puzzle=self.puzzle)
        #print("Turning off verbosity for timing measurements")
        if agent.VERBOSE:
            agent.VERBOSE = not agent.VERBOSE
        print("\n6 Words")
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
        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            for child in agent.root.children:
                agent.processTwoLetterWords(child,0,6)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("6 Words -- Execution time for two letter words is {}".format(elapsedTwo))  
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("6 Words -- Maximum Utility is {}".format(round(maxVal,3)))
            print("6 Words -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue =False)

    def testPz1_7_TwoLetterWords(self):
        '''
        This tries other two letter
        '''
        agent = Agent(puzzle=self.puzzle)
        #print("Turning off verbosity for timing measurements")
        if agent.VERBOSE:
            agent.VERBOSE = not agent.VERBOSE
        print("\n7 Words")
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
        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            for child in agent.root.children:
                agent.processTwoLetterWords(child,0,7)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("7 Words -- Execution time is {}".format(elapsedTwo))  

            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("7 Words -- Maximum Utility is {}".format(round(maxVal,3)))
            print("7 Words -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue = False)

    def testPz1_8_TwoLetterWords(self):
        '''
        This tries other two letter
        '''
        agent = Agent(puzzle=self.puzzle)
        #print("Turning off verbosity for timing measurements")
        if agent.VERBOSE:
            agent.VERBOSE = not agent.VERBOSE
        print("\n8 Words")
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
        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            for child in agent.root.children:
                agent.processTwoLetterWords(child,0,8)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("8 Words -- Execution time is {}".format(elapsedTwo))  

            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("8 Words -- Maximum Utility is {}".format(round(maxVal,3)))
            print("8 Words -- Node Count at {}".format(agent.node_count))
            self.evaluateChildrenForKey(agent.root, False)
            self.evaluateChildrenForKeyThree(agent.root,returnValue = False)

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
        if all([k in list(node.letter.keys()) for k in list('XCKG') ]):
                if node.letter['X'] == 'A':
                    if node.letter['C'] == 'I':
                        if node.letter['K'] == 'T':
                            if node.letter['G'] == 'O':
                                print("\n\tKey {} :: \n\tUtility of {} present in the puzzle".format(node.letter,round(node.utility,3)))
        # Leaving the system stack and not finding what we were
        return returnVal

    def checkkeyMoreLetters(self,node):
        '''
        Helper function for the tests
        '''
        returnVal = False
        if all([k in list(node.letter.keys()) for k in list('XCKGQM') ]):
                if node.letter['X'] == 'A':
                    if node.letter['C'] == 'I':
                        if node.letter['K'] == 'T':
                            if node.letter['G'] == 'O':
                                if node.letter['Q'] == 'M':
                                    if node.letter['M'] == 'E':
                                        print("\n\tBigger Key {} :: \n\tUtility of {}  present in the puzzle".format(node.letter,round(node.utility,3)))
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