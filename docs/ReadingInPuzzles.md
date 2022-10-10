# Reading in Puzzles

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