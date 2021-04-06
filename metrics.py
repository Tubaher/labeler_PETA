import argparse
import os
import shutil
import time
import sys
import numpy as np
import logging
import torch
import pandas as pd




# Level of warnings
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.NOTSET) 

def make_metrics(path_annotations):
    """
    input: path_annotations -> Path of annotations file
    output: pytorch tensor of attribute occurrences
    """

    #Open File
    try:
        df_annotations = pd.read_csv(path_annotations,sep=" ", head = None)
    except:
        logging.critical('Cannot read the file: {}'.format(path_annotations)) 
        return 
    

    logging.info('Data Frame loaded: {}'.format(df_annotations)) 
    num_attributes = len(df_annotations.columns)
    resume = df_annotations.iloc[:,1:num_attributes - 1].sum()
    number_of_samples = df_annotations['name'].count()

    list_weights = resume.tolist()
    print(list_weights)
    logging.info('List of Weights: {}'.format(list_weights)) 
    
    tensor_weights = torch.Tensor(list_weights).cuda()

    return tensor_weights


annotations = make_metrics('/home/ricardo/Documents/TRabajo/Labeler/annotations_test.txt')
print(annotations)