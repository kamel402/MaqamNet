import sys
import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score 

# Evaluation functions 

def tagwise_aroc_ap(tags_true_binary, tags_predicted):
    ''' Retrieval : tag-wise (col wise) calculation  '''
    n_tags = tags_true_binary.shape[1]
    auc = []
    aprec = []

    for i in range(n_tags):
        if np.sum(tags_true_binary[:, i]) != 0:
            auc.append(roc_auc_score(tags_true_binary[:, i], tags_predicted[:, i]))
            aprec.append(average_precision_score(tags_true_binary[:, i], tags_predicted[:, i]))


    return auc, aprec

def itemwise_aroc_ap(tags_true_binary, tags_predicted):
    ''' Annotation : item-wise(row wise) calculation '''
    n_songs = tags_true_binary.shape[0]
    auc = []
    aprec = []

    for i in range(n_songs):
        if np.sum(tags_true_binary[i]) != 0:
            auc.append(roc_auc_score(tags_true_binary[i], tags_predicted[i]))
            aprec.append(average_precision_score(tags_true_binary[i], tags_predicted[i]))


    return auc, aprec


# CUDA multigpu functions 

def handle_multigpu(multigpu, user_gpu_list, available_gpus):
    ''' Check if multigpu is going to be used correctly 
    Args :
        multigpu : user preference on whether to use mult gpu or not (bool)
        user_gpu_list : list of user assigned GPUs
        available_gpus : number of gpus available on the system
    '''

    note = '[GPU AVAILABLILITY]'

    if multigpu and available_gpus <= 1:
        print (note, "You don't have enough GPUs. Do not set any argument for --gpus")
        sys.exit()

    elif not multigpu and available_gpus > 1:
        print (note, "You have %d GPUs but only assigned 1. You can assign list of gpus with --gpus option to utilize multigpu functions"%available_gpus)

    elif len(user_gpu_list) > available_gpus:
        print (note, "You don't have enough GPUs. Check you system and reassign.")
        sys.exit()

    elif multigpu and available_gpus > 1 :
        print (note, "You assigned %d/%d available GPUs"%(len(user_gpu_list), available_gpus))





