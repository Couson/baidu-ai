import os
import numpy as np


def unpickle(file):
    '''
    take in python pickled input file and return dictionary
    '''
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict



def load_training_helper(dir_path, file_name):
    train_data = []
    train_labels = []
    for i in range(1, 6):
        train_dict = unpickle(os.path.join(dir_path, '{0}_{1}'.format(file_name, i)))
        if i == 1:
            train_data = train_dict[b'data']
        else:
            train_data = np.vstack((train_data, train_dict[b'data']))

        train_labels += train_dict[b'labels']

    train_data = np.rollaxis(train_data.reshape(train_data.shape[0], 3, 32, 32), 1, 4)
    train_labels = np.array(train_labels)
    return train_data, train_labels

def load_testing_helper(dir_path, file_name):
    train_data = []
    train_labels = []
    for i in range(1, 6):
        train_dict = unpickle(os.path.join(dir_path, 'test_batch'))
        if i == 1:
            train_data = train_dict[b'data']
        else:
            train_data = np.vstack((train_data, train_dict[b'data']))

        train_labels += train_dict[b'labels']

    train_data = np.rollaxis(train_data.reshape(train_data.shape[0], 3, 32, 32), 1, 4)
    train_labels = np.array(train_labels)
    return train_data, train_labels
    
def load_data(data_dir, return_label_name = False):
    
    train_data, train_labels = load_training_helper(data_dir, 'data_batch')
    
    test_data, test_labels = load_testing_helper(data_dir, 'test_batch')
    if return_label_name:
        meta_data_dict = unpickle(data_dir + "/batches.meta")
        label_names = meta_data_dict[b'label_names']
        return train_data, train_labels, test_data, test_labels, return_label_name
    else:
        return train_data, train_labels, test_data, test_labels

