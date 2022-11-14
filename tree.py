


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
        self.expand = True
        

        
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
    