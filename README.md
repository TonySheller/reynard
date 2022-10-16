# Reynard

## Overview 
Reynard is a project that utilizes an agent or agents to reason over cryptograms. The purpose of this project is to delve into artificial intelligence and how reasoning can be used to solve this type of problem.  This specifically focuses on reasoning.  Natural language processing may be involved in the solution as well.  The intent is to learn more about reasoning in AI by working on an interesting project.

Bayesian Networks, decision graphs, Monte Carlo tree search, natural language processing are types of AI that will be explored and used.

## Project Structure
The project contains the following subfolders:
- **data** -- This folder contains the data or puzzles used in this project. 
- **docs** -- Documentation on the development, analysis and implementation of this work.  It will be useful when writing a paper.
- **images** -- Images if they are going to be used. 
- **jupyter** -- Contains several Jupyter notebooks being used in the development of this work.
- **tests** -- Unit Tests used to run and evaluate the correctness of the project.

The project contains the following files
- *requirements.txt* A python list of modules that should be installed for the project
- *reynard_agent.py* A python module that represents the agent that will be reasoning about the puzzles.
- *reynard_constants.py* A python module that contains lists of values such as letter and word frequencies
- *reynard_puzzle.py* A python module that reads in the puzzle from a text file and creates a list of statistics about the puzzle.
- *reynard_reasoner.py* A python module that is specific to reasoning over the cryptograms.


## Concept on approaches
The concept will be to create several strategies that the agent will need to try to move forward in a puzzle.

1. oneTwo -- If there are one and two letter words work with them first.
2. Frequency Analysis -- Look at the frequency of existing letters and how that 
3. Use word suggestion with pyenchant.
4. Other approaches.

It's going to take a few solutions to get to the final solution




References:
Cryptograms Special, November 2022 Issue, Kappa Publishers, www.kappapuzzles.com