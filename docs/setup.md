# Setup

## Python virtual development environment
First setup a Python virtual environment. Using virtual environments lets one install modules and  even different versions of Python with orinary user privledges.

[Anaconda](https://www.anaconda.com/products/distribution) is the Python environment used for this project. This is not necessary, however Anaconda does make it very easy to start over with a new version of Python or a new set of modules if necessary. Follow the [installation instructions](https://docs.anaconda.com/anaconda/install/index.html) provided by Anaconda.

## Create A virtual environment
Call it whatever you like, it's just a namethat can help calrify what the environemnt is for. `conda` is the command line tool (CLT) used for this.  
```
conda create reynard
```

## Activate the virtual environment
Virtual environments are great for seperating projets or trying out configurations. A developer can have dozens of these. Each can be `activated` and `deactivated`.
```
conda activate reynard
```
`Ipython` is a powerful command line tool for working with Python.  Install that now.
```
conda install ipython

... stuff happens and select yes when it asks

asheller@neuron:~$ conda activate reynard
(reynard) asheller@neuron:~$ ipython
Python 3.8.8 (default, Apr 13 2021, 19:58:26) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.31.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 

```
It's always useful to be able to work from a python command line when developing, debugging, or exploring a new concept.

## Modules
You will need to install a few python modules

### Jupyter Lab
This would have installed Ipython. But knowing about Ipython is valuable.  It's 10 times better than an ordinary Python prompt.  To install Jupyter-Lab, another powerful Python development resource, do the following: 

```
conda install -c conda-forge jupyterlab

```
This is similar to having Ipython in a web-page.  One launches it by typing `jupyter-lab`. It's another, very useful Python tool.

### NLTK
The Natural Language Tool-Kit -- I am so thankful for this amazing Python Module. There are a few extra steps in the procedure for configuring the NLTK for use. 
```
conda install -c conda-forge nltk
....
... stuff ...
... more stuff ...
...stuff...

ownloading and Extracting Packages
regex-2022.10.31     | 441 KB    | ##################################### | 100% 
nltk-3.6.7           | 1.1 MB    | ##################################### | 100% 
tqdm-4.64.1          | 82 KB     | ##################################### | 100% 
click-8.1.3          | 74 KB     | ##################################### | 100% 
colorama-0.4.6       | 25 KB     | ##################################### | 100% 
joblib-1.2.0         | 205 KB    | ##################################### | 100% 
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Retrieving notices: ...working... done
(reynard) asheller@neuron:~$ 





```

### Pyagrum 