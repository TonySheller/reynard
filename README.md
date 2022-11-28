# Reynard

## Overview 
Reynard is a project that utilizes an agent to reason over cryptograms. The purpose of this project is to delve into artificial intelligence and how reasoning can be used to solve this type of problem.  This specifically focuses on using reasoning under uncertainty.  Natural language processing may be involved in the solution as well.  The intent is to learn more about reasoning in AI by working on an interesting project.


## Project Structure
The project contains the following subfolders:
- **data** -- This folder contains the data or puzzles used in this project. 
- **docs** -- Documentation on the development, analysis and implementation of this work.  It will be useful when writing a paper.

- **jupyter** -- Contains Jupyter notebooks being used in the development of this work.
- **tests** -- Unit Tests used to run and evaluate the correctness of the project.

The project contains the following files
- *requirements.txt* An Anaconda python list of modules that should be installed for the project
- *agent.py* A python module that represents the agent that will be reasoning about the puzzles.
- *reynard_constants.py* A python module that contains lists of values such as letter and word frequencies
- *puzzle.py* A python module that reads in the puzzle from a text file and creates a list of statistics 
about the puzzle.
- *tree.py* A python module defines a *tree* class to be used as *nodes* in the decision tree.


## Concept on approaches
The concept will be to create strategies that the agent will apply to move forward in a puzzle.
Review the [strategy](docs/strategy.md) for more information.




# Reference:
Cryptogram Puzzles are used from Cryptograms Special, November 2022 Issue, Kappa Publishers, www.kappapuzzles.com