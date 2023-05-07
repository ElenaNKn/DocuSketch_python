# **Solution of a test task for DocuSketch**  
   
## **Table of contents:**  
   
- [About the repository](#about-the-repository)   
- [Structure of the project](#structure-of-the-repository)   
- [Requirements](#requirements)  
- [Virtual environment and running the notebook](#virtual-environment-and-running-the-notebook)  
- [Contacts](#contacts)   

## **About the repository**   

This repository contains a solution for the test task for a python internship at DocuSketch.

## **Structure of the repository**    
   
The repository contains the next files and folders: 
* `README.md` - project documentation    
* `requirements.txt` - information about ibraries, that are needed to run the project files    
* `Pipfile` and `Pipfile.lock` - files to install a virtual environment for the project    
* `Notebook.ipynb` - a notebook to run a module `my_plot.py`, which was created within the project   
* `my_plot.py` - a python module, that contains a class, which was created according to test task requirements    
* `deviation.json` - json file with a dataset for the project
* `plots` - a folder, where created plots are to be stored

## **Requirements**

This project was written in python_version = "3.10"

Packages and libraries, which are needed to run project files:
pandas
seaborn
numpy
matplotlib

One can install these libraries (with pip or Anaconda etc.) or install virtual environment (as descripted below) and run project files there.

## **Virtual environment and running the notebook**

Virtual environment of the project is provided by `Pipfile` and `Pipfile.lock`. These files contain all information about libraries and dependencies for the project. To create a virtual environment with libraries and dependencies required for the project, one should install `pipenv` library:  
   
`pip install pipenv`   
   
Then it's necessary to clone this repository from GitHub, open a terminal in the folder with this repository, and run the following commands:   
   
`pipenv install`   # to install project virtual environment

This virtual environment is also used for `Notebook.ipynb` file. To open this file one should enter all previous commands and then start Jupyter Notebook by entering the next command in a terminal (command window):  
    
`pipenv run jupyter notebook`   
   
Then one can find `Notebook.ipynb` file, open and run it. This approach alows to run module `my_plot.py` within `Notebook.ipynb`.

## **Contacts**   
   
If you have any suggestions or comments about this project, please contact me via LinkedIn (https://www.linkedin.com/in/alena-kniazeva-a907bb197/ ) or email (elena.n.kniazeva@gmail.com).  