


import sys
sys.path.insert(0, '../../reynard')
import unittest
import math
from reynard_puzzle import Puzzle
from reynard_constants import letter_frequency,letter_frequency_wiki, most_common_first_letter_in_words




class TestOne(unittest.TestCase):
    '''
    Test Case one -- can we open and get
    1. Do our frequency tables add up to 1
    2. Can we read in the helper word lists
    '''
        
    def setUp(self):
        '''
        setup method for the unit tests. 
        '''
        self.reynard = Puzzle('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz2.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.reynard)
        
    def testAandIMethod(self):
        '''
        This method tests for both A and I in a puzzle.  having both of these
        one letter words.
        '''
        self.assertTrue(self.reynard.bothAandI())

if __name__ == '__main__':
    unittest.main()