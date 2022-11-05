from copy import deepcopy
class Tree:
    def __init__(self,parent=None,state=None):
        self.children = []
        self.parent = parent
        self.state = state
    
    def addChild(self,child):
        self.children.append(child)
        
    def addChildren(self, children):
        self.children = children
        
    def assignState(self,state):
        self.state = deepcopy(state)
        
if __name__ == "__main__":
    pass
    