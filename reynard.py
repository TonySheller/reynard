'''
Reynard is an agent that uses reasoning to solve cryptograms. 

Anthony Sheller
Reasoning Under Uncertainty
EN.605.7

'''

import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
import reynard_constants


class Reynard:
    
    def __init__(self):
        '''
        Constructor for Reynard
        '''
        pass
    
    def __del__(self):
        '''
        Destructor for Reynard
        In case I need to do some cleaning up.
        '''
        pass
        
        
    def readInPuzzle(self,puzzleFile):
        '''
        Method to read in the puzzle provided at the command line
        '''
        with open(puzzleFile,'r') as f:
            self.pz_as_string = f.read()

    def wordsWithPunctuation(self):
        '''
        Method that splits text into words with punctuiona. 
        '''
        self.pz_words_as_array_with_punctuation = nltk.word_tokenize(self.pz_as_string)
    
    def wordsWithoutPunction(self):
        '''
        Method to get all words without punctuation
        '''
        tokenizer = RegexpTokenizer(r'\w+')
        self.pz_words_as_array_without_punctuation = tokenizer.tokenize(self.pz_as_string)
        
    def letterFrequency(self):
        '''
        Method to get the frequency count of letters in the puzzle
        '''
        self.pz_letter_freqeuncy = {}
        # If it doesn't exist then create it
        if not hasattr(self, 'pz_words_as_array_without_punctuation'):
            self.wordsWithoutPunction()
        for word in self.pz_words_as_array_without_punctuation:
            for char in word:
                if char not in self.pz_letter_freqeuncy and char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    self.pz_letter_freqeuncy[char] = 0
                self.pz_letter_freqeuncy[char] += 1
        print(self.pz_letter_freqeuncy)
        
        
    def wordsWithApostrophes(self):
        pass

def main():
    '''
    Non class function used to create the class and run it. 
    '''
    pass

if __name__ == "__main__":
    pass
