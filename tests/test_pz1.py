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

class TestSetFour(unittest.TestCase):
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

        
    def testpz1GetActionsOneLetter(self):
        '''
        Evaluate getting the actions
        '''
       
        agent = Agent(self.puzzle)
        # The agent will create a puzzle for itself. The MCTS will do the same
        #actions =[]
        if 1 in self.puzzle.pz_word_lengths_freqeuncy.keys():
            actions = agent.getPossibleActions(['A','I'],agent.root)
            
        self.assertEqual(len(actions), 2)
        
        
    def testpz1TakeActionsOneLetter(self):
        '''
        Evaluate Taking the actions
        '''
        agent = Agent(self.puzzle)
        # The agent will create a puzzle for itself. The MCTS will do the same
        #actions =[]
        if 1 in self.puzzle.pz_word_lengths_freqeuncy:
            actions = agent.getPossibleActions(['A','I'],agent.root)
            self.assertEqual(len(actions), 2)
            for action in actions:
                agent.takeAction(action,agent.root)

        self.assertTrue(len(agent.root.children) == 2)           


    def test_twoLetterWords(self):
        agent = Agent(self.puzzle)
        if 1 in self.puzzle.pz_word_lengths_freqeuncy:
            actions = agent.getPossibleActions(['A','I'],agent.root)
            self.assertEqual(len(actions), 2)
            for action in actions:
                agent.takeAction(action,agent.root)

            self.assertTrue(len(agent.root.children) == 2)           
        ## Assume we did the one letter word thing
        
        if 2 in self.puzzle.pz_word_lengths_freqeuncy:
            actions = agent.getPossibleActions(two_letter_word_frequency,agent.root)
            print("pausing")
            for mAction in actions:
                if mAction[0].x == 'IT' and mAction[0].y == 'CK':
                    if mAction[1].x == 'OF' and mAction[1].y == 'GH':
                        if mAction[2].x == 'TO' and mAction[2].y == 'KG':
                            if mAction[3].x == 'ME' and mAction[3].y == 'QM':
                                self.assertEqual(1, 1)               
            # MK = IS
            # ML = TO
            # QM = ME
            # GH = OF    
                     
            #for child in agent.root.children:
            #    for action in actions:
            #        agent.takeAction(action, child)

if __name__ == '__main__':
    unittest.main()