import urllib
from urllib import request
import numpy as np

X = np.array([[1, 1, 0.3],
              [1, 0.4, 0.5],
              [1, 0.7, 0.8]])

Y = np.array([1, 1, 0])

W = np.array([0, 0, 0,])

def predict(X, W):
    if np.dot(X, W) > 0:
        return 1
    return 0

perfect = False
while not perfect:
    perfect = True
    for e in range(len(X)):
        print(f'Веса: {W}, предсказание: {predict(X[e], W)}, ожидание: {Y[e]}')
        if predict(X[e], W) != Y[e]:
            perfect = False
            if predict(X[e], W) == 0:
                W = W + X[e]
            else:
                W = W - X[e]
    print('Повторяем цикл:') if perfect == False else print('Полученные веса:')

print(W)