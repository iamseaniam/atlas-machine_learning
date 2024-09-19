#!/bin/usr/env python3
from sklearn.preprocessing import StandardScaler


X = [[0, 15],
     [1, -10]]
# scale data according to computed scaling values
test1 = StandardScaler().fit(X).transform(X)

print(test1)