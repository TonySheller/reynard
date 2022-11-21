'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745
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
from time import sleep,time

EXPANSION_LEVEL = 55000
VALIDATE = False
class Agent:
    '''
    This is agent that reasons its way through solving a cryptogram
    
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
        self.node_not = 0
        self.tooManyNodes = False
        self.keys_tried = []
        self.root.puzzle = self.puzzle.pz_array
        self.itcount = 0    
    def startPuzzle(self):
        '''
        The opening move --
        This initializes the key and provides an initial utility
        measure -- which will be zero because there is nothing filled in
        on the game board.
        '''
        firstGuess = []
        pz_keys = self.puzzle.pz_letter_frequency.keys()
        gs_keys = letter_frequency_wiki.keys()
                    
        firstGuess = dict(zip(pz_keys,gs_keys))

        state = []
        self.root.key = firstGuess
        self.root.makeGameState(self.puzzle)
        self.root.setUtility()
        
    def addChildToNode(self,node, fmLt, toLt,wd_pz,wd):
        '''
        Given the node, add a child to it

        '''
        #1. Copy the nodes values so we can add to them
        temp_key = deepcopy(node.key)
        tree.children =[]
        tree = Tree(parent=node)
        current_idx = list(node.key.keys())[list(node.key.values()).index(toLt)]
        
        other_value = node.key[fmLt]
        tree.pz_key_used.append(fmLt)
        tree.key[fmLt] = toLt
        tree.key[current_idx] =other_value
        tree.word = wd
        tree.word_pz = wd_pz
        tree.letter = {fmLt:toLt}
        tree.state = self.makeState(temp_key) 
        tree.makeGameState(self.puzzle)
        tree.setUtility()
        if tree.utility >= node.utility:        
            if len(self.high_node) == 0:
                self.high_node.append(tree)
            elif tree.utility >= self.high_node[-1].utility:
                self.high_node.append(tree)
            node.children.append(tree)
            self.node_count += 1

    def tryWord(self,node,puzz_wd,real_wd,minUtility = 0.0):
        '''
        Try this word in the puzzle
        # Just one word
        '''
        r_wd_temp = real_wd
        p_wd_temp = puzz_wd
        # if real_wd == 'HE' and puzz_wd == 'GH':
        #     self.itcount += 1
        #     print("{}".format(self.itcount))
        if all([lt in node.ltrsused() for lt in list(real_wd)]):
            return
        if all([lt in node.pz_key_used for lt in list(puzz_wd)]):
            return # Just go all these letters have been used
        elif any([lt in node.ltrsused() for lt in list(real_wd)]) or \
            any([lt in list(puzz_wd) for lt in list(real_wd)]):
            real_wd_tmp = ''
            puzz_wd_tmp = ''
            for i in range(len(real_wd)):
                if real_wd[i] not in node.ltrsused() and real_wd[i] != puzz_wd[i]:
                    real_wd_tmp += real_wd[i]
                    puzz_wd_tmp += puzz_wd[i]
            real_wd = real_wd_tmp
            puzz_wd = puzz_wd_tmp
            if puzz_wd == real_wd:
                puzz_wd = node.gamePzCharNotUsed(puzz_wd, real_wd)
        elif any([lt in node.pz_key_used for lt in list(puzz_wd)]):
            real_wd_tmp = ''
            puzz_wd_tmp = ''
            for i in range(len(puzz_wd)):
                if puzz_wd[i] not in node.pz_key_used:
                    real_wd_tmp += real_wd[i]
                    puzz_wd_tmp += puzz_wd[i]
            real_wd = real_wd_tmp
            puzz_wd = puzz_wd_tmp
            if puzz_wd == real_wd:
                puzz_wd = node.gamePzCharNotUsed(puzz_wd, real_wd)
            # We adjust the words such that that letter isn't in there any 
        if len(puzz_wd) != len(real_wd) or not len(real_wd) >  0 and not len(puzz_wd) > 0:
            return

        pz_idx = self.puzzle.indexOfWord(puzz_wd)
        # Are these puzzle keys available for use?
        if node.checkGameStateForWord(pz_idx, len(puzz_wd)):
            tode = deepcopy((node))
            del tode.children
            tode.children = []
            tode.parent = node
            swapKeys = tode.gameCharForWord(puzz_wd,real_wd)
            # For each letter do this
            if VALIDATE:
                if not tode.checkValidkey():
                    print("Validation Failed -- something is wrong")
            for pz_key in list(puzz_wd):
                # Get its value

                pz_val = tode.key[pz_key]
                idx_rl_wd = list(puzz_wd).index(pz_key) # index of the letter in the real word
                rl_key = list(tode.key.keys())[list(tode.key.values()).index(real_wd[idx_rl_wd])]
                rl_val = tode.key[rl_key]
                if pz_key == rl_val:
                    pz_key = tode.gamePzCharNotUsed(puzz_wd+pz_key, real_wd)
                tode.key[pz_key] = rl_val
                tode.letter[pz_key] = rl_val
                tode.pz_key_used.append(pz_key)
                if rl_key == pz_val:
                    o_key = tode.gamePzCharNotUsed(puzz_wd+rl_key, real_wd)
                    v3 = tode.key[o_key]
                    tode.key[o_key] =pz_val
                    pz_val = v3
                tode.key[rl_key] = pz_val
            if VALIDATE:
                if not tode.checkValidkey():
                    print("Validation Failed -- something is wrong")
            tode.word = real_wd
            tode.word_pz = puzz_wd
            tode.setState(self.puzzle)
            tode.makeGameState(self.puzzle)
            if VALIDATE:
                if not tode.checkValidkey():
                    print("Validation Failed -- something is wrong")
            tode.setUtility()
            if self.checkkey(tode):
                print("This is the key so far")
            ## Deciding to add node or not
            if not tode.keyValueUsed() and tode.utility > node.utility:
                if tode.shouldAddChildren() and tode.utility >= minUtility:
                    node.children.append(tode)
                    self.node_count += 1
                    print("Adding {} utility is {}".format(tode.letter,round(tode.utility,3)))

                if self.checkkey(tode):
                    print("This is the key so far")

                    #if not self.high_node:
                    #    self.high_node.append(tode)
                        #print("{} to {} with Utility of {}".format(tode.word,tode.word_pz,tode.utility))    
                    #elif tode.utility >= self.high_node[-1].utility:
                    #    self.high_node.append(tode)
                    #    print("{} to {} with Utility of {}".format(tode.word,tode.word_pz,tode.utility))    
                    if VALIDATE:
                        if not tode.validChildren():
                            print("Validation Failed -- something is wrong -- child overwrote parent's key")
                else:
                    pass
                    #print("not adding {} utility too low {}".format(tode.letter,tode.utility))
        else:
            pass
            #print("Cannot Assign {} <-> {} || used set is {}".format(real_wd,puzz_wd,node.pz_key_used))
        if self.node_count % 500 == 0:
            print("Node Count at {}.".format(self.node_count))

    def tryWords(self,node,wdLst,minUtility):
        '''
        When we get into this function we're going to be dangling on
        the end of a node. and need to  
        '''

        for puzz_wd in self.puzzle.pz_words_as_array_without_punctuation:
            for real_wd in wdLst:
                if len(puzz_wd) == len(real_wd) and node.word != real_wd:
                    self.tryWord(node,puzz_wd,real_wd.upper(),minUtility)

     
    def twoLtWdsBeginWithAorI(self):
        '''
        If we had an A or I or both then lets see if there are words that begin with A or I 
        That we can do something about.
        '''        
        pz = self.puzzle.pz_words_as_array_without_punctuation
        for child in self.root.children:
            for ltAorI in child.letter.values():
                the_key = list(child.letter.keys())[list(child.letter.values()).index(ltAorI)]
                twoLtWdpz = list(set([wd for wd in pz if len(wd) == 2]))

                for twLtWd in twoLtWdpz:
                    if  twLtWd[0] == the_key:
                        searchString = ''
                        if ltAorI == 'A':
                            searchString = 'STMN'
                        elif ltAorI == 'I':
                            searchString = 'FSNT'
                        for lt in searchString:
                            self.addChildToNode(child, twLtWd[1], lt, wd_pz=twLtWd, wd=ltAorI+lt)
              
    def assignAorI(self,node,ltr):
        '''
        First method coded -- needs refactored but good for now
        TODO Refactor this method someday
        '''
        pz = self.puzzle.pz_words_as_array_without_punctuation
        oneLtWd = list(set([wd for wd in pz if len(wd) == 1]))
        if len(oneLtWd) > 1:
            tree = deepcopy(node)
            tree.children = []
            temp_key = node.key
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
                    tree.pz_key_used.append(key)    
                tree.letter = ltrs
                tree.makeGameState(self.puzzle)
                tree.makeGameState(self.puzzle)
                tree.setUtility()
                node.children.append(tree)
                self.node_count += 1                         
                        
        else:
            to_idx = ''
            tree = tree = deepcopy(node)
            tree.children = []
            tree.word = ltr
            for i in range(len(self.puzzle.pz_words_as_array_without_punctuation)):
                if len(self.puzzle.pz_words_as_array_without_punctuation[i]) == 1:
                    to_idx = self.puzzle.pz_words_as_array_without_punctuation[i]
                    break # as we've got the key
            other_val = tree.key[to_idx]
            other_idx = list(tree.key.keys())[list(tree.key.values()).index(ltr)]
            tree.key[to_idx] = ltr
            tree.pz_key_used.append(to_idx)
            tree.key[other_idx] = other_val
            tree.letter[to_idx] = ltr
            tree.setState(self.puzzle)
            tree.makeGameState(self.puzzle)
            tree.setUtility()
            tree.parent = node
            node.children.append(tree)

            self.node_count += 1
 
    def traverseTree(self,node,wdLst,minUtility):
        '''
        Recursive function to traverse all the children and add nodes
        if there worth it.
        '''

        if len(node.children) > 0:
            if not self.tooManyNodes:
                for child in node.children:
                    if child.expand:
                        self.traverseTree(child,wdLst,minUtility)
        else:
            # No children so add some based on current puzzle setup
            self.tryWords(node,wdLst,minUtility)
            #self.tryTwoLetterWord(node,wdLst)
        #print("leaving Recursion")

    def otherWordsThisLength(self,node,length):
        '''
        We need to see if we can fill in all the words of a certain length.
        '''
        if len(node.children) > 0:
            for child in node.children:
                if child.expand:
                    return self.otherWordsThisLength(child, length)
        else:
            for wd in self.tokenizer.tokenize(''.join(node.game_state)):
                if len(wd) == length:
                    if any([ch not in ascii_uppercase for ch in list(wd)]):
                        return True
        return False

    def filterSearch(self,node, limit,search_list):
        '''
        Prune the child nodes and create a completely new tree before executing again
        fewer nodes :shrug:
        '''
        for child in node.children:
            if len(child.children) > 0:
                self.filterSearch(child, limit,search_list)
            else:
                if child.utility > limit:
                    tode = deepcopy(child)
                    tode.parent = None
                    search_list.append(tode)
                else:
                    print("node {} not good {} < {}".format(child.letter,round(child.utility,3),limit))
        return search_list 
                    
    def processTwoLetterWords(self):
        if self.puzzle.wordsOfLength(2):
            # do an initial pass
            self.traverseTree(self.root,two_letter_word_frequency,0.10)
            iterationCount = 0
            search_list = []
            new_list = self.filterSearch(self.root, 0.10,search_list)
            filters =[0.15, 0.20, 0.25,0.30,0.35,0.40,0.50]
            for i in range(self.puzzle.pz_word_lengths_freqeuncy[2] - 1):
                for newagent in new_list:
                    print("newagent {} {}".format(newagent.letter, newagent.utility))
                    
                    iterationCount += 1
                    self.traverseTree(newagent,two_letter_word_frequency,filters[i])
                    et = time()
                    search_list = []
                    new_child_list = agent.filterSearch(newagent,filters[i],search_list)
                    newagent.children = new_child_list
           
            if len(new_list) > 0:

                self.root.children = new_list

    def checkkey(self,node):
        if all([k in list(node.letter.keys()) for k in list('XCKGQM') ]):
            if all([k in list(node.letter.values()) for k in list('AITOME') ]):
                if node.letter['X'] == 'A':
                    if node.letter['C'] == 'I':
                        if node.letter['K'] == 'T':
                            if node.letter['G'] == 'O':
                                if node.letter['Q'] == 'M':
                                    if node.letter['M'] == 'E':
                                        print("this is the one we want to live")
                                        return True
        return False

    def processThreeLetterWords(self):
        if self.puzzle.pz_word_lengths_freqeuncy[2] <= 1:
            filters =[0.10,0.20,0.25, 0.30]
        elif agent.puzzle.pz_word_lengths_freqeuncy[2] == 2:
            filters =[0.10,0.20,0.30,0.40]
        elif  agent.puzzle.pz_word_lengths_freqeuncy[2] > 3:
            filters =[0.20,0.25,0.30,0.35,0.40,0.50,]  
        if self.puzzle.wordsOfLength(3):

            # do an initial pass
            self.traverseTree(self.root,three_letter_word_frequency,0.10)
            iterationCount = 0
            search_list = []
            new_list = self.filterSearch(self.root, 0.10,search_list)
            for i in range(self.puzzle.pz_word_lengths_freqeuncy[3] - 1):
                for newagent in new_list:
                    print("newagent {} {}".format(newagent.letter, newagent.utility))
                    iterationCount += 1
                    self.traverseTree(newagent,three_letter_word_frequency,filters[i])
                    search_list = []
                    new_child_list = agent.filterSearch(newagent,filters[i],search_list)
                    newagent.children = new_child_list

            if len(new_list) > 0:
                self.root.children = new_list



if __name__ == "__main__":
    
    puzzle = Puzzle('data/pz1.txt')
    agent = Agent(puzzle=puzzle)
    agent.startPuzzle()

    if agent.puzzle.wordsOfLength(1):
        st = time()
        # If the puzzle doesn't have both A and I then
        if not agent.puzzle.bothAandI():
            for ltr in ['A','I']:
                agent.assignAorI(agent.root, ltr)
        else: # The puzzle has both A and I
            
            agent.assignAorI(agent.root, ['A','I'])
        agent.twoLtWdsBeginWithAorI()
        et = time()
        #print("Execution Time for one letter words is {}".format(et-st))

    if agent.puzzle.wordsOfLength(2):
        startTime = time()
        agent.processTwoLetterWords()
        endTime = time()
        print("Execution time for two letter words is {}".format(endTime-startTime))   

    if agent.puzzle.wordsOfLength(3):
        startTime = time()
        agent.processThreeLetterWords()
        endTime = time()
        print("Execution time for three letter words is {}".format(endTime-startTime))   
    
    print("pausing")