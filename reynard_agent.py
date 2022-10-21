'''
This python module will create an agent.

The agent is being constructed in a separate module for 
compactness and separation of concerns (agent from data)
'''

import pyAgrum as gum
from reynard_constants import letter_frequency, two_letter_word_frequency
from reynard_puzzle import Puzzle
from reynard_reasoner import Reasoner

class Agent:
    '''
    This is the robot, prefer agent, that reasons its way through solving a cryptogram
    
    '''
    
    def __init__(self):
        '''
        Constructor
        Set Gaol as 0 aka not achieved.  1 will be achieved. This will be based on the percentage of the puzzle solved.
        '''
        self.experience = {} # May use a stack, linked list or something liek that
        self.goal = 0.0  #Goal is a measure of the puzzle 
        self.stackOfDecisions = [] # Lists make great stacks because they have a push and pop method
        self.lettersUsed =[] 
        self.puzzle = Puzzle('data/pz1.txt')
        self.reasoner = Reasoner()
    
    def reason(self):
        '''
        This method will use the infromation the agent has to decide on the first move.
        The approach will be to start with small letters and go up.
        The approach will also include the consideration of double letters.
        The agent will first reason about the situation.

        '''
        # A list of strategies that have been tried
        triedStrategies = []
        # Need to check that one or two letters are in the puzzle
        # if not then set the flag so the one two strategy isn't applied
        if 1 in self.puzzle.word_lengths_freqeuncy.keys() and 2 in self.puzzle.word_lengths_freqeuncy.keys():
            pass
        else:
            triedStrategies['oneTwo']
            
        # This will continue to loop reason over the puzzle. 
        while self.goal < 1:
            

            # If we have one and two letter words then we should try this initial stratedgy
            if 'OneTwo' not in triedStrategies:
                self.oneTwoStratedgy()
    
            break
        
        
    
         
    def oneTwoStratedgy(self):
        '''
        Givent that we have 
        '''
        # our starting guess
        guess = 'A'
        one_letter_word_locals = self.nLetterWords(n=1)
        # What do we do when there are more than one letter words. :-(
        replaceThis = ''
        for key in one_letter_word_locals.keys():
            replaceThis = key
            self.stackOfDecisions.append({'guess':guess,'value':key})
            for idx in one_letter_word_locals[key]:
                self.puzzle.pz_blank_puzzle_array[idx] = guess
            break #breakout afer only one key
        # Are there two letter words that start with A
        two_letter_word_starts_with_A = False
        for word in self.nLetterWords(n=2):
            if word[0] == replaceThis:
                two_letter_word_starts_with_A = True
                break
        ## If we start a letter with our Guess then we can use a small BN to forecast 
        ## second letter to use        
        if two_letter_word_starts_with_A:
            # Create the one Two Bayes Net and then 
            self.reasoner.bayesNetOneTwo()
            self.reasoner.oneTwoIE.setEvidence({"OneLetterWords":[1.0,0.0]})
            self.reasoner.oneTwoIE.makeInference()
            self.reasoner.oneTwoIE.posterior("TwoLetterWords")
            suggestion = two_letter_word_frequency[self.reasoner.oneTwoIE.posterior("TwoLetterWords")[:].argmax()]
            # This did not get evaluated on the first go so will need to work on it another way. 
        self.puzzle.showPuzzle()
        # Now ask ourself == are there any two letter words that begin with an a?
        #We do this because its 
        
        
        
 
    def goalMeasure(self):
        '''
        The idea is to have a measure of the solution
        this can be 
        '''
        pass
    
    
    def nLetterWords(self,n=1):
        '''
        Check for n letter words
        return all indexes of n-letter words.
        If it's a one letter word it will return the index of all letters that are the one letter word
        '''
        import re
        # return the letter that's there and the index. This could be more than one. so need to be careful
        returnMe  = {}
        n_letter_words = [wd for wd in self.puzzle.pz_words_as_array_without_punctuation if len(wd) ==n]
        print(n_letter_words)
        deduped_list = [*set(n_letter_words)]
        for item in deduped_list:
            returnMe[item] =[]
            for i in range(len(self.puzzle.pz_as_string)):
                if item == self.puzzle.pz_as_string[i]:
                    returnMe[item].append(i)

        return returnMe                    

    
    def getLetterToReplace(self):
        pass
    
def main():
    agent = Agent()
    #agent.bayesNetOneTwo()
    agent.reason()
    print("tada")

if __name__ == "__main__":
    main()