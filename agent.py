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
    This is agent, that reasons its way through solving a cryptogram
    
    '''
    
    def __init__(self,puzzle=None):
        '''
        Constructor
        
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
        self.high_node = []
        self.node_count = 0
        

    def utility(self,node):
        '''
        Provides a utilty score based on the key that is being used.
        go for one and two letters first. 
        
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
            if len(word) == 2 and word.lower()[0] in 'efklpqruvxyz':
                wordTruth.append(0)
                wordTruth.append(0)
        node.utility = sum(wordTruth)/len(wordTruth)                

    def makeState(self,guess):
        '''
        Makes the puzzle state -- given a guess it will 
        take the puzzle and 
        
        '''
        state = []
        for lt in self.puzzle.pz_array:
            if lt in ascii_uppercase:
                state.append(guess[lt])
            else:
                state.append(lt)
        return state
    
    def makeGameState(self,node):
        '''
        As we go along pupulate the game board 
        Use it for reference -- does it make sence.
        '''
        for ky in node.letter.keys():
            tryThis = []
            if type(node.word) == list:
                tryThis = node.word
            else:
                tryThis = list(node.word.upper())
            
            if node.letter[ky] in tryThis:
                for i in range(len(self.puzzle.pz_array)):
                    if self.puzzle.pz_array[i] == ky:
                        node.game_state[i] = node.letter[ky]

                             
    def makeInitialGuess(self):
        '''
        The opening move
        '''
        firstGuess = []
        pz_keys = self.puzzle.pz_letter_frequency.keys()
        gs_keys = letter_frequency_wiki.keys()
                    
        firstGuess = dict(zip(pz_keys,gs_keys))

        state = []
        self.root.key = firstGuess
        self.root.state = self.makeState(firstGuess)
        self.utility(self.root)
        
    def addChildToNode(self,node, fmLt, toLt,wd):
        '''
        Given the node, make this assignment
        '''
        #1. Copy the nodes values so we can add to them
        temp_key = deepcopy(node.key)
        tree = Tree(parent=node)
        current_idx = list(node.key.keys())[list(node.key.values()).index(toLt)]
        other_value = node.key[fmLt]
        temp_key[fmLt] = toLt
        temp_key[current_idx] =other_value
        tree.key = temp_key
        tree.word = wd
        tree.letter = {fmLt:toLt}
        tree.state = self.makeState(temp_key)
        tree.game_state = deepcopy(node.game_state)
        self.makeGameState(tree)
        self.utility(tree)
        if tree.utility > node.utility:
            node.children.append(tree)
            self.node_count += 1
        
    def swapLettersBasedOnKey(self,tkey,k1,k2):
        '''
        Swap letters based on keys
        '''
        returnThis = {}

        for i in range(len(k1)):
            v1 = tkey[k1[i]]
            v2 = tkey[k2[i]]
            returnThis[k1[i]] = v2
            returnThis[k2[i]] = v1

        return returnThis



        
    def tryTwoLetterWord(self,node,tlw):
        
        #1. get the characters in the puzzle that are used so far
        pz_lts = []
        for ch in node.game_state:
            if ch in ascii_uppercase:
                if ch not in pz_lts:
                    pz_lts.append(ch)

        two_letter_word_list = list(set([word for word in self.puzzle.pz_words_as_array_without_punctuation if len(word)==2]))
        temp_key = deepcopy(node.key)

        two_ltr_wd_idxs = []
        add_word = True
        for ltr in tlw:
            if ltr.upper() not in pz_lts:
                try: 
                    two_ltr_wd_idxs.append(list(temp_key.keys())[list(temp_key.values()).index(ltr.upper())])
                except Exception as e:
                    print("ERROR {}".format(e))
                    print("p")
            else:
                #print("not this one {}".format(tlw))
                add_word = False
                break
                
        # Now we have the indexes of the two letters we want to replace.  
        # Find a two letter word
        if add_word:
            for wd in two_letter_word_list:
                
                tree = Tree(parent=node)
                if any([k in two_ltr_wd_idxs for k in wd]):
                    break  # This took a while to find -- bug
                ltrs = self.swapLettersBasedOnKey(temp_key,list(wd),two_ltr_wd_idxs)
                    
                if not any([k==v for k,v in ltrs.items()]):
                    for lt in ltrs.keys():
                        tree.key[lt] =ltrs[lt]
                    tree.word = tlw  
                    tree.letter = ltrs
                    tree.state = self.makeState(tree.key)
                    #tree.game_state = deepcopy(node.game_state)
                    self.makeGameState(tree)
                    self.utility(tree)
                    if len(self.high_node) == 0:
                        self.high_node.append(tree)
                    elif tree.utility >= self.high_node[-1].utility:
                        self.high_node.append(tree)
                    if tree.utility > 0.20:
                        print("20% Utility Achieved!")      
                    if tree.utility > 0.25:
                        print("Even more Wow")
                    if tree.utility > 0.30:
                        print("OMG 30%")
                    
                    if tree.utility >= node.utility:

                        node.children.append(tree)
                        self.node_count += 1
                        if tree.utility >= self.high_node[-1].utility:
                            print("utility at {} for word '{}' '{}' ".format(tree.utility,tree.word.upper(),wd))
                            ltrsN = list(set([ch for ch in node.game_state if ch in ascii_uppercase]))
                            print("\tletters used {}".format(ltrsN))
                else:
                    pass
                    #print("ILLEGAL SWAP {} {}".format(tree.word.upper(),wd))
                
        if self.node_count % 1000 == 0:
            print("NODE COUNT NOW {}".format(self.node_count))
     
    def twoLtWdsBeginWithAorI(self):
        # Are there any two letter words that begin with A or I
        
        pz = self.puzzle.pz_words_as_array_without_punctuation
        for child in self.root.children:
            for ltAorI in child.letter.values():
                the_key = list(child.letter.keys())[list(child.letter.values()).index(ltAorI)]
                twoLtWdpz = list(set([wd for wd in pz if len(wd) == 2]))
                for twLtWd in twoLtWdpz:
                    if  twLtWd[0] == the_key:
                        #print("We have a two letter word that begins with A or I")
                        ## We need to add 'as at am and an' nodes to for each
                        searchString = ''
                        if ltAorI == 'A':
                            searchString = 'STMN'
                        elif ltAorI == 'I':
                            searchString = 'FSNT'
                        for lt in searchString:
                            self.addChildToNode(child, twLtWd[1], lt, wd=ltAorI+lt)
                
                            
    def recurseDownTryTwoLtWds(self,node,tlw):

        if len(node.children) > 0:
            for child in node.children:
                self.recurseDownTryTwoLtWds(child,tlw)
        else:
            for wd in tlw:
                self.tryTwoLetterWord(node, wd)
            
                
    def swapLettersBasedOnValues(self, tkey,lt1,lt2):
        lt1_idx = list(tkey.keys())[list(tkey.values()).index(lt1)]
        lt2_idx = list(tkey.keys())[list(tkey.values()).index(lt2)]
        returnThis ={}
        returnThis[lt2_idx] = lt1
        returnThis[lt1_idx] = lt2
        return returnThis
        
        
    def assignAorI(self,node,ltr):
        if self.puzzle.wordsOfLength(1):
            pz = self.puzzle.pz_words_as_array_without_punctuation
            oneLtWd = list(set([wd for wd in pz if len(wd) == 1]))
            if len(oneLtWd) > 1:
                temp_key = deepcopy(node.key)
                for i in [['A','I'],['I','A']]:
                    k=0
                    ltrs = {}

                    tree = Tree(parent = node)
                    tree.word = i
                    for j in i:
                        current_idx = list(temp_key.keys())[list(temp_key.values()).index(j)]

                        # If the other values is the index of the opposite then get index of 'E'
                        if temp_key[current_idx] == j and current_idx in oneLtWd:
                            if len(node.children) == 0:
                                ltrs[current_idx] = j
                            else: 
                                ltrs = self.swapLettersBasedOnValues(deepcopy(temp_key),"A","I")    
                        else:
                            for lt in oneLtWd:
                                if lt not in ltrs.keys():
                                    to_idx = lt
                                    break
                                
                            original_value = temp_key[to_idx]
                            temp_key[to_idx] = j
                            temp_key[current_idx] = original_value
                            ltrs[to_idx] =j
                        k += 1
                    for key in ltrs.keys():
                        tree.key[key] = ltrs[key]    
                    #tree.key = temp_key
                    tree.letter = ltrs
                    tree.state = self.makeState(temp_key)
                    #tree.game_state = deepcopy(node.game_state)
                    self.makeGameState(tree)
                    self.utility(tree)
                    tree.parent = node
                    node.children.append(tree)
                    self.node_count += 1                         
                        
            else:
                to_idx = ''
                tree = Tree(parent = node)
                tree.word = ltr
                for i in range(len(self.puzzle.pz_words_as_array_without_punctuation)):
                    if len(self.puzzle.pz_words_as_array_without_punctuation[i]) == 1:
                        to_idx = self.puzzle.pz_words_as_array_without_punctuation[i]
                        break # as we've got the key
                temp_key  = deepcopy(node.key)
                other_val = node.key[to_idx]
                other_idx = list(node.key.keys())[list(node.key.values()).index(ltr)]
                tree.key[to_idx] = ltr
                tree.key[other_idx] = other_val
                tree.letter[to_idx] = ltr
                tree.state = self.makeState(temp_key)
                tree.game_state = deepcopy(node.game_state)
                self.makeGameState(tree)
                self.utility(tree)
                node.children.append(tree)
                self.node_count += 1
 

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
        agent.twoLtWdsBeginWithAorI()
        print("Now trying other two letter words at the root node")
        #two letter words that do not begin with A or I
  