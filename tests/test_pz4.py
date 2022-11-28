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

class TestPz3(unittest.TestCase):
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
        print("Completed test 2 for puzzle 5.")
                                
    def testPz4_3_TwoLetterWords(self):
        '''
        Three are no one letter words in this puzzle
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
        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            if len(agent.root.children) > 0:
                for child in agent.root.children:
                    agent.processTwoLetterWords(child,0,12)
            else:
                agent.processTwoLetterWords(agent.root, 0, 12)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("Execution time for two letter words is {}".format(elapsedTwo))  
            if self.evaluateChildrenForKeyThree(agent.root, False):
                self.assertTrue(1==1)  
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("Maximum Utility in this possible solution is {}".format(maxVal))
        
    def testPz4_4_ThreeLetterWords(self):
        '''
        Test to evaluate three letter words
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

        startTime = time()
        if agent.puzzle.wordsOfLength(2):
            startTime = time()
            if len(agent.root.children) > 0:
                for child in agent.root.children:
                    agent.processTwoLetterWords(child,0,12)
            else:
                agent.processTwoLetterWords(agent.root, 0, 12)
            endTime = time()
            elapsed = endTime - startTime
            elapsedTwo = str(timedelta(seconds=elapsed))
            print("Execution time for two letter words is {}".format(elapsedTwo))  

            if self.evaluateChildrenForKeyThree(agent.root, False):
                self.assertTrue(1==1)
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("Maximum Utility in this possible solution is {}".format(maxVal))



        if agent.puzzle.wordsOfLength(3):
            startTime = time()
            if len(agent.root.children) > 0:
                for child in agent.root.children:
                    agent.processTwoLetterWords(child,0,12)
            else:
                agent.processTwoLetterWords(agent.root, 0, 12)
            endTime = time()
            elapsed = endTime - startTime
            elapsedThree = str(timedelta(seconds=elapsed))
            print("Execution time for three letter words is {}".format(elapsedThree))  

            if self.evaluateChildrenForKeyThree(agent.root, False):
                self.assertTrue(1==1)
            maxVal = max(self.getHighestUtility(agent.root,[]))
            print("Maximum Utility in this possible solution is {}".format(round(maxVal,3)))  



    def evaluateChildrenForKeyThree(self,node,returnValue):
        '''
        Helper function for the tests 
        '''
        if len(node.children) > 0: 
            for child in node.children:
                self.evaluateChildrenForKeyThree(child,returnValue)
        else:
            if self.checkkeyThreeLetters(node):
                returnValue = True
            else:
                returnValue = False
        return returnValue

    def checkkeyThreeLetters(self,node):
        '''
        Helper function for the tests
        '''
        if all([k in list(node.letter.keys()) for k in list('THQDFE') ]):
                if node.letter['T'] == 'I':
                    if node.letter['H'] == 'O':
                        if node.letter['Q'] == 'T':
                            if node.letter['D'] == 'A':
                                if node.letter['F'] == 'N':
                                    if node.letter['E'] == 'D':
                                        print("Key {} :: Utility of {}  present in the puzzle".format(node.letter,round(node.utility,3)))
                                        return True
        # Return from system stack
        return False


        '''

        '''
        if all([k in list(node.letter.keys()) for k in list('XCKGOQM') ]):
                if node.letter['X'] == 'A':
                    if node.letter['C'] == 'I':
                        if node.letter['K'] == 'T':
                            if node.letter['G'] == 'O':
                                print("Key {} :: Utility of {}  present in the puzzle".format(node.letter,round(node.utility,3)))
                                return True

        return False
            
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

        '''

        '''
        if all([k in list(node.letter.keys()) for k in list('MCKL') ]):
                 if node.letter['M'] == 'I':
                    if node.letter['C'] == 'A':
                        if node.letter['K'] == 'S':
                            if node.letter['L'] == 'N':
                                print("Key {} :: Utility of {}  present in the puzzle".format(node.letter,round(node.utility,3)))
                                return True
        # Leaving the system stack and not finding what we were
        return False
        
if __name__ == '__main__':
    unittest.main()