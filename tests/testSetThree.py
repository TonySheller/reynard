


import sys
sys.path.insert(0, '../../reynard')
import unittest
import math
from reynard import Reynard
from reynard_constants import letter_frequency,letter_frequency_wiki, most_common_first_letter_in_words


PZ1_WORD_COUNT= 41
PZ2_WORD_COUNT = 35
PZ3_WORD_COUNT = 0

class TestSetThree(unittest.TestCase):
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
        self.reynard.readInPuzzle('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz3.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.reynard)
        
    def test_for_apostrophe_words(self):
        '''
        Because pz3 has an apostrophe word in it, we can test that.
        '''
        self.reynard.isThereApostrophes()
        self.assertEqual(1,self.reynard.apostophe_words)


if __name__ == '__main__':
    unittest.main()