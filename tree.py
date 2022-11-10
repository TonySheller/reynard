


from copy import deepcopy
import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words
import enchant
from threading import Thread
import re
from string import ascii_uppercase

class Tree(Thread):
    def __init__(self,parent=None,state=None):
        Thread.__init__(self)
        self.children = []
        self.parent = parent
        self.state = state
        self.utility = 0
        self.game_state = []
        self.letter = {}

        
    def run(self):
        self.utilityMeasure()
    
    def addChild(self,child):
        self.children.append(child)
        
    def addChildren(self, children):
        self.children = children
        
    def assignState(self,state):
        self.state = deepcopy(state)
        
    

        
if __name__ == "__main__":
    pass
    