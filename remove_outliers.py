import numpy as np

a = np.array([2.1, 2.4, 3.3, 3.1, 1.9, 11])

# function to remove outliers from an array
def rmv_outliers(original_array, no_of_std_deviations):

    # calculate average of all elements
    mean = np.mean(original_array)

    # get the standard deviation
    std_deviation = np.std(original_array)

    # calculate standard deviation of all elements
    distance_from_mean = abs(original_array - mean)

    # no of standard deviations allowed
    no_of_std_deviations = 2

    # not outliers
    not_outlier = distance_from_mean < no_of_std_deviations * std_deviation

    # new array without the outliers
    new_array = original_array[not_outlier]

    return new_array



# function call with no of standard deviations = 2
a_wo_outliers = rmv_outliers(a, 2)

print(a_wo_outliers)

