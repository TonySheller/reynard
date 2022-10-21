'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745


tests for the reynard_bn module
'''
import sys
sys.path.insert(0, '../../reynard')
import unittest
import math

from reynard_constants import letter_frequency,letter_frequency_wiki, most_common_first_letter_in_words

from reynard_bn import ReynardBN

class TestSetFour(unittest.TestCase):
    '''

    '''
        
    def testReynardBNConstruct(self):
        '''

        '''
        RBN = ReynardBN()
        RBN.add_letterFrequencyNode("First Letter", "the First Letter")
        RBN
        pass


if __name__ == '__main__':
    unittest.main()