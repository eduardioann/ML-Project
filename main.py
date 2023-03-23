from sklearn import neural_network
import numpy as np
import pandas as pd
import csv


def myMLP(x_train, y_train, x_test, y_test, lr, size1, size2 = 0):
    # CREATING AND TESTING MLP

    if (size2 == 0):
        clf = neural_network.MLPClassifier(hidden_layer_sizes = (size1), learning_rate_init = lr)
    else:
        clf = neural_network.MLPClassifier(hidden_layer_sizes = (size1, size2), learning_rate_init = lr)

    clf.fit(x_train, y_train)

    # TESTING MLP
    predictii = clf.predict(x_test)

    # ACCURACY
    k = 0

    for i in range(len(y_test)):
        if (predictii[i] == y_test[i]):
            k += 1

    print(k / len(y_test))


dataset = pd.read_csv("skin.csv")
dataset = np.asarray(dataset)

# UPLOAD DATA
etichete = dataset[:, 3]

# DIVISION INTO TRAIN AND TEST
date_train = dataset[:183792, :]
etichete_train = etichete[:183792]

date_test = dataset[183792:, :]
etichete_test = etichete[183792:]

########

dim_intrare = 3

learning_rate = [0.1, 0.01]


for my_lr in learning_rate:

    for i in range(2):  ## no. of neurons

        for j in range(2):  ## full or half
            nr_neuroni = i + 1

            if nr_neuroni == 1:
                size = dim_intrare // (j + 1)
                myMLP(date_train, etichete_train, date_test, etichete_test, my_lr, size1 = size)

            elif nr_neuroni == 2:
                size1 = dim_intrare // (j + 1)
                size2 = size1 // (j + 1)
                myMLP(date_train, etichete_train, date_test, etichete_test, my_lr, size1 = size1, size2 = size2)
