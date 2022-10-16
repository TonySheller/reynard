'''
Reynard is an agent that uses reasoning to solve cryptograms. 

Anthony Sheller
Reasoning Under Uncertainty
EN.605.745

'''

import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
import reynard_constants
import os
import collections



class Puzzle:
    
    def __init__(self,puzzleFile=None):
        '''
        Constructor for Reynard that does nothing
        This is useful in testing each method indivudually.
        '''
        if not puzzleFile:
            pass
        else:
            self.readInPuzzle(puzzleFile)
            self.wordsWithPunctuation()
            self.wordsWithoutPunction()
            self.isThereApostrophes() 
            self.letterFrequency()
            self.wordLengthsFrequency()
            self.generateBlankPuzzle()
            
        
        
    def readInPuzzle(self,puzzleFile):
        '''
        Method to read in the puzzle provided at the command line
        '''
        with open(puzzleFile,'r') as f:
            self.pz_as_string = f.read()
            self.pz_array = []
            # Need to take out the name in the cryptogram as its impacting frequency counts
            temp = ''
            for ch in self.pz_as_string:
                if ch == '(':
                    break
                else:
                    temp += ch
            self.pz_as_string = temp
            for char in self.pz_as_string:
                self.pz_array.append(char)

    def wordsWithPunctuation(self):
        '''
        Method that splits text into words with punctuiona. 
        '''
        self.pz_words_as_array_with_punctuation = nltk.word_tokenize(self.pz_as_string)
    
    def wordsWithoutPunction(self):
        '''
        Method to get all words without punctuation
        Note May want to figure out how to leave apostrophes in.
        '''
        tokenizer = RegexpTokenizer(r'\w+') ## Consider leaving apostrophes in
        self.pz_words_as_array_without_punctuation = tokenizer.tokenize(self.pz_as_string)
        
    def letterFrequency(self):
        '''
        Method to get the frequency count of letters in the puzzle
        It sets the self.pz_letter_frequency attribute
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
        
    def wordLengthsFrequency(self):
        '''
        Method to get a frequency count of word lengths
        It sets the self.pz.len_words_frequency attribute
        '''
        self.word_lengths_freqeuncy = {}
        # If it doesn't exist then create it
        if not hasattr(self, 'pz_words_as_array_without_punctuation'):
            self.wordsWithoutPunction()
        for word in self.pz_words_as_array_without_punctuation:
            if len(word) not in self.word_lengths_freqeuncy:
                self.word_lengths_freqeuncy[len(word)] =0
            self.word_lengths_freqeuncy[len(word)] += 1
      
        
        
    def isThereApostrophes(self):
        '''
        Method to test to see if the phrase as apostrophe's in it.
        If there are apostrophe's then set it to the number of apostrophe's in the phrase.
        Note the ap
        '''
        self.apostophe_words = 0
        for char in self.pz_as_string:
            if char == "'":
                self.apostophe_words += 1 
            
    def generateBlankPuzzle(self):
        '''
        Create a Blank Puzzle with the correct spacing as in the original.
        This is where characters will be filled in
        '''
        self.pz_blank_puzzle = ''
        self.pz_blank_puzzle_array = []
        for char in self.pz_as_string:
            if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                self.pz_blank_puzzle += '_'
                self.pz_blank_puzzle_array.append('_')
            else:
                self.pz_blank_puzzle += char
                self.pz_blank_puzzle_array.append(char)

    def checkForDoubleLetters(self):
        '''
        method to check for double letters
        
        '''
        self.double_letter_words = 0
        for i in range(len(self.pz_as_string)-1):
                
            if self.pz_as_string[i] == self.pz_as_string[i+1]:
                 self.double_letter_words += 1       


    def getWordCounts(self):
        '''
        Sometimes there are duplicate words that give a clue
        For example, the word 'the' may appear two or even three times
        Knowing there are duplicates is helpful
        '''
        self.word_counts = collections.Counter(self.pz_words_as_array_without_punctuation)
        
    

    def showPuzzle(self):
        '''
        Method to show the puzzle on the screen
        May consider using curses to display on the console
        '''
        # Convert pz_blank_puzzle_array to blank puzzle
        self.pz_blank_puzzle = ''
        for char in self.pz_blank_puzzle_array:
            self.pz_blank_puzzle += char
        pz_string_as_lines = self.pz_as_string.split('\n')
        blank_pz_as_lines = self.pz_blank_puzzle.split('\n')
        for i in range(len(pz_string_as_lines)):
            print(blank_pz_as_lines[i])
            print(pz_string_as_lines[i])



def main():
    '''
    Run this as needed for evaluation 
    '''
    reynard = Puzzle('data/pz1.txt')
    
    reynard.showPuzzle()
    reynard.getWordCounts()
    print("OK")

if __name__ == "__main__":
    main()