import numpy as np
from sklearn.linear_model import perceptron
from sklearn.neural_network import MLPClassifier
import tensorflow as tf
from tensorflow import keras
import tensorflow as tf
from
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

from sklearn import datasets
X, y = datasets.load_iris(return_X_y=True)

iris = load_iris ()

X_train_full, X_test, y_train_full, y_test = \
    train_test_split(iris.data, iris.target, test_size=0.33, random_state=42)

X_train, X_valid, y_train, y_valid = \
    train_test_split(X_train_full, y_train_full, test_size=0.33, random_state= 42)


history = model.fit(X_train, y_train, epochs=30,
                    validation_data=(X_valid, y_valid))