import h5py
import numpy as np

def load_dataset() -> tuple:
    """
    Load the dataset from HDF5 files.

    Returns:
        tuple: A tuple containing train and test set data and labels in the following order:
            - train_set_x: Training set features (original shape)
            - train_set_x_flat: Training set features (flattened)
            - train_set_y: Training set labels
            - test_set_x: Test set features (original shape)
            - test_set_x_flat: Test set features (flattened)
            - test_set_y: Test set labels
    """
    # h5 files contain multidimensional arrays, to load them into Python use h5py.File
    train_dataset = h5py.File('data/train_catvnoncat.h5', "r")
    test_dataset = h5py.File('data/test_catvnoncat.h5', "r")

    train_set_x = np.array(train_dataset["train_set_x"][:])  # Your train set features
    train_set_y = np.array(train_dataset["train_set_y"][:])  # Your train set labels

    test_set_x = np.array(test_dataset["test_set_x"][:])     # Your test set features
    test_set_y = np.array(test_dataset["test_set_y"][:])     # Your test set labels

    train_set_x_flat = train_set_x.reshape((train_set_x.shape[0], -1))
    test_set_x_flat = test_set_x.reshape((test_set_x.shape[0], -1))

    return train_set_x, train_set_x_flat, train_set_y, test_set_x, test_set_x_flat, test_set_y
