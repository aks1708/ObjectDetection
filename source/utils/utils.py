from collections import defaultdict
from pymatreader import read_mat
import os
import matplotlib.pyplot as plt

def get_class_distribution(split):
    """
    This function shows a pyplot histogram illustrating top classes in dataset split
    parameters: split (str), the portion of the dataset to view
    return: None
    """
    class_vals = defaultdict(lambda: 0)

    #In this loop we iterate through each filename, get their class
    for filename in os.listdir('../data/processed/images/{}'.format(split)):

        annotation = read_mat('../data/raw/Annotations/{}.mat'.format(filename.split('.')[0]))
        label = annotation['record']['objects']['class']
        classes = [label] if not isinstance(label, list) else label

        for classname in classes:
            class_vals[classname] += 1

    #Sort the dictionary by their values and obtain the top 20 classes
    class_vals_dict = sorted(dict(class_vals).items(), key=lambda x: x[1], reverse=True)
    top_classes = class_vals_dict[:20]

    #Plot a histogram to illustrate these classes
    plt.barh(list(dict(top_classes).keys()), list(dict(top_classes).values()))

    plt.title('Top 20 classes in the {} split'.format(split))
    plt.xlabel('Count')
    plt.ylabel('Category')

    plt.show()


def coordinate_normalizer(coords, img_width, img_height):
    """
    param: coords  (list) This is a list of coordinates for one bounding box
    param img_width: (float) Width of image
    param img_height: (float) Height of image
    return: x_centre, y_centre, width_norm, height_norm. Values are normalized to use YOLO
    """
    width = coords[2] - coords[0] #Width of bounding box
    height = coords[-1] - coords[1] #Height of bounding box
    x_center = coords[0] + (width) / 2
    y_center = coords[1] + (height) / 2

    #Now we normalise these values
    x_norm = x_center / img_width
    y_norm = y_center / img_height
    width_norm = width / img_width
    height_norm = height / img_height

    return x_norm, y_norm, width_norm, height_norm


def get_class_index(class_name):
    """
    For a given object, return its class index needed to use YOLO
    parameters: class_name (str). Name of the class 
    return: The class index of the object (int)
    """
    line_number = 0

    with open('../data/raw/Image_sets/classes.txt', 'r') as file:
        for line in file.readlines():
            line_number += 1
            if class_name in line:
                return line_number - 1
            else:
                continue



