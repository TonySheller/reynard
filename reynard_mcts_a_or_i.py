'''
Reynard Reasoner - used by the agent to reason about the puzzle
The concept is to take the puzzle and then reason about each word.
This can be used in constructing Bayesian networks that can lead to 
solutions.

Potentially dynamic solutions based on what is being reasoned about.
This would certianly arm the agent with more information that a 
human counterpart would have.


While learning new topics such as Bayesian and Decision Networks, it 
became clear that to solve a cryptogram was going to require a search,
afterall all of AI is search (reference needed).

I chose to adopt an approach called Monte Carlo Tree Search, which 
would iterate through possible combinations of the key for the puzzle
returning the solution. 

This effort is the start of 

Anthony Sheller
Reasoning Under Uncertainty
EN.605.745

'''

from mcts import mcts
from copy import deepcopy
from reynard_constants import *
from reynard_puzzle import Puzzle   
import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words
import enchant

class ReynardStateAorI:
    
    def __init__(self, puzzle = None):
        if not puzzle:
            print('please provide a puzzle')
            return
        # Initialize the Puzzle
        self.puzzle = Puzzle(puzzle)
        
        self.board = self.puzzle.pz_blank_puzzle_array
        self.currentPlayer = 1
        
        # Since we are starting a new state we should check to see 
        # what letters were used. 
        
        self.actions_taken = []

    def getCurrentPlayer(self):
        # 1 for maximiser, -1 for minimiser
       return self.currentPlayer

    def getPossibleActions(self):
        '''
        This class only checks the letter A or I for one letter words
        So we have to 
        
        '''
        possibleActions = []
        # We're making a new list of actions.
        #Get the one letter words in the puzzle
        oneLetterWords=[]
        for word in self.puzzle.pz_words_as_array_without_punctuation:
            if len(word) == 1 and word not in oneLetterWords:
                oneLetterWords.append(word) # more of a character
        
        
        x_actions_taken =  [ action.x for action in self.actions_taken]
        y_actions_taken = [action.y for action in self.actions_taken]
        for key in oneLetterWords:
            #if key not in x_actions_taken:
            for key2 in ['A','I']:     
                if key != key2 and key2 not in y_actions_taken:
                    possibleActions.append(Action(player=self.currentPlayer,x=key,y=key2))
        print("Length of Possible Actions is {}".format(len(possibleActions)))
        return possibleActions

    def actionUtility(self,action):
        '''
        When an action is taken we want to measure its utility.
        It should be a common criterium
        1. Does it start any two letter words? + 1 
        2. Does it start any three letter words? +1
        3.  Does it make send if it does?  + 1
        3. Is there a word with an apostrophe, Like I'm? +2
        4. What is the word count for 3 and 4 letter words that
        contain the letter? floor(Sqrt(of the count) should keep it small
        '''
        d = enchant.Dict('en.US')
        utilityScore = 0
        tokenizer = RegexpTokenizer("[\w']+") ## The \w' will leave in the apostrophe
        temp_word_list = tokenizer.tokenize(''.join(self.board))
        
        for word in temp_word_list:
            if action.y in word:
                possible_words = list(set([wd.lower() for wd in words.words() if len(wd) == len(word) and wd.lower()[word.index(action.y)] == action.y.lower() and d.check(wd.lower())]))
                utilityScore += len(possible_words)
        action.utility = utilityScore
        return action

    def takeAction(self, action):

        newState = deepcopy(self)
        
        # Assign the action to the board
        # Iterate through the puzzle 
        for i in range(len(newState.board)):            
            if newState.puzzle.pz_array[i] == action.x:
                newState.board[i] = action.y
        action = newState.actionUtility(action)
        newState.actions_taken.append(action)
            
        print("Action {} taken".format(action))
        print("\n{} \n".format(self.puzzle.pz_as_string))
        print("\n{} \n".format(''.join(newState.board)))
        print("\n")
        #newState.currentPlayer = self.currentPlayer * -1
                       
        return newState

    def isTerminal(self):
        ''' 
        What is our terminal state? 
        If I know something is not working out,
        Can I just cut it off? yes, why not!
        '''
        if not self.oneLetterWordCheckOK():
            # There was a forbidden one letter word in a one letter
            # word slot. :-0 Oh No!
            self.termination_reason = TERMINATEONELETTERWORD
            return True
        if '_' not in self.board:
            self.termination_reason = BOARDFULL
            return True
        if not self.twoLetterWordsOK():
            self.termination_reason = TERMINATETWOLETTERWORD
            return True
        if len(self.getPossibleActions()) == 0:
            self.termination_reason = NOMOREACTIONS
            return True

        return False
    
    def oneLetterWordCheckOK(self):
        '''
        I'm going to assume that one letter words are either an A or an I
        
        if a character has been placed in a one letter word then its bad
        '''
        tokenizer = RegexpTokenizer("[\w']+") ## The \w' will leave in the apostrophe
        temp_word_list = tokenizer.tokenize(''.join(self.board))
        for word in temp_word_list:    
            if len(word) == 1 and word != '_':
                # if there's a letter in the one letter word spot and its not an A or I
                # Then return False
                if word not in ['A','I',]:
                    return False
        # Everything OK -- return True
        return True    
    
    def twoLetterWordsOK(self):
        '''
        Checking for two letter words now
        
        '''

        d = enchant.Dict("en_US")
        tokenizer = RegexpTokenizer("[\w']+") ## The \w' will leave in the apostrophe
        temp_word_list = tokenizer.tokenize(''.join(self.board))
        
        twoLetterWords = [word for word in temp_word_list if len(word) == 2]
        for word in twoLetterWords:
            if '_' not in word:
                if word not in two_letter_word_frequency:
                    return False
        return True



        
    def getReward(self):
        # only needed for terminal states

        ## If puzzle partially solve
        ## Return 10
        
        ## If Puzzle sovled return 100

        #return self.termination_reason
        if self.termination_reason < 0: 
           return False
        return self.termination_reason 
    
    
    def __eq__(self, other):
        pass

class Action:
    def __init__(self, player, x, y):
        '''
        We can think of an action as a letter assignment. 
        For every letter in the puzzle it could take on 1 of 25
        possible values.  
        '''
        self.player = player
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y and self.player == other.player

    def __hash__(self):
        return hash((self.x, self.y, self.player))

if __name__=="__main__":
    rs_aori = ReynardStateAorI(puzzle ='data/pz1.txt')
    # The 'searcher' will keep a tree of the search states. 
    searcher = mcts(iterationLimit=10)
    
    action = searcher.search(initialState=rs_aori)
    print('search complete and action provided')
    print(action)    