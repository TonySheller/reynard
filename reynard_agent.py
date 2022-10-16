'''
This python module will create an agent.

The agent is being constructed in a separate module for 
compactness and separation of concerns (agent from data)
'''

import pyAgrum as gum
from reynard_constants import letter_frequency, two_letter_word_frequency
from reynard_puzzle import Puzzle

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
        while goal < 1:

            # If we have one and two letter words then we should try this initial stratedgy
            if 'OneTwo' not in triedStrategies:
                self.bayesNetOneTwo()
            
            
    def bayesNetOneTwo(self):
        '''
        This is pretty rudimentary to start but assume that there are one letter words and two letter words.
        Given A or I as the most likely one letter words.  What can we say about the two letter words and the follow on to that.  
        This is my first Bayes net
        
        '''
        # First, are there any one letter words?
        # Check the lettpass
        
        # The bayes network variable will be called fl and have two options
        # Create Wrapper around the Bayesian Network
        self.bn=gum.BayesNet('cryptogram Solver')
        # Create the startNode, this method takes the name, description and the possible values it can be
        self.bn.add(gum.LabelizedVariable('OneLetterWords','Are there any one letter words?',['A','I']))
        # Assign Initial Probabilities
        self.bn.cpt('OneLetterWords').fillWith([0.5297,0.4703]);
        # Add next Layer
        # 1. Create LabeleliedVariable
        self.bn.add(gum.LabelizedVariable('TwoLetterWords','Are there any two letter words?', two_letter_word_frequency))
        # 2. initialize two arrays to all zeros as only two letter words that begin with A or I matter
        temp_probsA = [0 for i in range(len(two_letter_word_frequency)) ]
        temp_probsI = [0 for i in range(len(two_letter_word_frequency))]
        # 3. Iterate through list of words and assign the ones that begin with A or I a probability based on
        #    the second letter value. 
        for i in range(len(two_letter_word_frequency)):
            if two_letter_word_frequency[i].startswith('A'):
                temp_probsA[i] = letter_frequency[two_letter_word_frequency[i][1]]
            elif two_letter_word_frequency[i].startswith('I'):
                temp_probsI[i] = letter_frequency[two_letter_word_frequency[i][1]]
        # 4. Calculate Lists of Probabilities
        probsA = [x/sum(temp_probsA) for x in temp_probsA]
        probsI = [y/sum(temp_probsI) for y in temp_probsI]
        # 5. Add Arc from OneLetterWords to Two LetterWords
        self.bn.addArc('OneLetterWords','TwoLetterWords')
        # 6. Assign probabilities to TwoLetterWords
        self.bn.cpt('TwoLetterWords')[:]= [probsA,probsI]
        # 7. Create the inferrence engine 
        self.oneTwoIE = gum.LazyPropagation(self.bn)
        


 
    def goalMeasure(self):
        '''
        The idea is to have a measure of the solution
        this can be 
        '''
        pass
    
    
    def nLetterWords(self,n=1):
        '''
        Check for n letter words
        return all indexes of one letter words.
        '''
        # return the letter that's there and the index. This could be more than one. so need to be careful
        returnMe = [wd for wd in agent.puzzle.pz_words_as_array_without_punctuation if len(wd) ==n]
        
        

    
def main():
    agent = Agent()
    #agent.bayesNetOneTwo()
    agent.reason()
    print("tada")

if __name__ == "__main__":
    main()