import h5py
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_dataset():
    train_dataset = h5py.File('data/train_catvnoncat.h5', "r")
    test_dataset = h5py.File('data/test_catvnoncat.h5', "r")

    train_set_x = np.array(train_dataset["train_set_x"][:])
    train_set_y = np.array(train_dataset["train_set_y"][:])

    test_set_x = np.array(test_dataset["test_set_x"][:])
    test_set_y = np.array(test_dataset["test_set_y"][:])

    # Perform data augmentation on the training set
    datagen = ImageDataGenerator(
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True
    )
    datagen.fit(train_set_x)  # Compute statistics for data augmentation

    # Apply data augmentation transformations to training set and labels
    augmented_images = datagen.flow(train_set_x, batch_size=len(train_set_x), shuffle=False).next()

    # Concatenate augmented images and original images
    train_set_x_augmented = np.concatenate((train_set_x, augmented_images))
    train_set_y_augmented = np.concatenate((train_set_y, train_set_y))

    # Flatten the images
    train_set_x_flat = train_set_x.reshape((train_set_x.shape[0], -1))
    test_set_x_flat = test_set_x.reshape((test_set_x.shape[0], -1))

    return train_set_x_augmented, train_set_x_flat, train_set_y_augmented, test_set_x, test_set_x_flat, test_set_y