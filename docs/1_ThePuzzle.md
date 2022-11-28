# The Puzzle

## Overview
This is a summary of what was done to read in the puzzle.  Reading in a puzzle is very straightforward, however a puzzle has attributes that will form a knowledge base for the agent to work with. One might say that an agent
should calculate these, it will, when it turns the page and sees the puzzle. Like some puzzle solvers it will systematically start solving it by, potentially looking for one letter words and seeing how A and I fill out the puzzle.   

The following attributes of a puzzle are generated:
1. Puzzle as a string
2. wordsWithPunctuation (may remove this as its not useful)
3. words without punctuation -- useful but may transform so it includes apostrophe words.
4. Letter Frequency
5. Word Frequency
6. Word Lenght Frequency
7. Are there Apostrophes (Really thinking about removing this as part of 2,3 above)
8. BlankPuzzle
9. DoubleLetterCheck -- nice to know -- can make assumptions about words
10. WordCounts -- are there repeats.
11. Pattern words -- for words in the puzzle.  Are there words that have letters that repeat, other than double letters. for example the word, 'that' has two 't' in it.  Other pattern words include PEOPLE, ELEVEN, LEGALLY, ILLEGALLY, SELLS, 

A method that shows that puzzle is also provided.

## Notes
These are some notes I put in for reference.

To read in the puzzle and tokenize down to words.
 - conda install -c anaconda nltk
 This may have been done if requirements.txt file was used as input.

```
import nltk
file_content = open("myfile.txt").read()
tokens = nltk.word_tokenize(file_content)
print tokens
```


Reference:
[StackOverflow :: How to tokenize natural English text in an input file in python?](How to tokenize natural English text in an input file in python?)
[StackOverflow :: How to get rid of punctuation using NLTK tokenizer](https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer)