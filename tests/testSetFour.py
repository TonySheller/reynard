'''
This group of tests evaluates the constructor and other more complex tasks
that take place after Reynard is constructed
'''
import sys
sys.path.insert(0, '../../reynard')
import unittest
import math
from reynard_puzzle import Puzzle
from reynard_constants import letter_frequency,letter_frequency_wiki, most_common_first_letter_in_words
from reynard_reasoner import Reasoner


class TestSetFour(unittest.TestCase):
    '''

    '''
        
    def testReynardConstructorNoArguments(self):
        '''

        '''
        self.reynard = Puzzle()
        self.assertTrue(not hasattr(self.reynard,'pz_words_as_array_without_punctuation' )) 
        self.assertTrue(not hasattr(self.reynard,'pz_words_as_array_with_punctuation' )) 
        self.assertTrue(not hasattr(self.reynard,'pz_words_as_array_without_punctuation' )) 
        self.assertTrue(not hasattr(self.reynard,'pz_as_string' )) 
        self.assertTrue(not hasattr(self.reynard,'word_lengths_freqeuncy' )) 
        self.assertTrue(not hasattr(self.reynard,'apostophe_words' )) 

    def testReynardConstructorWithArguments(self):
        '''

        '''
        self.reynard = Puzzle('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz1.txt')
        self.assertTrue(hasattr(self.reynard,'pz_words_as_array_without_punctuation' )) 
        self.assertTrue(hasattr(self.reynard,'pz_words_as_array_with_punctuation' )) 
        self.assertTrue(hasattr(self.reynard,'pz_words_as_array_without_punctuation' )) 
        self.assertTrue(hasattr(self.reynard,'pz_as_string' )) 
        self.assertTrue(hasattr(self.reynard,'word_lengths_freqeuncy' )) 
        self.assertTrue(hasattr(self.reynard,'apostophe_words' )) 

    def testReasoner1(self):
        '''
        '''
        self.puzzle = Puzzle('/mnt/e/OneDrive - Johns Hopkins/EN.605.745/reynard/data/pz1.txt')
        self.reasoner = Reasoner()
        self.reasoner.createWordSearcher(self.puzzle.word_lengths_freqeuncy.keys())
        
        re_exp = '^[Aa].+$'
        self.reasoner.getWordsWithGivenPattern(re_exp,3)
        print("pause")
        
    
        

if __name__ == '__main__':
    unittest.main()