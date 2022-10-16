


import sys
sys.path.insert(0, '../../reynard')
import unittest
import math
from reynard import Reynard
from reynard_constants import letter_frequency,letter_frequency_wiki, most_common_first_letter_in_words


PZ1_WORD_COUNT= 41
PZ2_WORD_COUNT = 35

class TestOne(unittest.TestCase):
    '''
    Test Case one -- can we open and get
    1. Do our frequency tables add up to 1
    2. Can we read in the helper word lists
    '''
        
    def setUp(self):
        '''
        setup method for hte unit tests. 
        '''
        self.reynard = Reynard()
        self.reynard.readInPuzzle('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz2.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.reynard)
        


if __name__ == '__main__':
    unittest.main()