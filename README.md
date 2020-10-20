# pyntools
A set of python tools to ease every day life and computations on frioul the high performance computing cluster of the Institut de Neurosciences de la Timone (INT) in Marseille 
## Dependencies
Pyntools  relies only on packages included in Python standard libraries (see https://docs.python.org/3/library/) thus does not have any runtime dependency.
However its installation do require pip and setuptools.
## How to use ?
1. Clone the current repository:
````bash
git clone https://github.com/alexpron/pyntools.git 
````

If you want to be able to use functions of the frioul module the repoisitory must be cloned in a location accessible from frioul the head of the INT cluster (e.g. /hpc volume)

2. Go inside the pyntools local git reposiory and install it
````bash
pip install --user . 
````
Remark: to use functions of the frioul module this operation must be performed from frioul the head of the INT cluster not from the nodes !

