#!~/virtualEnvs/anaconda3/envs/imageproc35/bin/python
"""
Author: Garrett Gaskins
Date Initialized: 2017-01-24
Last Edited: 2019-02-21
Email: gaskins@keiserlab.org

Summary: Utility functions for running portions of predict.py and compare_to_ligands.py
""" 

###########################################################################################################################################
#        #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       # 
#                                                                IMPORT MODULES                                                            
#    #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       #     
###########################################################################################################################################

# I/O Handling
import os,sys
import csv
import gzip

# Data Handling
import numpy as np
import pandas as pd

# Plotting
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')


###########################################################################################################################################
#        #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       # 
#                                                              PRIMARY FUNCTIONS                                                           
#    #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       #       #     
###########################################################################################################################################


def map_target_identifiers(chembl_targ_f):
    """Function for mapping target names, so that uniprotID or targ_desc are
    used before generic uninterpretable Chembl_ID."""
    chid_to_targName = {}
    print('Mapping target chembl_IDs to human-readable Names...')
    fi = gzip.open(chembl_targ_f, 'rt')
    reader = csv.reader(fi)
    next(reader) # Iterate over file header
    for chid, unid, cpd_assocs, tdesc in reader:
        if unid != '':
            chid_to_targName[chid] = unid
        elif tdesc != '':
            chid_to_targName[chid] = tdesc
        else:
            chid_to_targName[chid] = chid
    print('\tMapped {} chembl_IDs'.format(len(chid_to_targName)))
    print('')
    return chid_to_targName


def flatten_list(l):
    """Util function for flattening list of lists into a single list"""
    flat_list = [item for sublist in l for item in sublist]
    return flat_list


def view_target_dist(preds_f, targ_limit=15, figsize=(30,20)):
    """Create bar chart of top predicted targets."""
    # Setup Figure
    fig = plt.figure(figsize=figsize)
    plt.subplot(111)
    fig.subplots_adjust(bottom=0.2)
    # Generate pandas dataframe of 
    predsDF = pd.read_csv(preds_f, usecols=['Probability_Estimate', 'Targ_Class'])
    targ_counts = predsDF['Targ_Class'].value_counts()
    xvals = targ_counts.index.values[0:targ_limit]
    yvals = targ_counts.values[0:targ_limit]
    sns.barplot(x=xvals[::-1], y=yvals[::-1], palette='GnBu')
    plt.title('Top {} Predicted Targets'.format(targ_limit), fontsize=26)
    plt.xlabel('Target Prediction', fontsize=17)
    plt.ylabel('Frequency of Prediction', fontsize=20)
    plt.xticks(rotation='vertical', fontsize=17)
    plt.yticks(fontsize=20)
    base_dir = os.getcwd()
    base_name = os.path.basename(preds_f).split('.')[0]
    ofn = os.path.join(base_dir, base_name + '.png')
    plt.savefig(ofn)
    plt.show()
    return

# Reads training data from tar.gz files, returns (X, y)
def format_training_data(chembl_mol_f, chembl_targ_f):
    """Returns nDim array of bit-vectorized molecules (x-values) and corresponding nDim array of target classes
    that each bit-vector is assigned to (y-values)."""
    bayes_XY_fields = []
    cpid_to_bitVec = {} # cpid = compound chembl_ID
    
    print('Formatting training data for use with Naive Bayesian Classifier...')
    mol_fi, targ_fi = (gzip.open(chembl_mol_f, 'rt'), gzip.open(chembl_targ_f, 'rt'))
    # Iterate through mol_file, transform smile to bit-vector, map cpid to its corresponding bit-vector
    mol_reader = csv.reader(mol_fi)
    next(mol_reader) # circumvent file header
    print('\tTransforming cpd smiles to bit-vectors from file: {}'.format(os.path.basename(chembl_mol_f)))
    for cpid, smi, fp in mol_reader:
        bitVec = np.frombuffer(fp.encode(), 'i1') - 48 # creates numpy array from string of 0's and 1's
        cpid_to_bitVec[cpid] = bitVec
    print('\t\tGenerated {} compound bit-vectors'.format(len(cpid_to_bitVec)))

    # Iterate through targ_file, get all compounds (bitVector) associated with each target, format for bayes learning.
    targ_reader = csv.reader(targ_fi)
    next(targ_reader)
    print("\tMapping target classes to compound bit-vectors from file: {}".format(os.path.basename(chembl_targ_f)))
    for targID, uniprotID, cpd_assocs, targ_desc in targ_reader:
        for cpid in cpd_assocs.split(':'):
            if cpid in cpid_to_bitVec:
                bitVec = cpid_to_bitVec[cpid]
                bayes_XY_fields.append((bitVec, targID))
    
    # Return xvalues (bit-Vectors for each compound), and yvalues (class label of target each compound is associated with)
    xvals, yvals = zip(*bayes_XY_fields)
    print('\t\tGenerated {} total training examples.'.format(len(xvals)))
    print('')
    return np.array(xvals), np.array(yvals)