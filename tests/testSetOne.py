'''
For the lack of a creative name, just testSetOne

These tests will use pz1.txt as the puzzle so the metrics are from it. 

'''
import sys
sys.path.insert(0, '../../reynard')
import unittest
import math
from reynard_puzzle import Puzzle
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
        self.reynard = Puzzle()
        self.reynard.readInPuzzle('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz1.txt')
    
    def tearDown(self):
        '''
        tear down what was setup.
        '''
        del(self.reynard)
        
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

    def testFirstLetterInWordsList(self):
        '''
        Test that the string converts to a list
        '''
        mc1w = most_common_first_letter_in_words
        self.assertEqual(type(mc1w), list)
        
    def testReynardReadIn(self):
        '''
        Test reading in the puzzle string.
        This test is specific to pz1.txt
        '''
        self.assertEqual(217, len(self.reynard.pz_as_string))
        
    def testReynardCordCountWithPunctuation(self):
        '''
        Test the word count not splitting out the punctuation
        '''  
        self.reynard.wordsWithPunctuation()
        self.assertEqual(46, len(self.reynard.pz_words_as_array_with_punctuation))

    def testReynardWordCountWithoutPunctuation(self):
        '''
        Test the word count not splitting out the punctuation
        '''  
        self.reynard.wordsWithoutPunction()
        self.assertEqual(41, len(self.reynard.pz_words_as_array_without_punctuation))
    
    def testReynardLetterCount(self):
        '''
        Need to get a frequency count of the letters
        '''
        self.reynard.letterFrequency()
        self.assertEqual(24, len(self.reynard.pz_letter_freqeuncy.keys()))

        
    def testWordLengthFrequency(self):
        '''
        Confirm word_lengths_frequency works
        '''
        self.reynard.wordLengthsFrequency()
        self.assertEqual(9, len(self.reynard.word_lengths_freqeuncy))
        
        
    def testBlankPuzzle(self):
        '''
        Confirm blank puzzle matches original
        '''
        self.reynard.generateBlankPuzzle()
        #print(self.reynard.pz_as_string)
        #print("\n\n")
        #print(self.reynard.blank_puzzle)
        self.assertEqual(len(self.reynard.pz_as_string), len(self.reynard.blank_puzzle))
        
    def testDoubleLetterWords(self):
        '''
        Evaluate method for checking if there are double letter words
        
        '''
        self.reynard.checkForDoubleLetters()
        self.assertEqual(3, self.reynard.double_letter_words)
        
        
if __name__ == '__main__':
    unittest.main()