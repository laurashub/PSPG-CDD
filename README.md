# UCSF PSPG Computational Drug Discovery Workshop
*Please read through the directions thoroughly and then move on to setting up your working environment.*

In this workshop you will:

1. Find a breast cancer cell line that is representative of your tumor sample from the NCI-60
2. Analyze the NCI-60 screening dataset to select compounds that are potent against your cell line
3. Build a model that uses chemical structure to predict protein target profiles
4. Predict which protein targets your selected compounds bind
5. Analyze ligand profiles of targets (known binders) that commonly appear in your predictions to identify important chemical substructures 

---

*thank you to [@gtgask](https://github.com/gtgask) for putting this script together in 2017*
*moved to `python 3.9` in 2021 by [@wconnell](https://github.com/wconnell)*

## Part 1
The overall goal of this workshop is to apply machine learning methods to the DTP-NCI60 cancer drug screening dataset (https://dtp.cancer.gov/discovery_development/nci-60) to predict which compounds are most relevant for treatment given the tumor data provided to you. The NCI60 dataset consists of approximately 27k compounds screened against 60 individual cancer cell lines, originating from 10 tissue subtypes. 

In order to determine which compounds are optimal for treatment, you will need to identify which **breast cancer cell line** is most relevant to your tumor. Before the second portion of the workshop, your goal is to explore the datasets provided by the NCI60 and to make a decision on which cell line(s) to focus on. You will share how you made your decision.

### Exploring the Data
The NCI's genomics and bioinformatics group has created a web portal consolidating all the data and metadata related to the screen that is publicly available and convenient to access. The sites homepage is located here: https://discover.nci.nih.gov/cellminer/home.do We encourage you to examine the upper blue tabs, especially the ones labeled "Data Set Metadata", "Cell Line Metadata", and "Download Data Sets"

## Part 2
In this workshop, you will use machine learning tools from scikit-learn (aka sklearn, http://scikit-learn.org) along with chemical fingerprinting and visualization tools from RDKit (http://rdkit.org) to predict the protein targets of cancer-related compounds. This workshop uses two Python scripts that are mostly complete. Your job is to fill in the missing sections and use these scripts to explore the protein (target) profiles of these cancer-related compounds. Your goal is to decide which compound(s) are most applicable to your tumor for treatment and then predict which protein targets these compounds will bind. Then you will compare the chemical structures of compounds you would like to investigate to the ligands (known binders) of a protein target you would like to investigate.

Perform exploratory data analysis on your cell line to decide which compounds you would like to make target profile predictions for.

Explain common substructures or functional groups (“warheads”) that are present in the compound you choose and the most similar ligands for the predicted off-targets of this compound. Do these off-targets explain the compounds efficacy, it’s side effects, or perhaps a repurposing opportunity? Is there an experiment you would recommend to better understand your compound? Explain why or why not. If an off-target, for what indication might it be used? Is this worth pursuing? Why or why not?

As a sanity measure along the way, you can always double-check your predictions against the SEA web tool, at http://sea.bkslab.org/search, which will make similar (but not identical) target predictions for each drug you provide. Simply input the drug SMILES from the cancer_compounds.csv file and the drug name or ID, followed by a space.


### Script 1: "Predict" notebook

`Predict_Script_Fill_Jupy-Env-STUDENTS.ipynb`

This notebook takes in a file containing compounds (SMILES), along with two reference files containing data on molecules and targets from ChEMBL. It loads the data, converts the SMILES into in-memory representations of molecules using RDKIT, calculates chemical fingerprints from them, and trains a machine-learning method called a Naïve Bayesian Classifier to predict the drug targets of each compound.

http://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes

Some parts of the script are incomplete, and these are marked with question marks (?). It is your job to fill them in.

### Script 2: "Compare" notebook

`Compare_Script_Fill_Jupy-Env-STUDENTS.ipynb`

This notebook is used to explore why a prediction from the first script was made. It takes a file of drugs along with a target ID (e.g., “CHEMBL...”), and the two ChEMBL reference files as mentioned before. It uses RDKit to calculate the molecular similarity of all the ligands for the target you specified as compared to the drugs you gave it, and shows the most similar ligands.

http://www.rdkit.org/docs/GettingStartedInPython.html

Do these ligands share common patterns, functional groups, “warheads”, etc with your compound? Which ones?

### Data
`cancer_compounds.sample.csv`
- This file can be opened in Excel, or a simple text editor, and contains the SMILES and names or IDs of various cancer-related compounds.
- **It demonstrates the file format for to be used for the query drugs as input to the "Predict" notebook.**

`candidate_compounds.sample.csv`
- This file can be opened in Excel, or a simple text editor, and likewise contains SMILES and IDs of several cancer compounds from the first data file. 
- **It demonstrates the file format for to be used for the query drugs as input to the "Compare" notebook.**

`chembl_21_binding_molecules.csv.gz`
- This file contains: Chembl_ID, SMILE, Fingerprint
- **The code requires this file to be gzipped, but you can explore this file by unzipping into a new file: `gunzip -c chembl_21_binding_molecules.csv.gz > chembl_21_binding_molecules.csv`**

`chembl_21_binding_targets.csv.gz`
- This file contains: Target ID, UniProt Name, Molecule IDs, Description
--**The code requires this file to be gzipped, but you can explore this file by unzipping into a new file: `gunzip -c chembl_21_binding_targets.csv.gz > chembl_21_binding_targets.csv`**

### Setting up our Working Environment
Let's create a directory for us to work from. This directory is where we will store all the files we plan to use.

First clone this repository on your local computer:
    
    cd ~/Desktop/
    git clone https://github.com/wconnell/PSPG-CDD.git

### Install Miniconda and Additional Packages
If you do not have Conda installed, install Miniconda from here: https://docs.conda.io/en/latest/miniconda.html

Once Miniconda has been installed, close your terminal window, and reopen another one. Check to see conda was installed correctly. Type the following command to see the list of packages that were installed.

    conda list

### Create and Activate a new Conda Environment
Now that we have the infrastructure in place, we need to create a new conda environment, and install the additional packages, such as rdkit and jupyter, we will need to generate our predictions.

Create a new environment using the following code:

    cd PSPG-CDD/
    conda env create -f environment.yml
    
Activate the environment and confirm:

    conda activate cdd_workshop
    conda env list

Make conda environment avaialable in jupyter kernel:

    ipython kernel install --user --name=ccd_workshop

### Start a Jupyter Notebook Session
To test if everything is working, let's open up a jupyter lab session. We'll import the modules we need to run our scripts correctly.

    jupyter lab

This should bring up a jupyter lab session that is being hosted from your local machine. Open the scripts provided and in the first cell try importing the modules we'll need to ensure all our packages are installed correctly.
