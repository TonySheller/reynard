# The Agent
## Overview
The concept of the agent will be based on the work of Poole and Mackworth (1). Their work focuses on the agent's ability to reason. Likewise the work of Russel and Norvig provide good insight as well as 

## Design Considerations
The Bayesian network will be constructed based on the length of words. One cannot assume that a phrase will have one letter words to start so will need to build the Bayes Net based on the statistics of the puzzle. In resarching solutions, I came across PyAgrum which is nice to use and pretty well maintained.  It has some very recent code updates and nice features for displaying Bayesian Network (Dags).

### Bayesian and Decision Networks
Designing a Bayesian or decision network for this problem turned out to be very challenging. Some initial work was done with PyAgrum.  The nature of what the Bayesian network is doing is *embodied* in the process used. 

#### Monte Carlo Tree Search (MCTS)
MCTS was experimented with but capturing the correct Utility function proved difficult.  It's concept did provide the insight that a focus on the Utility

## Final Design
The final agent uses a tree data structure combined with a utiliy function that evaluated whether a letter or word assignment added value (utility) to the puzzle.  It did this by seeing if words were formed.  Trying words will certainly cause utility to increase. At the same time assigning an incorrect word can cause other words in the cryptogram to be incorrect and lower the utility.


## References:
1. Poole, D., Mackworth, A. (2017). Artificial Intelligence: Foundations of Computational Agents. Cambridge, UK: Cambridge University Press. ISBN: 978-0-521-51900-7
2. Russel, Stuart and Norvig, Peter, Artificial intelligence—a modern approach  , Englewood Cliffs, NJ.: Prentice Hall., 2021, .



 