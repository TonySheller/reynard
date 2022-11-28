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
import operator
import string



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
            self.pz_letter_frequency =self.letterFrequency()
            self.wordLengthsFrequency()
            self.generateBlankPuzzle()
            self.generateEmptyKey()
              
    def generateEmptyKey(self):
        '''
        Generate an empty key 
        '''
        pz_key = {}
        for key in self.pz_letter_frequency:
            pz_key[key] = "_"
            
        return pz_key
                   
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
        Method that splits text into words with punctuation. 
        '''
        tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        self.pz_words_as_array_with_punctuation = tokenizer.tokenize(self.pz_as_string)
    
    def wordsWithoutPunction(self):
        '''
        Method to get all words without punctuation
        Note May want to figure out how to leave apostrophes in.
        '''
        tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        self.pz_words_as_array_without_punctuation = tokenizer.tokenize(self.pz_as_string)
        
    def letterFrequency(self):
        '''
        Method to get the frequency count of letters in the puzzle
        It sets the self.pz_letter_frequency attribute
        '''
        pz_letter_frequency = {}
        # If it doesn't exist then create it
        if not hasattr(self, 'pz_words_as_array_without_punctuation'):
            self.wordsWithoutPunction()
        # use split on this on the original and see what happens.
        for word in self.pz_words_as_array_without_punctuation:
            if "'" in word:
                word = ''.join(word.split("'")) # pull out the apostrophe so we can count letters
            for char in word:
                if char not in pz_letter_frequency \
                    and char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    pz_letter_frequency[char] = 0
                pz_letter_frequency[char] += 1
        summed = sum(pz_letter_frequency.values())
        for key in pz_letter_frequency:
            pz_letter_frequency[key] = float("{:.4f}".format(pz_letter_frequency[key]/summed))
        # Now rearrange them according to most frequent to least frequent.
        pz_letter_frequency = dict(sorted(pz_letter_frequency.items(), key=operator.itemgetter(1),reverse=True ))
        return pz_letter_frequency

    def uniqueWordsThisLength(self,length):
        '''
        method to return the count of unique words of a certain length
        '''
        wds = {}
        for wd in self.pz_words_as_array_without_punctuation:
            if len(wd) == length:
                if wd not in wds.keys():
                    wds[wd] = 0
                wds[wd] += 1
        return len(wds.keys())

    def wordLengthsFrequency(self):
        '''
        Method to get a frequency count of word lengths
        It sets the self.pz.len_words_frequency attribute
        '''

        self.pz_word_lengths_freqeuncy = {}
        # If it doesn't exist then create it
        if not hasattr(self, 'pz_words_as_array_without_punctuation'):
            self.wordsWithoutPunction()
        words =list(set([word for word in self.pz_words_as_array_without_punctuation]))
        for word in words:
            if len(word) not in self.pz_word_lengths_freqeuncy:
                self.pz_word_lengths_freqeuncy[len(word)] =0
            self.pz_word_lengths_freqeuncy[len(word)] += 1
      
    def bothAandI(self):
        '''
        There is a possibility that both A and I will be a puzzle so need to check for that. 
        '''
        oneLetterWords = []
        for word in self.pz_words_as_array_without_punctuation:
            if len(word) == 1 and word not in oneLetterWords:
                oneLetterWords.append(word)
        if len(oneLetterWords) > 1:
            return True
        return False
        
    def wordsOfLength(self,length):
        '''
        Simple method to return 
        '''     
        return length in self.pz_word_lengths_freqeuncy.keys()

    def indexOfWord(self, puzz_wd):
        '''
        Find all indexes of this word in the puzzle
        Return the index of the first letter
        '''
        returnThis = self.pz_as_string.find(puzz_wd)
        return returnThis
        
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
        self.pz_word_counts = collections.Counter(self.pz_words_as_array_without_punctuation)  

    def showPuzzle(self):
        '''
        Method to show the puzzle on the screen
        May consider using curses to display on the console
        '''
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
    For Evaluation
    '''
    reynard = Puzzle('data/pz1.txt')
    
    reynard.showPuzzle()
    reynard.getWordCounts()
    print("OK")

if __name__ == "__main__":
    main()