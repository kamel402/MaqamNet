''' Functions for processing the Maqam annotation by selecting top N tags and dividing the dataset into train/valid/test set '''

import os
import pandas as pd
import numpy as np
import config 
np.random.seed(0)



def split_data(filename, base_dir, ratio=0.2):
    ''' Split into train/val/test and saves each set to a new file  
    Args: 
        filename : path to the Maqam annotation csv file 
        base_dir : path to the general project directory 
    Return : 
        None
    '''

    df = pd.read_csv(filename, delimiter='\t')
    data_len = df.shape[0]
    print ("Data shape {}".format(df.shape))
    
    test_len = int (data_len * ratio)
    train_valid_len = data_len - test_len
    valid_len = int(train_valid_len * ratio)
    train_len = train_valid_len - valid_len
    print ("Train %d, valid %d, test %d"%(train_len, valid_len, test_len))
    
    # add headers to all files
    test_df = df.iloc[train_valid_len:]
    valid_df = df.iloc[train_len : train_valid_len]
    train_df = df.iloc[:train_len]
    
    # save each test, valid, train files
    f = filename.split('/')[-1]
    test_df.to_csv(base_dir + 'test_' + f, sep='\t',index=False)
    valid_df.to_csv(base_dir + 'valid_' + f, sep='\t',index=False)
    train_df.to_csv(base_dir + 'train_' + f, sep='\t', index=False)


if __name__ == "__main__":
    new_csvfile = './data/MaqamNet/4_tags_annotations_final.csv'
    split_data(new_csvfile, config.BASE_DIR)

