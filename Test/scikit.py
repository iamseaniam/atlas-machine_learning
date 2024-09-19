#!/usr/bin/env python3
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import StandardScaler

# Fitting and predicting: estimator basics
clf = RandomForestClassifier(random_state=0)
X = [[ 1,  2,  3],  # 3 samples, 3 features
     [11, 12, 13],
     [100, 200, 300]]
y = [0, 1, 2] # classes of each sample
test1 = clf.fit(X, y)

test2 = clf.predict(X) # predict classes of the training data
test3 = clf.predict([[4, 5, 6], [14, 15, 16], [1, 2, 3], [121, 132, 155]]) # predict classes of new data

print(test1)
print(test2)
print(test3)


# Transformers and pre-processors
Z = [[0, 15],
     [1, -10]]
# scale data according to computed scaling values
test4 = StandardScaler().fit(Z).transform(Z)

print(test4)