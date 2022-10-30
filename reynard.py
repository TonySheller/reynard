'''

Define a recursive algorithm that will start with word length 1, 2, 3, 4 and go on from there

It will 
'''

from reynard_puzzle import Puzzle
from reynard_constants import *

#This is a dictionairy of letters to the ones they represent
precepts = []



def substitute(puzzle,this,that):
    '''
    Function to generally substitute a letter into a puzzle a
    '''
    # Assign blank value of that to this.
    puzzle.pz_key[that] = this
    # Replace all the letters in the blank puzzle with a '_'
    puzzle.pz_blank_puzzle = ''
    for i in range(len(puzzle.pz_as_string)):
        if puzzle.pz_array[i] == that:
            puzzle.pz_blank_puzzle_array[i] = this
    for char in puzzle.pz_blank_puzzle_array:
        puzzle.pz_blank_puzzle += char  
      
    return puzzle

def undo(puzzle,undoThis):
    '''
    Function that will undo the move 'undoThis' and restore the puzzle to normal.
    '''
    # Get the this and that we want to use
    this = list(undoThis.keys())[0]
    that = undoThis[this]
    position = list(puzzle.pz_key.keys()).index(that)
    puzzle.pz_blank_puzzle = ''
    for i in range(len(puzzle.pz_as_string)):
        if puzzle.pz_array[i] == that:
            puzzle.pz_blank_puzzle_array[i] = '_'
    for char in puzzle.pz_blank_puzzle_array:
        puzzle.pz_blank_puzzle += char  
    return puzzle


def oneTwoStrat(puzzle,this,that):
    '''
    
    Note: This may or may not work all the time.  :-/  
    Why? Words are strange
    
    Embodies the one two strategey
    A is more frequent so we'll go with it first.
    
    We are replaceing "this" for "that"
    '''
    # substitute this for that
    puzzle = substitute(puzzle, this, that)
    precepts.append({this:that})
    
    if len([word for word in puzzle.pz_words_as_array_without_punctuation if len(word)==2 and word[0]== that]):
        print("words begining with our character {}".format(that))       
    # We have no two letter words that begin with the character we were looking for
    else:
        # Let's try I in the same spot
        undo(puzzle, precepts.pop())
        substitute(puzzle, 'I', that)
        precepts.append({this:that})
        if len([word for word in puzzle.pz_words_as_array_without_punctuation if len(word)==2 and word[0]== that]):
            print("words begining with our character {}".format(that))
        else:
        # A is still our best bet
            undo(puzzle, precepts.pop())
            substitute(puzzle, 'A', that)
            precepts.append({this:that})
        
            
                
                
                         
                
                #then we have a 2 letter word that begins with A
                
     
    
    return 0


def makesSense(puzzle):
    
    '''
    How to do this?
    '''
    

    return 0
    



def one_letter_words(puzzle):
    '''
    Start with one letter words and then go to two letter words.
    
    In the case where there are two, we will get the two letters
    and which ever is the most frequent we will assign A to. I will be assigned to the other. 
    
    '''
    # Do we have any one letter words?
    if 1 in puzzle.pz_word_lengths_freqeuncy.keys():
        #yes we do
        # How many one letter words?
        if puzzle.bothAandI():
            # Ack we have both A and I in the puzzle
            # Get the unique one letter words
            pass
        # So there is only a one letter word
        else:
            # Get one letter word to be substituted
            sub_me = [ab for ab in puzzle.pz_words_as_array_without_punctuation if len(ab) ==1][0]
            measure = oneTwoStrat(puzzle,'A',sub_me)
            
            
            
def frequencyStrategy(puzzle):
    '''
    Given our puzzle can we try a recursive way of doing things
    '''
    for letter in 
    
    

def main():
    '''
    
    '''
    puzzle = Puzzle('data/pz1.txt')
    
    print("pause")
    ## So we have the puzzle read in.
    ## Are there any one letter words?
    one_letter_words(puzzle)

if __name__ == "__main__":
    main()