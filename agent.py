'''
Anthony Sheller
Reasoning Under Uncertainty
EN.605.745
This Python module will create an agent.

The agent Python Module of Reynard
'''

from copy import deepcopy, copy
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
from datetime import timedelta
import statistics
import hashlib
import json


MAX_NODE_COUNT = 500
VALIDATE = False
VERBOSE = False


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
        self.node_count = 0
        self.hashkeysUsed = []
        self.VERBOSE = VERBOSE

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
        tree = deepcopy(node)
        tree.children =[]
        if toLt not in tree.key.values():
            ## Swap out least used key
            tree.swapFor(self.puzzle.pz_letter_frequency,toLt)
            
        current_idx = list(tree.key.keys())[list(tree.key.values()).index(toLt)]
        
        other_value = node.key[fmLt]
        tree.pz_key_used.append(fmLt)
        tree.key[fmLt] = toLt
        tree.key[current_idx] =other_value
        tree.word = wd
        tree.word_pz = wd_pz
        tree.letter[fmLt] =toLt
        tree.makeGameState(self.puzzle)
        tree.setUtility()
        if tree.utility >= node.utility:        
            node.children.append(tree)
            self.node_count += 1

    def tryWord(self,node,puzz_wd,real_wd,minUtility = 0.0):
        '''
        Try this word in the puzzle
        # Just one word
        '''
        r_wd_temp = real_wd
        p_wd_temp = puzz_wd
        if all([lt in node.ltrsused() for lt in list(real_wd)]):
            return # Don't bother -- these letters have been used already
        if all([lt in node.pz_key_used for lt in list(puzz_wd)]):
            return # don't bother --  all these letters have been used
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
        if node.checkGameStateForWord(pz_idx, len(puzz_wd)):
            tode = deepcopy(node)
            del tode.children
            tode.children = []
            tode.parent = node
            swapKeys = tode.gameCharForWord(self.puzzle.pz_letter_frequency,puzz_wd,real_wd)
            if VALIDATE:
                if not tode.checkValidkey():
                    print("Validation Failed -- something is wrong")
            for pz_key in list(puzz_wd):
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

            dhash = hashlib.md5()
            encoded = json.dumps(tode.key,sort_keys=True).encode()
            dhash.update(encoded)
            tode.hash = dhash.hexdigest()
            if tode.hash not in self.hashkeysUsed:
                if not tode.keyValueUsed() and tode.utility > node.utility:
                    if tode.shouldAddChildren() and tode.utility > minUtility:
                        node.children.append(tode)
                        self.node_count += 1
                        self.hashkeysUsed.append(dhash.hexdigest())
                        if self.VERBOSE:
                            print("Adding {} utility is {}".format(tode.letter,round(tode.utility,3)))
                        if VALIDATE:
                            if not tode.validChildren():
                                print("Validation Failed -- something is wrong -- child overwrote parent's key")
            else:
                if dhash.hexdigest() in self.hashkeysUsed:
                    if self.VERBOSE:
                        print("not adding {} {} already added".format(tode.letter,round(tode.utility,3)))
        else:
            if self.VERBOSE:
                print("Cannot Assign {} <-> {} || used set is {}".format(real_wd,puzz_wd,node.pz_key_used))
        if self.node_count % 500 == 0:
            if self.VERBOSE:
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

    def swapLettersBasedOnValues(self, tkey,lt1,lt2):
        lt1_idx = list(tkey.keys())[list(tkey.values()).index(lt1)]
        lt2_idx = list(tkey.keys())[list(tkey.values()).index(lt2)]
        returnThis ={}
        returnThis[lt2_idx] = lt1
        returnThis[lt1_idx] = lt2
        return returnThis

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
        elif len(oneLtWd) == 1:                
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
        elif len(oneLtWd) == 0: 
            if self.VERBOSE:
                print("No one letter words in this puzzle.")
 
    def traverseTree(self,node,wdLst,minUtility):
        '''
        Recursive function to traverse all the children and add nodes
        if there worth it.
        '''

        if len(node.children) > 0:
            for child in node.children:
                if child.expand:
                    self.traverseTree(child,wdLst,minUtility)
        else:
            self.tryWords(node,wdLst,minUtility)

    def otherWordsThisLength(self,node,length):
        '''
        We need to see if we can fill in all the words of a certain length.
        Are there other words of this length?
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
                if child.utility >= limit:
                    tode = deepcopy(child)
                    search_list.append(tode)

                else:
                    if self.VERBOSE:
                        print("node {} not good {} < {}".format(child.letter,child.utility,round(limit,3)))
        return search_list 
                    
    def getAvgChildUtility(self,node,avgUtil):
        for child in node.children:
            if len(child.children) > 0: 
                return self.getAvgChildUtility(child, avgUtil)
            
 
            avgUtil.append(child.utility)

        return statistics.mode(avgUtil) 

    def processTwoLetterWords(self,node,start_index,end_index):
        if self.puzzle.wordsOfLength(2):
            # do an initial pass 
            newRoot = None
            children = []
            self.node_count = 0
            for i in range(self.puzzle.uniqueWordsThisLength(2)):
                #startTime = time()
                if len(node.children) > 0:
                    filter = self.getAvgChildUtility(node,[])
                else:
                    filter = node.utility
                if self.VERBOSE:
                    print("Filtering out trees with Utility lower than {}".format(filter))
                self.traverseTree(node,two_letter_word_frequency[start_index:end_index],filter)
                iterationCount = 0
                search_list = []
                filter = self.getAvgChildUtility(node, [])
                temp_list = self.filterSearch(node,filter,search_list)
                newRoot = deepcopy(node)
                newRoot.parent = self.root
                newRoot.children = []

                for item in temp_list:
                    item.parent = newRoot
                    newRoot.children.append(item)
                    self.node_count += 1
                
                #elapsed = time() - startTime
                #elapsedThree = str(timedelta(seconds=elapsed))
                #print("\n\n TIME ELAPSED IS {} ".format(elapsedThree))
            node.children = newRoot.children

    def processThreeLetterWords(self,node,start_idx,end_idx):
        if self.puzzle.wordsOfLength(3):
            # do an initial pass 
            newRoot = None
            children = []
            for i in range(self.puzzle.uniqueWordsThisLength(3)):
                if len(node.children) > 0:
                    filter = self.getAvgChildUtility(node,[])
                else:
                    filter = node.utility
                if self.VERBOSE:
                    print("Filtering out trees with Utility Value lower than {}".format(filter))
                self.traverseTree(node,three_letter_word_frequency[start_idx:end_idx],filter)
                iterationCount = 0
                search_list = []
                filter = self.getAvgChildUtility(node, [])
                temp_list = self.filterSearch(node,filter,search_list)
                newRoot = deepcopy(node)
                newRoot.parent = self.root
                newRoot.children = []
                self.node_count = 0
                for item in temp_list:
                    item.parent = newRoot
                    newRoot.children.append(item)
                    self.node_count += 1

            node.children = newRoot.children

    def evaluateChildrenForKey(self,node,returnValue):
        '''
        Helper function for the tests 
        '''
        if len(node.children) > 0: 
            for child in node.children:
                self.evaluateChildrenForKey(child,returnValue)
        else:
           returnValue = self.checkkeyTwoLetters(node)
        return returnValue

    def evaluateChildrenForKeyThree(self,node,returnValue):
        '''
        Helper function for the tests 
        '''
        if len(node.children) > 0: 
            for child in node.children:
                self.evaluateChildrenForKeyThree(child,returnValue)
        else:
           returnValue = self.checkkeyMoreLetters(node)
        return returnValue       

    def checkkeyTwoLetters(self,node):
        '''
        Helper function for the tests
        '''
        returnVal = False
        if all([k in list(node.letter.keys()) for k in list('XCKG') ]):
                if node.letter['X'] == 'A':
                    if node.letter['C'] == 'I':
                        if node.letter['K'] == 'T':
                            if node.letter['G'] == 'O':
                                print("\n\tKey {} :: \n\tUtility of {} present in the puzzle".format(node.letter,round(node.utility,3)))
                                agent.showProgressPuzzle(node)
        # Leaving the system stack and not finding what we were
        return returnVal

    def checkkeyMoreLetters(self,node):
        '''
        Helper function for the tests
        '''
        returnVal = False
        if all([k in list(node.letter.keys()) for k in list('XCKGQM') ]):
                if node.letter['X'] == 'A':
                    if node.letter['C'] == 'I':
                        if node.letter['K'] == 'T':
                            if node.letter['G'] == 'O':
                                if node.letter['Q'] == 'M':
                                    if node.letter['M'] == 'E':
                                        print("\n\tBigger Key {} :: \n\tUtility of {}  present in the puzzle".format(node.letter,round(node.utility,3)))
                                        agent.showProgressPuzzle(node)
        # Leaving the system stack and not finding what we were
        return returnVal

    def getHighestUtility(self,node,maxVal=[]):
        '''
        What is the highest utility in the tree
        '''
        if len(node.children) > 0: 
            for child in node.children:
                self.getHighestUtility(child,maxVal)    
        else:
            maxVal.append(node.utility)
        return maxVal

    def showProgressPuzzle(self,node):
        gpuz = ''.join(node.game_state).split('\n')
        puzz = ''.join(self.puzzle.pz_array).split('\n')
        for i in range(len(gpuz)):
            print(gpuz[i])
            print(puzz[i])

if __name__ == "__main__":
    
    puzzle = Puzzle('data/pz1.txt')
    agent = Agent(puzzle=puzzle)
    agent.temp_root = []
    # Assign the initial guess
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

    if agent.puzzle.wordsOfLength(2):
        startTime = time()
  
        for child in agent.root.children:
            agent.processTwoLetterWords(child,0,5)
            

        endTime = time()
        elapsed = endTime - startTime
        elapsedTwo = str(timedelta(seconds=elapsed))
        print("Puzzle 1 -- Execution time for two letter words is {}".format(elapsedTwo))  
        maxVal = max(agent.getHighestUtility(agent.root,[]))
        print("Puzzle 1 -- Maximum Utility is {}".format(round(maxVal,3)))
        print("Puzzle 1  -- Node Count at {}".format(agent.node_count))
        agent.evaluateChildrenForKey(agent.root, False)
        agent.evaluateChildrenForKeyThree(agent.root,returnValue =False)

    if agent.puzzle.wordsOfLength(3):
        startTime = time()

        for child in agent.root.children:
            agent.processThreeLetterWords(child,0,5)

        endTime = time()
        elapsed = endTime - startTime
        elapsedTwo = str(timedelta(seconds=elapsed))
        print("Puzzle 1 -- Execution time for three letter words is {}".format(elapsedTwo))  
        maxVal = max(agent.getHighestUtility(agent.root,[]))
        print("Puzzle 1 -- Maximum Utility is {}".format(round(maxVal,3)))
        print("Puzzle 1  -- Node Count at {}".format(agent.node_count))
        agent.evaluateChildrenForKey(agent.root, False)
        agent.evaluateChildrenForKeyThree(agent.root,returnValue =False)      
    print("")