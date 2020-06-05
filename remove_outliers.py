# code to detect outliers in an array based -
# takes array and no of std deviations as input
# and outputs array without outliers and outlier indices for the original array

import numpy as np

a = np.array([2.1, 2.4, 3.3, 3.1, 1.9, 11.0, 2.3, 1.4, 1.5, 1.11, 1.31, 11.5, 1.13, 1.14, 2.2])
print("length = ", len(a))

# function to remove outliers from an array
def rmv_outliers(input_array, no_of_std_deviations):

    # calculate average of all elements
    mean = np.mean(input_array)

    # get the standard deviation
    std_deviation = np.std(input_array)
    print("Std deviation = ", std_deviation)

    # calculate standard deviation of all elements
    # dist_from_mean = abs(input_array - mean)

    outliers = []

    for i in range(len(a)):
        dist_from_mean = abs(a[i]-mean)
        if(dist_from_mean>no_of_std_deviations*std_deviation):
            outliers.append(i)

    new_array = np.delete(a, outliers)

    # not_outlier = dist_from_mean < no_of_std_deviations * std_deviation
    # print(not_outlier)

    # new array without the outliers
    # new_array = input_array[not_outlier]

    # print(outlier_indices)

    return new_array, outliers


# function call with no of standard deviations = 2
a_wo_outliers, outliers = rmv_outliers(a, 2)

print(a_wo_outliers)
print(len(a_wo_outliers))
print("outliers = ", outliers)



# function call with no of standard deviations = 2
a_wo_outliers = rmv_outliers(a, 2)

print(a_wo_outliers)
