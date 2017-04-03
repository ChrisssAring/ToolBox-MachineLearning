"""Explore learning curves for classification of handwritten digits"""

import matplotlib.pyplot as plt
import numpy
import math
from sklearn.datasets import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def display_digits():
    """Read in the 8x8 pictures of numbers and display 10 of them"""
    digits = load_digits()
    print(digits.DESCR)
    fig = plt.figure()
    for i in range(10):
        subplot = fig.add_subplot(5, 2, i+1)
        subplot.matshow(numpy.reshape(digits.data[i], (8, 8)), cmap='gray')

    plt.show()


def train_model():
    """Train a model on pictures of digits.

    Read in 8x8 pictures of numbers and evaluate the accuracy of the model
    when different percentages of the data are used as training data. This function
    plots the average accuracy of the model as a function of the percent of data
    used to train it.
    """
    data = load_digits()
    num_trials = 10
    train_percentages = range(5, 95, 5)
    test_accuracies = numpy.zeros(len(train_percentages))
    model = LogisticRegression(C=10**-10)

    for percentage in range(len(train_percentages)):
        test_avg = []
        for i in range(num_trials):
            X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=train_percentages[percentage]/100)
            model.fit(X_train, y_train)
            test_avg.append(model.score(X_test, y_test))
        test_accuracies[percentage] = numpy.mean(test_avg)

    print("Train accuracy %f" %model.score(X_train, y_train))
    print("Test accuracy %f"%model.score(X_test, y_test))

    fig = plt.figure()
    plt.plot(train_percentages, test_accuracies)
    plt.xlabel('Percentage of Data Used for Training')
    plt.ylabel('Accuracy on Test Set')
    plt.show()


if __name__ == "__main__":
    # Feel free to comment/uncomment as needed
    #display_digits()
    train_model()
