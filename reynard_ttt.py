'''
Test the MCTS Concept


'''


from reynard_puzzle import Puzzle
from reynard_constants import *
from mcts import mcts
from copy import deepcopy
from functools import reduce
import operator

class NaughtsAndCrossesState():
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.currentPlayer = 1
    
    def getCurrentPlayer(self):
        return self.currentPlayer

    def getPossibleActions(self):
        possibleActions = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    possibleActions.append(Action(player=self.currentPlayer, x=i, y=j))
        return possibleActions

    def takeAction(self, action):
        newState = deepcopy(self)
        newState.board[action.x][action.y] = action.player
        newState.currentPlayer = self.currentPlayer * -1
        return newState

    def isTerminal(self):
        for row in self.board:
            if abs(sum(row)) == 3:
                return True
        for column in list(map(list, zip(*self.board))):
            if abs(sum(column)) == 3:
                return True
        for diagonal in [[self.board[i][i] for i in range(len(self.board))],
                         [self.board[i][len(self.board) - i - 1] for i in range(len(self.board))]]:
            if abs(sum(diagonal)) == 3:
                return True
        returnThis = reduce(operator.mul, sum(self.board, []), 1)
        return returnThis

    def getReward(self):
        for row in self.board:
            if abs(sum(row)) == 3:
                return sum(row) / 3
        for column in list(map(list, zip(*self.board))):
            if abs(sum(column)) == 3:
                return sum(column) / 3
        for diagonal in [[self.board[i][i] for i in range(len(self.board))],
                         [self.board[i][len(self.board) - i - 1] for i in range(len(self.board))]]:
            if abs(sum(diagonal)) == 3:
                return sum(diagonal) / 3
        return False


class Action():
    def __init__(self, player, x, y):
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

   
    
class Action():
    '''
    This is modeled after the tic-tac-toe example here: 
    https://github.com/pbsinclair42/MCTS/blob/master/naughtsandcrosses.py
    
    '''
    def __init__(self, player, x, y):
        '''
        Don't get hung up on this being two player.
        The idea is to solve the puzzle -- so maybe both x and y take turns and share
        the same knowlege base.
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
    initialState = NaughtsAndCrossesState()
    searcher = mcts(timeLimit=1000)
    action = searcher.search(initialState=initialState)

    print(action)    
    
    
'''
1. define the initial state which is the tictactoe board.
2. First player gets to choose the first move and usually selects (0,0)
3. That action is returned and the player can take the actions.

Step 3 is where the agent would come into play.  

In what I'm working 

'''