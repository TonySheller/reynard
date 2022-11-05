class Action:
    def __init__(self, x, y):
        '''
        We can think of an action as a letter assignment. 
        For every letter in the puzzle it could take on 1 of 25
        possible values.  
        '''
        self.x = x
        self.y = y
        self.utility = 0
    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.x == other.x and self.y == other.y 

    def __hash__(self):
        return hash((self.x, self.y))