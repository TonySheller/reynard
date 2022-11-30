'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745


tests for the reynard mcts concept
'''
import sys,os


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import unittest
import math

from reynard_constants import *
from agent import Agent
from puzzle import Puzzle
import threading
from itertools import combinations, permutations
import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words

#FILE = '/home/asheller/reynard/data'
FILE_PATH = '../reynard'

class TestSetPz1Solution(unittest.TestCase):
    '''

    '''
    def readSolution(self,solFile):
        '''
        Method to read in the puzzle provided at the command line
        '''
        
        with open(solFile,'r') as f:
            self.solution_as_string = f.read()
            self.solution_array = []
            # Need to take out the name in the cryptogram as its impacting frequency counts
            temp = ''
            for ch in self.solution_as_string:
                if ch == '(':
                    break
                else:
                    temp += ch
            self.solution = temp
            for char in self.solution_as_string:
                self.solution_array.append(char)
   
    def testpz1(self):
        '''
        
        '''
        self.readSolution(FILE_PATH + '/data/solutions/sol1.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
            
        if False in wordTruth:
            self.assertTrue(1==2)
        
    def testpz2(self):
        '''
        
        '''
        self.readSolution(FILE_PATH + '/data/solutions/sol2.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz3(self):
        '''
        
        '''
        self.readSolution(FILE_PATH + '/data/solutions/sol3.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a,','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz4(self):
        '''
        
        '''
        self.readSolution(FILE_PATH + '/data/solutions/sol4.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(wordin ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
            else:
                print("{} NOT IN LISTS".format(word))

        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz5(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol5.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz6(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol6.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)
                   
    def testpz7(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol7.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz8(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol8.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz9(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol9.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)


    def testpz10(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol10.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3 and "'" not in word:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
            
            
        if False in wordTruth:
            self.assertTrue(1==2)
                        
    def testpz11(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol11.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz12(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol12.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz13(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol13.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz14(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol14.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                wordTruth.append(word.lower() in four_letter_word_frequency)
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz15(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol15.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                if "'" not in word:
                    wordTruth.append(word.lower() in four_letter_word_frequency)
                else:
                    print('that was an apostrophe')
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

    def testpz19(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol19.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                if "'" not in word:
                    wordTruth.append(word.lower() in four_letter_word_frequency)
                else:
                    print('that was an apostrophe')
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)
            
    def testpz53(self):
        self.readSolution(FILE_PATH + '/data/solutions/sol53.txt')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        wordTruth = []
        checkThis = self.tokenizer.tokenize(self.solution_as_string)
        for word in checkThis:
            if len(word) == 1:
                wordTruth.append(word in ['A','a','I'])
            elif len(word) == 2:
                wordTruth.append(word.lower() in two_letter_word_frequency)
            elif len(word) == 3:
                wordTruth.append(word.lower() in three_letter_word_frequency)
            elif len(word) == 4:
                if "'" not in word:
                    wordTruth.append(word.lower() in four_letter_word_frequency)
                else:
                    print('that was an apostrophe')
            elif len(word) > 4:
                pass
        if False in wordTruth:
            self.assertTrue(1==2)

if __name__ == '__main__':
    unittest.main()