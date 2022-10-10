'''
For the lack of a creative name, just testOne
'''
import sys
sys.path.insert(0, '../../reynard')
import unittest
import math
from reynard import Reynard
from reynard_constants import letter_frequency,letter_frequency_wiki, most_common_first_letter_in_words

PZ1_WORD_COUNT= 41


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
        pass
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        pass
        
    def testLetterFreqIsOne(self):
        '''
        Test the letter frequencies = 1
        Iterate through to ensure the letter frequency dictionary sums to one
        '''
        lf = letter_frequency
        sum = 0
        for i in lf.keys():
            sum += lf[i]
        self.assertEqual(1, round(sum,4))
        
    def testLetterFreqWikiIsOne(self):
        '''
        Test the letter frequencies Wiki = 1
        Iterate through to ensure the letter frequency wiki dictionary sums to one
        '''
        lf = letter_frequency_wiki
        sum = 0
        for i in lf.keys():
            sum += lf[i]
        self.assertEqual(1, round(sum,4))

    def test_first_letter_in_words_list(self):
        '''
        Test that the string converts to a list
        '''
        mc1w = most_common_first_letter_in_words
        self.assertEqual(type(mc1w), list)
        
    def test_reynard_read_in(self):
        '''
        Test reading in the puzzle string.
        This test is specific to pz1.txt
        '''
        reynard = Reynard()
        reynard.readInPuzzle('../data/pz1.txt')
        self.assertEqual(217, len(reynard.pz_as_string))
        
    def test_reynard_word_count_with_punctuation(self):
        '''
        Test the word count not splitting out the punctuation
        '''  
        reynard = Reynard()
        reynard.readInPuzzle('../data/pz1.txt')
        reynard.wordsWithPunctuation()
        self.assertEqual(46, len(reynard.pz_words_as_array_with_punctuation))

    def test_reynard_word_count_without_punctuation(self):
        '''
        Test the word count not splitting out the punctuation
        '''  
        reynard = Reynard()
        reynard.readInPuzzle('../data/pz1.txt')
        reynard.wordsWithoutPunction()
        print(reynard.pz_words_as_array_without_punctuation)
        self.assertEqual(41, len(reynard.pz_words_as_array_without_punctuation))
    
    def test_reynard_letter_count(self):
        '''
        Need to get a frequency count of the letters
        '''
        reynard = Reynard()
        reynard.readInPuzzle('../data/pz1.txt')
        reynard.letterFrequency()
        
        
    def test_for_apostrophe_words(self):
        pass
        
if __name__ == '__main__':
    unittest.main()