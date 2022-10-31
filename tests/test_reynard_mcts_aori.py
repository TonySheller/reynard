'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745


tests for the reynard mcts concept
'''
import sys
sys.path.insert(0, '../../reynard')
import unittest
import math

from reynard_constants import *
from reynard_agent import Agent

class TestSetFour(unittest.TestCase):
    '''

    '''
        
    def testpz1(self):
        '''
        will it run against the various puzzles
        '''
        agent = Agent('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz1.txt')
        # The agent will create a puzzle for itself. The MCTS will do the same
        action = agent.oneLetterWords()
        print("Action is {} utility value is {}".format(action,action.utility))
        if hasattr(action,'joint_action' ):     
            print("Joint Action is {} utility value is {}".format(action.joint_action))
             
        self.assertEqual(action.x,'X')
        self.assertEqual(action.y,'A')
        agent = None

    def testpz2(self):
        '''
        will it run against the various puzzles
        '''
        agent = Agent('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz2.txt')
        # The agent will create a puzzle for itself. The MCTS will do the same
        action = agent.oneLetterWords()
        print("Action is {} utility value is {}".format(action,action.utility))
        if hasattr(action,'joint_action' ):     
            print("Joint Action is {} utility value is {}".format(action.joint_action))
        self.assertEqual(action.x,'M')
        self.assertEqual(action.y,'I')
        agent = None

if __name__ == '__main__':
    unittest.main()