'''
Reynard BN came about after gaining further understanding of the Bayesian networks
and having worked with argum a little things are starting to come clear or less murky.


There are 25 Variables at most to be defined.  This is dependent on the puzzle itself
because not all letters of the alphabet will be used.

So given the alphabet what character was substitutued for it?  That string is what 
I'm trying to solve for.

We have to make an initial guess but its an informed guess.  We have *evidence* that certain 
letters come before others: ETAOIN are the top letters.  I have a complete distribution in
the reynard constants Python Module, this will provide the probability distribution for the variables
variable.

This module will handle the construction of the Bayesian Network Used by Reynard
 

Anthony Sheller
Reasoning Under Uncertainty
EN.605.745

'''

import reynard_constants
import pyAgrum as gum
from reynard_constants import letter_frequency_wiki as lf

class ReynardBN:
    '''
    A Bayesian Network 
    
  
    
    '''
    def __init__(self):
        '''
        Constructor used to generate the node
        
        takes a Bayesian Network to assign Nodes to
        
        '''
        self.bn =  self.bn=gum.BayesNet('Reynard')
        self.nodeList = []


    def theRoot(self):
        '''
        Every node is required to have a name that is different
        '''
        # Start out with Are there one letter words
        # We can introduce evidence here and take it forward
        self.bn.add(gum.LabelizedVariable("one letter words","Are there one Letter Words used?",2))
        self.bn.add(gum.LabelizedVariable("E as most frequent","Does 'E' make sense as a substitute?",2))
        self.bn.add(gum.LabelizedVariable("A or I","Choose A or I for the one letter position",['A','I']))

        self.bn.addArc("one letter words","E as most frequent")
        self.bn.addArc("one letter words","A or I")
        
        self.bn.cpt("one letter words").fillWith([lf['A'] + lf['I'],1-(lf['A'] + lf['I'])])
        self.bn.cpt("E as most frequent")[{"one letter words":0}] =[1-lf['E'], lf['E']]
        prob_A = lf['A']/(lf['A']+lf['I'])
        prob_I = lf['I']/(lf['A']+lf['I'])
        self.bn.cpt("A or I")[{"one letter words":1}]= [prob_A,prob_I]

    def twoLetterWordStartsWithA(self):
        '''
        Given that we have a singleletter Does it start A
        AT, AS, AM most likely.
        '''
        self.bn.add(gum.LabelizedVariable("two letter words starts with A?","This is likely an S,N, or an M but were just asking",2 ))
        self.bn.addArc("A or I","two letter words starts with A?") 
        self.bn.cpt("two letter words starts with A?")[{"one letter words":1,"A or I":'A' }] = [0.1,0.9] # I would say they are very frequent but can't find a source
        
        self.bn.add(gum.LabelizedVariable("an, as, am, at","",['n','s','m','t'] ))
        self.bn.addArc("A or I","two letter words starts with A?") 
        self.bn.cpt("two letter words starts with A?")[{"one letter words":1,"A or I":'A' }] = [0.1,0.9] # I would say they are very frequent but can't find a source
        
        
        # Now add the two letter  words

if __name__ == '__main__':
    pass
        