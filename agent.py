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
from action import Action
from tree import Tree
from string import ascii_uppercase
import re
from itertools import combinations, permutations

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
        self.state = self.puzzle.pz_blank_puzzle_array
        self.root = Tree(parent=None)
        self.root.assignState(self.state)
        self.root.utility = 0


    def checkActionInThere(self,actions):
        for action in actions:
            pass
    
    def pruneActions(self,actions,key):
        '''
        '''
        wordIndex = []
        actionIndex = []
        for i in range(len(actions[0])):
            if key in actions[0][i].y:
                actionIndex.append(i)
                wordIndex.append(actions[0][i].y.index(key))
        idxList =[]   
        tempActions = []
        for z in range(len(actions)):
            charLst = []
            for m in range(len(actionIndex)):
                char = actions[z][actionIndex[m]].x[wordIndex[m]]
                charLst.append(char)
            if len(set(charLst)) == 1:
                tempActions.append(actions[z])
           
            

                    
        return tempActions
    
    def formMultiActions(self,pa,node):
        '''
        Take the list of actions and form them into multiple actions
        '''
        lettersUsed =  []
        possibleActions = []
        the_Ys = list(set([action.y for action in pa]))
        the_Ys.sort()
        the_Xs =list(set([action.x for action in pa]))
        perms = list(permutations(the_Xs, len(the_Ys)))
        # Take a look at the Ys.
        # Are the letters all unique 
    
        for item in perms:
            multiAction = []
            append = append = True
            for i in range(len(item)):
                multiAction.append(Action(item[i],the_Ys[i]))
            possibleActions.append(multiAction)

        # Narrow actions further
        lf = {}
        for wd in the_Ys:
            for char in wd:
                if char not in lf:
                    lf[char] = 1
                else:
                    lf[char] += 1
        newPossibleActions = []
        for key in lf:
            if lf[key] > 1:
                ## Duplicate Letters
                possibleActions = self.pruneActions(possibleActions,key)

                # Now we need to 
                
        return possibleActions 
    
    
    def getPossibleActions(self,searchWords,node):
        '''
        Pass in a list of words of the same length to try in locations in the puzzle
        searchWords :: actual words that correspond words of the same length
        in the puzzle
        node :: We need to know the current state so we can take appropriate actions.            
        '''
        possibleActions = []

        # Assume all words will be the same length
        # It's my design 
        word_length = len(searchWords[0])

        wordsInPuzzle=[]
        for word in self.puzzle.pz_words_as_array_without_punctuation:
            if len(word) ==  word_length and word not in wordsInPuzzle:
                wordsInPuzzle.append(word) # more of a character
        for key in searchWords:
            #if key not in x_actions_taken:
            for key2 in wordsInPuzzle:     
                if key != key2:
                    possibleActions.append(Action(x=key,y=key2))

        if len(wordsInPuzzle) > 1:
            # There are more than one of the words of this length so need to combine
            possibleActions = self.formMultiActions(possibleActions,node)
        #print("{}".format(len(possibleActions)))
        return possibleActions
    
    
    def anyLetterInWord(self,word):
        '''
        Check to see if letters are in the word 
        '''
        return any([a in ascii_uppercase for a in (list(word))])
    
    def returnRegExp(self,word):
        '''
        Generates the regular expression for the word so we can search for it
        '''
        regex = ''
        for char in list(word):
            if char in ascii_uppercase:
                regex += char.lower()
            elif char == "'": # For apostrophe words
                regex += char
            else:
                regex += "."
        return regex
                
    
    def utilityMeasure(self,tree):
        '''
        '''
        d = enchant.Dict('en.US')
        utilityScore = 0
        tokenizer = RegexpTokenizer(r"[\w']+") ## The \w' will leave in the apostrophe
        temp_word_list = tokenizer.tokenize(''.join(tree.state))
        for word in temp_word_list:
            index_list =[]
            if self.anyLetterInWord(word):
                    rgx = re.compile(self.returnRegExp(word))
                    possible_words = list(set([wd.lower() for wd in words.words() if len(wd) == len(word) and d.check(wd.lower()) and rgx.match(wd.lower())]))

                    utilityScore += len(possible_words)
        if type(tree.action) != list:
            tree.action.utility = utilityScore            
        else:
            for act in tree.action:
                act.utility = utilityScore
        tree.utility= utilityScore
    
    def takeMultiAction(self,actions,node):
        
        tree = Tree(parent=node)
        tree.action = actions
        tree.assignState(self.state)
        for action in actions:
            for i in range(len(self.state)):
                ## More letters now need to do by character
                for char in action.y:
                    if char in tree.state: 
                        print("This letter used so can't use it again {} from {}".format(char,action.y))
                        break # Don't use this word            
                    elif self.puzzle.pz_array[i] == char and tree.state[i] not in ascii_uppercase:
                        tree.state[i] = action.x[action.y.index(char)]
        
        if len(node.children) > 0:
            for nd in node.children:
                if not any([nd.state == tree.state for nd in node.children]):
                    self.utilityMeasure(tree)
                    node.addChild(tree)
        else:
            self.utilityMeasure(tree)
            node.addChild(tree)

    
    def takeAction(self,action,node):
        if type(action) == list:
            self.takeMultiAction(action,node)
            return
        
        tree = Tree(parent=node)
        tree.action = action
        tree.assignState(self.state)
        for i in range(len(self.state)):            
            if self.puzzle.pz_array[i] == action.y:
                tree.state[i] = action.x
        self.utilityMeasure(tree)         
        node.addChild(tree)



if __name__ == "__main__":
    puzzle = Puzzle('data/pz1.txt')
    agent = Agent(puzzle=puzzle)
    
    print("pause")
    