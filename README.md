# UCSF PSPG Computational Drug Discovery Workshop
*Please read through the directions thoroughly and then move on to setting up your working environment.*

In this workshop you will:

1. Work with RDKit to practice reading molecules and generating molecular fingerprints
2. Build a model that uses chemical structure to predict protein target profiles
3. Predict which protein targets potential cancer drugs bind
4. Repeat steps 3 and 4 with a neural network to compare results across different ML methods.

---

*thank you to [@gtgask](https://github.com/gtgask) for putting this script together in 2017*  
*moved to `python 3.9` in 2021 by [@wconnell](https://github.com/wconnell)*  
*updated 2023 by [@laurashub](https://github.com/laurashub) and [@ghorbanimahdi73](https://github.com/ghorbanimahdi73)*

The overall goal of this workship is (1) to gain experience with computational tools such as Python, conda, Jupyter notebooks, and (2) apply machine learning methods to the DTP-NCI60 cancer drug screening dataset (https://dtp.cancer.gov/discovery_development/nci-60). The NCI60 dataset consists of approximately 27k compounds screened against 60 individual cancer cell lines, originating from 10 tissue subtypes. 

Slides available [here](https://docs.google.com/presentation/d/1W4rIua1Z5v-R2DaMrXnbc6X9lPkZOLPNmqgAVZ7n7HA/edit?usp=sharing).

### Data
`cancer_compounds.sample.csv`
- This file can be opened in Excel, or a simple text editor, and contains the SMILES and names or IDs of various cancer-related compounds.
- **It demonstrates the file format for to be used for the query drugs as input to the "Predict" notebook.**

`chembl_21_binding_molecules.csv.gz`
- This file contains: Chembl_ID, SMILE, Fingerprint
- **The code requires this file to be gzipped, but you can explore this file by unzipping into a new file: `gunzip -c chembl_21_binding_molecules.csv.gz > chembl_21_binding_molecules.csv`**

`chembl_21_binding_targets.csv.gz`
- This file contains: Target ID, UniProt Name, Molecule IDs, Description
--**The code requires this file to be gzipped, but you can explore this file by unzipping into a new file: `gunzip -c chembl_21_binding_targets.csv.gz > chembl_21_binding_targets.csv`**

## Part 1: Setting up your Python environment and notebooks
This workshop will be conducted entirely in Python, a programming language with broad scientific use. We will be using a number of packages, including scikit-learn and Pytorch for model training, as visualization libraries such as matplotlib and seaborne. 

### Setting up our Working Environment
Let's create a directory for us to work from. This directory is where we will store all the files we plan to use.

First clone this repository on your local computer by opening a terminal window and typing:
    
    cd ~/Documents
    git clone git@github.com:laurashub/PSPG-CDD.git

### Install Miniconda and Additional Packages
Conda (and miniconda) is an environment management system that will help us to install packages and resolve dependencies. If you do not have Conda installed, install the latest version of Miniconda for you OS from here: https://docs.conda.io/en/latest/miniconda.html

Once Miniconda has been installed, close your terminal window, and reopen another one. Check to see conda was installed correctly. Type the following command to see the list of packages that were installed.

    conda list

### Create and Activate a new Conda Environment
Now that we have the infrastructure in place, we need to create a new conda environment, and install the additional packages, such as rdkit and jupyter, we will need to generate our predictions.

Create a new environment using the following code:

    cd PSPG-CDD/ # change location to PSPG-CDD directory
    conda env create -f environment.yml # create environment 'cdd_workshop'
    
Activate the environment and confirm:

    conda activate cdd_workshop # activates our installed environment and gives us access to included packages
    conda env list # list of installed environments - should see * beside cdd_workshop

### Using our created environment in a jupyter notebook

For this workshop, we will be using an interactive Python session with Jupyter notebooks. This opens notebook files (.ipynb extensions) inside a web browser that can be run manually, as opposed to creating a single .py file that is run all at once. First, we need to make the conda environment we created available to Jupyter with the following command:

    ipython kernel install --user --name=ccd_workshop 

### Start a Jupyter Notebook Session
To test if everything is working, let's open up a jupyter lab session. We'll import the modules we need to run our scripts correctly.

    cd WorkshopNotebooks
    jupyter notebook

This should bring up a jupyter notebook session that is being hosted from your local machine in your browser. Open `PSPG245B-NaiveBayes-Classification-STUDENTS.ipynb` and try running the import cell by either hitting Shift+Enter or clicking "Run" at the top of the screen. If everything is set up correctly, that should throw no errors.


## Part 2: Cheminformatics exploration, ML Model Training
In this workshop, you will use machine learning tools from scikit-learn (aka sklearn, http://scikit-learn.org) along with chemical fingerprinting and visualization tools from RDKit (http://rdkit.org) to predict the protein targets of cancer-related compounds. This workshop uses two Python notebooks that are mostly complete. Your job is to fill in the missing sections and use these notebooks to explore the protein (target) profiles of these cancer-related compounds. Your goal is to decide which compound(s) are most applicable to your tumor for treatment and then predict which protein targets these compounds will bind.


### 2a. Naive Bayes Classification notebook

`PSPG245B-NaiveBayes-Classification-STUDENTS.ipynb`

This notebook explains common molecular formats such as SMILES and molecular fingerprint as well as molecular similarity calculations using the RDKit package. In addition, this notebook takes in a file containing compounds (SMILES), along with two reference files containing data on molecules and targets from ChEMBL. It loads the data, converts the SMILES into in-memory representations of molecules, calculates chemical fingerprints from them, and trains a machine-learning method called a Naïve Bayesian Classifier to predict the drug targets of each compound.

http://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes

Some parts of the script are incomplete, and these are marked with question marks (?). It is your job to fill them in.

### 2b. Neural network Classification notebook

`PSPG245B-NeuralNetwork-Classification-STUDENTS.ipynb`

This notebook is similar to the later part of 2b, except instead of using a neural network this notebook demonstrates how to setup and train a deep neural network using the PyTorch library. It details setting up the Datasets and DataLoaders, defining the model architecture, and evaluating performance. It also shows how to apply the model to get predictions for novel compounds to compare predictions between the two different classification methods.

https://pytorch.org/docs/stable/index.html

The script is largely complete, but there are directions to follow and questions to answer.

