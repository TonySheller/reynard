# The Agent
## Overview
The concept of the agent will be based on the work of Poole and Mackworth (1). Their work focuses on the agent's ability to reason. Likewise the work of Russel and Norvig provide good insight as well as 

## Design Considerations
The Bayesian network will be constructed based on the length of words. One cannot assume that a phrase will have one letter words to start so will need to build the Bayes Net based on the statistics of the puzzle. In resarching solutions, I came across PyAgrum which is nice to use and pretty well maintained.  It has some very recent code updates and nice features for displaying Bayesian Network (Dags).

## Assume there are one letter words.
The first test puzzle does include one letter words.  So as far as design and implementation I'll assume that its there.  The probability that a 1-letter word is either A or I is 100% (assume this). but the probability of A or I will not be 50%. It'll be taken from the table of constants in `reynard_constants.` The frequency of A is 0.084966, while the frequency of I is .075448. Then:

$$P(A) = {{0.084966} \over {(0.084966+0.075448)}} = .5297$$ 
$$P(I) = {{0.075448} \over {(0.084966+0.075448)}} = 0.4703$$

We can start our Bayes Net with these assignments. 

The second layer of this Bayes Network will assume two letter words are present, and they are in the trial case.  But if they weren't then we would probably not do three as there are over 1500. But we can narrow that down given a letter or two. 

This one to two letter word attack pattern may end with just that: Given A or I how many two letter words are possible. 
This small effort feeds into a more complex idea where the agent reasons about word possibilities based on some of the statistics
provided in the reynard_constants.


## References:
1. Poole, D., Mackworth, A. (2017). Artificial Intelligence: Foundations of Computational Agents. Cambridge, UK: Cambridge University Press. ISBN: 978-0-521-51900-7
2. Russel, Stuart and Norvig, Peter, Artificial intelligence—a modern approach  , Englewood Cliffs, NJ.: Prentice Hall., 2021, .



 