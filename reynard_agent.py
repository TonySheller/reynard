'''
This python module will create an agent.

The agent is being constructed in a separate module for 
compactness and separation of concerns (agent from data)
'''


from mcts import mcts
from copy import deepcopy
import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
import enchant
import pyAgrum as gum
from reynard_constants import *
from reynard_puzzle import Puzzle
from reynard_mcts_a_or_i import ReynardStateAorI, Action

class Agent:
    '''
    This is the robot, prefer agent, that reasons its way through solving a cryptogram
    
    '''
    
    
    def __init__(self,puzzle=None):
        '''
        Constructor
        Set Gaol as 0 aka not achieved.  1 will be achieved. This will be based on the percentage of the puzzle solved.
        '''
        if not puzzle:
            print("Please provide a puzzle as an argument")
            return -1
        self.pz = Puzzle('data/pz1.txt')
        self.pz_string = puzzle
        
    def reason(self):
        
        pass
        
        
    def oneLetterWords(self):
        '''
        We want to be sure that we have the best value for one letter words
        so we will reason about it firs -- if there are any one letter words
        
        '''
        # Check for one letter words in the puzzle
        #self.aori = ReynardStateAorI(self.pz_string)
        check_this = ' '.join(self.pz.pz_words_as_array_without_punctuation)
        oneLetterWords=[]
        for word in self.pz.pz_words_as_array_without_punctuation:
            if len(word) == 1 and word not in oneLetterWords:
                oneLetterWords.append(word) # more of a character
                
        if len(oneLetterWords) > 0:
            print("yes, therer are one letter words")
            self.aori = ReynardStateAorI(self.pz_string)       
    
        aori = ReynardStateAorI(self.pz_string)    
        searcher = mcts(timeLimit=5000,iterations=10)
    
        action = searcher.search(initialState=self.aori)
        print('search complete and action provided')
        print(action)    

if __name__ == "__main__":
    rnag = Agent('data/pz1.txt')
    rnag.oneLetterWords()
    