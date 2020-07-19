# PYTHON script

'''

this is a demo for checking differnet methods for list and array averaging ...

'''


import os
import numpy as np


a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = np.array([[20, 30, 40], [100, 200, 300], [1000, 2000, 3000], [4000, 5000, 6000]])

b = np.array([10, 11, 12])
print("b shape = ", b.shape)
print("b type = ", type(b))

new_b = np.array([b])
print(new_b.shape)
print("new b type = ", type(new_b))
'''
c = np.array([[4, 5, 6]])
newer_b = np.append(new_b, c, axis = 0)
print(newer_b.shape)
'''
d = np.empty([1, 3])

new_d = np.append(d, new_b, axis = 0)
print(new_d)
'''
new_a = np.append(a, b, axis = 0)
print("new_a = ", new_a)
print(new_a.shape[0])

mean_a = np.mean(a, axis=0)
print("mean = ", mean_a)

new_a_deleted = np.delete(new_a, 0, axis = 0)
print("new_a_deleted = ", new_a_deleted)

sum_rows = np.sum(a, axis = 0)
avg = (np.sum(a, axis = 0)/3)

print(avg)
print("          ")
print(sum_rows)
print("           ")
'''

print("            ")
