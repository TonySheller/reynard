'''
This python module will create an agent.

The agent is being constructed in a separate module for 
compactness and separation of concerns (agent from data)
'''



from copy import deepcopy
import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words
import enchant
import pyAgrum as gum
from reynard_constants import *
from puzzle import Puzzle
from tree import Tree
from string import ascii_uppercase
import re
from itertools import combinations, permutations
import threading
from time import sleep

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
        
        self.puzzle= puzzle
        self.root = Tree(parent=None)
        self.root.assignState(self.puzzle.pz_blank_puzzle_array)
        self.d = enchant.Dict('en.GB')
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        self.root.game_state = self.puzzle.pz_blank_puzzle_array
        
    def __del__(self):
        pass
        

    def adjust_key(self):
        pass

    def utility(self,node):
        '''
        
        '''
        wordTruth = []
        checkThis = self.tokenizer.tokenize(''.join(node.state))
        for word in checkThis:
            if len(word) == 1 and word in ['A','I']:
                wordTruth.append(1)
            if len(word) == 2 and word.lower() in two_letter_word_frequency:
                wordTruth.append(1)
            elif len(word) == 3 and word.lower() in three_letter_word_frequency:
                wordTruth.append(1)
            elif len(word) == 4 and word.lower() in four_letter_word_frequency:
                wordTruth.append(1)
            else:
                wordTruth.append(0)
        node.utility = sum(wordTruth)/len(wordTruth)                

    def makeState(self,guess):
        state = []
        for lt in self.puzzle.pz_array:
            if lt in ascii_uppercase:
                state.append(guess[lt])
            else:
                state.append(lt)
        return state
    
    def makeGameState(self,node):
        for ky in node.letter.keys():
            for i in range(len(self.puzzle.pz_array)):
                if self.puzzle.pz_array[i] == ky:
                    node.game_state[i] = node.letter[ky]
                    print('tada')
                             
    def makeInitialGuess(self):
        print("Making a guess")
        firstGuess = []
        pz_keys = self.puzzle.pz_letter_frequency.keys()
        gs_keys = letter_frequency_wiki.keys()
                    
        firstGuess = dict(zip(pz_keys,gs_keys))
        print("Guess Ready")
        state = []
        self.root.key = firstGuess
        self.root.state = self.makeState(firstGuess)
        self.utility(self.root)
        
     
    def swapLetter(self,node,fromLtr):
        to_idx = ''
            
            
        
        
    def assignAorI(self,node,ltr):
        if self.puzzle.wordsOfLength(1):
            pz = self.puzzle.pz_words_as_array_without_punctuation
            oneLtWd = list(set([wd for wd in pz if len(wd) == 1]))
            if len(oneLtWd) > 1:

                for i in [['A','I'],['I','A']]:
                    k=0
                    ltrs = {}
                    temp_key = deepcopy(node.key)
                    tree = Tree(parent = node)
                    for j in i:
                        # Get the index of the key whose value is A or I
                        from_idx = list(node.key.keys())[list(node.key.values()).index(j)]
                    
                        # If the other values is the index of the opposite then get index of 'E'
                        if j == 'A' and node.key[from_idx] == 'A':
                            pass
                             # Don't change it! we got it right!
                        elif j == 'I' and node.key[from_idx] == 'I':
                            pass
                            # Again I is in an acceptable location
                        else:
                            # Now we want to swap things around 
                            if j == 'A':
                                from_idx = oneLtWd[k]
                            elif j == 'I':
                                from_idx = oneLtWd[k]
                            k+=1 
                            tempValue = temp_key[from_idx]
                            temp_key[from_idx] = j
                            temp_key[to_idx] = tempValue
                            ltrs[from_idx] =j
                    tree.key = temp_key
                    tree.letter = ltrs
                    tree.state = self.makeState(temp_key)
                    tree.game_state = deepcopy(node.game_state)
                    self.makeGameState(tree)
        

                    self.utility(tree)
                    node.children.append(tree)
                print("pause")                            
                        
            else:
                to_idx = ''
                tree = Tree(parent = node)
                for i in range(len(self.puzzle.pz_words_as_array_without_punctuation)):
                    if len(self.puzzle.pz_words_as_array_without_punctuation[i]) == 1:
                        to_idx = self.puzzle.pz_words_as_array_without_punctuation[i]
                        break # as we've got the key
                temp_key  = deepcopy(node.key)
                other_val = node.key[to_idx]
                other_idx = list(node.key.keys())[list(node.key.values()).index(ltr)]
                temp_key[to_idx] = ltr
                temp_key[other_idx] = other_val
                tree.key = temp_key
                tree.letter[to_idx] = ltr
                tree.state = self.makeState(temp_key)
                tree.game_state = deepcopy(node.game_state)
                self.makeGameState(tree)
                self.utility(tree)
                node.children.append(tree)
                print("pause")
 
                        





if __name__ == "__main__":
    puzzle = Puzzle('data/pz1.txt')
    agent = Agent(puzzle=puzzle)
    agent.makeInitialGuess()
    if agent.puzzle.wordsOfLength(1):
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else:
            agent.assignAorI(node, ['A','I'])
    
    print("pause")
    