import numpy as np


a = np.array([[1, 3, 5], [1.1, 3.3, 5.5], [0.9, 3.1, 5.3], [12, 3.05, 15]])

print(a)
print()
a_mean = np.mean(a, axis=0)
print(a_mean)

standard_deviation = np.std(a)

print("Std Dev - ", np.std(a, axis=0))

distance_from_mean = abs(a - a_mean)

max_deviations = 2

not_outlier = distance_from_mean < max_deviations * standard_deviation

no_outliers = a[not_outlier]
print(no_outliers)

