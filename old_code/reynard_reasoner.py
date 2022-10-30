'''
Reynard Reasoner - used by the agent to reason about the puzzle
The concept is to take the puzzle and then reason about each word.
This can be used in constructing Bayesian networks that can lead to 
solutions.

Potentially dynamic solutions based on what is being reasoned about.
This would certianly arm the agent with more information that a 
human counterpart would have.

Anthony Sheller
Reasoning Under Uncertainty
EN.605.745

'''

import nltk # Natural Language Toolkit
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import words
import reynard_constants
import os
import collections
import re

class Reasoner:
    '''
    
    
    '''
    def __init__(self):
        pass
    
    
    def createWordSearcher(self,word_lengths):
        '''
        We are going to process the puzzle and get word suggests that can lead to letter suggestions.
        Take the word 
        '''
        self.wordSearchLists = {}
        for key in word_lengths:
            self.wordSearchLists[key] = [word for word in words.words('en') if len(word) == key]
        print("pause")
        
    def getWordsWithGivenPattern(self, re_exp,word_length):
        '''
        Need to narrow down words that are produced
        
        Given a regular expression find the words
        '''
        returnMe = [w for w in self.wordSearchLists[word_length] if re.search(re_exp,w)  ]
        return returnMe
    

    def letterFrequencyAnalysis(self,lf):
        '''
        Analyze the frequency and see if it matches up to what we said.
        '''
        letterprobs = {}
        summed = 0
        for key in puzzle.pz_letter_freqeuncy.keys():
            summed += puzzle.pz_letter_freqeuncy[key]
        for key2 in puzzle.pz_letter_freqeuncy.keys():
            letterprobs[key2] =  puzzle.pz_letter_freqeuncy[key2]/summed
        sorted_probs = sorted(letterprobs.items(), key=operator.itemgetter(1),reverse=True)
        return dict(sorted_probs)

        
    
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
        