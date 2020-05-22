# PYTHON script
'''

normalizing pixel values from (0,255) to (0,1)
normalizing pixel values from (0,255) to (-1,1)

Black and white images are single matrix of pixels whereas color images have a separate array of pixel values for each color channel, such as red, green, and blue.

Pixel values are often unsigned integers in the range between 0 and 255. Although these pixel values can be presented directly to neural network models in their raw format, this can result in challenges during modeling, such as in the slower than expected training of the model.

Instead, there can be great benefit in preparing the image pixel values prior to modeling, such as simply scaling pixel values to the range 0-1 to centering and even standardizing the values.

https://machinelearningmastery.com/how-to-manually-scale-image-pixel-data-for-deep-learning/


'''

import csv
import pprint as pp

signs_dict = {}
dict_list = []

i = 0
with open('signnames.csv', newline='') as csvfile:
    row_reader = csv.reader(csvfile, delimiter=',')
    for row in row_reader:
        dict_list.append(row)
        if (i != 0):
            signs_dict[i-1] = dict_list[i][1]
        i = i + 1
        
pp.pprint(signs_dict)

