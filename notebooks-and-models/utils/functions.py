import h5py
import numpy as np


def load_dataset():
    # h5 files contain multidimensional arrays, to load them to python use h5py.File
    train_dataset = h5py.File('data/train_catvnoncat.h5', "r")
    test_dataset = h5py.File('data/test_catvnoncat.h5', "r")

    train_set_x = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_set_x = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y = np.array(test_dataset["test_set_y"][:]) # your test set labels

    train_set_x_flat = train_set_x.reshape((train_set_x.shape[0], -1))
    test_set_x_flat = test_set_x.reshape((test_set_x.shape[0], -1))

    return train_set_x, train_set_x_flat, train_set_y, test_set_x, test_set_x_flat, test_set_y

