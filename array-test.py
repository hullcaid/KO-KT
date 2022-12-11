import numpy as np

X = np.array( [1,2,3,4,5,6,7,8,9,10] )
print('X: '+str(X))
ids = np.arange(0,X.shape[0])

print('Ids: ' + str(ids))

np.random.shuffle(ids)

print('Shuffled Ids: ' + str(ids))

x_test = X[ids[0:5]]
x_single = X[ids[5:]]
x_double = X[ids[5::]]
print(x_single)
print(x_double)