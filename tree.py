


from copy import deepcopy
import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words
import enchant
import re
from string import ascii_uppercase
from random import choice
from reynard_constants import *

class Tree:
    '''
    Tree Structure based on recursion.
    A node or tree can have many children depending
    '''
    def __init__(self,parent=None,state=None):
        '''
        Constructor 
        Root parent is None
        '''
        self.children = []
        self.parent = parent
        self.state = state
        self.utility = 0
        if parent:
            self.game_state = deepcopy(parent.game_state)
            self.key = deepcopy(parent.key)
            self.pz_key_used =deepcopy((parent.pz_key_used))
        else:
            self.game_state = []
            self.key = []
            self.pz_key_used = []
            
        self.letter = {}

        self.word = ''
        self.word_pz = ''
        self.expand = True
        self.tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe

    def keyValueUsed(self):
        if self.parent == None:
            return False
        if self.parent.parent == None:
            # We're at a reasonable level:
            return False
        if len(self.parent.children) < 2:
            # If there aren't two children then don't bother
            return False
        for child in self.parent.children:
            child_keys = list(child.letter.keys())
            child_values = list(child.letter.values())
            self_keys = list(self.letter.keys())
            self_values = list(self.letter.values())

            if len(child_keys) == len(self_keys) and len(child_values) == len(self_values) \
            and all([child_keys[i] == self_keys[i] for i in range(len(child_keys))]) \
            and all([child_values[j] == self_values[j] for j in range(len(child_values))]):
                #print('keys {} {} and values {} {} are the same'.format(child_keys,self_keys,child_values,self_values))
                return True
        return False

    def addChild(self,child):
        self.children.append(child)
        
    def assignState(self,state):
        self.state = deepcopy(state)
                   
    def checkGameStateForWord(self, pz_idx, lenPzWd):
        '''
        For the given puzzle index is this entire
        word blank
        '''
        for i in range(pz_idx,pz_idx+lenPzWd):
            if self.game_state[i] != '_':
                return False
        return True

    def gamePzCharNotUsed(self,puzz_wd,real_wd):
        '''
        Given these two words, return a random character that hasn't been used 
        '''
        charLst = []
        for char in self.key.keys():
            if char not in self.pz_key_used:
                if self.key[char] not in list(real_wd):
                    charLst.append(char)
        return choice(charLst)

    def ltrsused(self):

        return list(set([ch for ch in self.game_state if ch in ascii_uppercase ]))

    def lettersNotInKey(self):
        '''
        Return letters not in key 
        When a puzzle doesn't use all the keys we need to be swap them in and out
        This is not useful
        '''
        return [letter for letter in ascii_uppercase if letter not in self.key.keys()]      

    def gameCharForWord(self,puzz_wd,real_wd):
        '''
        Given these two words, return the keys for real_wd
        '''
        charLst = []
        for char in list(real_wd):
            if char in list(self.key.values()):
                charLst.append(list(self.key.keys())[list(self.key.values()).index(char)])
            else:
                # Note that some letters may not be used in the puzzle so need to add it 
                # when we can.  It may be important - Real Word Letters that is

                t_key = self.gameCharForWord()
                self.key[t_key] = char
                charLst.append(t_key)
        return charLst

    def setState(self,puzzle):
        '''
        Makes the puzzle state -- given a guess it will 
        take the puzzle and 
        
        '''
        guess = self.key
        state = []
        for lt in puzzle.pz_array:
            if lt in ascii_uppercase:
                state.append(guess[lt])
            else:
                state.append(lt)
        self.state = state
    
    def makeGameState(self,puzzle):
        '''
        As we go along pupulate the game board 
        Use it for reference -- does it make sence.
        '''

        for ky in self.letter.keys():
            tryThis = []
            if type(self.word) == list:
                tryThis = self.word
            else:
                tryThis = list(self.word.upper())
            
            if self.letter[ky] in tryThis:
                for i in range(len(puzzle.pz_array)):
                    if puzzle.pz_array[i] == ky:
                        self.game_state[i] = self.letter[ky]

    def validChildren(self):
        '''
        Method to check that the parent's gamestate agrees with the childs
        Child's should only be different by the letters its assigned.
        Expensive but worth it -- Validation.
        '''
        if self.parent == None and len(self.children) > 0:
            for child in self.children:
                self.checkChildren(child)
        elif self.parent.parent == None and len(self.children) > 0:
            for child in self.children:
                self.validChildren(child)
        else:
            for i in range(len(self.parent.game_state)):
                if self.parent.game_state[i] in ascii_uppercase:
                    if self.parent.game_state[i] != self.game_state[i]:
                        return False
        return True

    def checkValidkey(self):
        '''
        All the letters in the key and values should be unique
        This is a very expensive algorithm in terms of time. 
        It checks every child against every parent.
        '''
        valueCount= {}
        keyCount = {}
        for ky in list(self.key.values()):
            if ky not in valueCount.keys():
                valueCount[ky]= 0
            valueCount[ky] += 1
            if valueCount[ky] > 1: 
                return False
        for ky2 in list(self.key.keys()):
            if ky2 not in keyCount.keys():
                keyCount[ky2] = 0
            keyCount[ky2] += 1
            if keyCount[ky2] > 1:
                return False
        return True

    def setUtility(self):
            '''
            Provides a utilty score based on the key that is being used.
            go for one and two letters first. 

            '''
            wordTruth = []
            checkThis = self.tokenizer.tokenize(''.join(self.state))
            for word in checkThis:
                if '_' not in word:
                    if len(word) == 1 and word in ['A','I']:
                        if word == 'A':
                            wordTruth.append(1)
                        wordTruth.append(1)
                    if len(word) == 2 and word.lower() in two_letter_word_frequency:
                        wordTruth.append(1)
                        wordTruth.append(1)
                    elif len(word) == 3 and word.lower() in three_letter_word_frequency:
                        wordTruth.append(1)
                        wordTruth.append(1)
                        wordTruth.append(1)
                        if word == 'THE':
                            wordTruth.append(1)
                    elif len(word) == 4 and word.lower() in four_letter_word_frequency:
                        wordTruth.append(1)
                        wordTruth.append(1)
                        wordTruth.append(1)
                        wordTruth.append(1)
                    else:
                        wordTruth.append(0)
                    if len(word) == 2 and word.lower()[0] in 'efklpqruvxyz':
                        wordTruth.append(0)
                        wordTruth.append(0)
                        wordTruth.append(0)
                    if len(word) == 2:
                        if word[0] not in ['aeiou'] and word[1] not in ['aeiou']:
                           for i in range(4):
                               wordTruth.append(0)
                            
                else:
                    wordTruth.append(0)
            #// TODO as we progress can we guess at words
            self.utility = sum(wordTruth)/len(wordTruth)       
            #// TODO Try different algorithms here to get to correct solutions        

    def shouldAddChildren(self):
        '''
        To make it less costly in terms of processing an approach to adding nodes 
        that are only added if they have a higher utility than the nodes siblings.
        '''
        if self.parent == None:
            return True
        if self.parent.parent == None:
            # We're at a reasonable level:
            return True
        if len(self.parent.children) < 2:
            # If there aren't two children then don't bother
            return True
        if not any([self.utility >= child.utility for child in self.parent.children]):
            if sum([self.utility >= child.utility for child in self.parent.children]) > 0:
                print(">>>{}".format(sum([self.utility >= child.utility for child in self.parent.children])))
            return False
        return True
            


if __name__ == "__main__":
    pass
    