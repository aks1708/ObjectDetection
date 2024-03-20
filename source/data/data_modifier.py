from pymatreader import read_mat
import os
from source.utils.utils import get_class_index, coordinate_normalizer
import shutil

def create_image_split_directory(split):
    """
    Creating the data image split directory from the original dataset 
    parameters: split (str) The split name ('train', 'train_val', 'val', 'test') 
    return: None
    """
    with open('../data/raw/Image_sets/{}.txt'.format(split)) as split_read:
        split_file = split_read.readlines()

    try:
        os.mkdir('../data/processed/images/{}'.format(split))
    except OSError:
        print(OSError)

    for image in split_file:
        shutil.copy('../data/raw/Images/{}.JPEG'.format(image.strip('\n')), '../data/processed/images/{}'.format(split))


def create_label_file(filename, split):
    """
    Create the labels .txt file for the image to use YOLO
    parameters: 
    - filename (str) The name of the image file
    - split (str): The split to create label.txt for 
    returns: None
    """
    
    #Read the image's annotation file
    annotation = read_mat('../data/raw/Annotations/{}.mat'.format(filename.split('.')[0]))

    #Fetching the class labels and bounding box coordinates
    label = annotation['record']['objects']['class']
    coords = annotation['record']['objects']['bbox']

    classes = [label] if not isinstance(label, list) else label
    bbox_coords = [coords] if not isinstance(label, list) else coords

    #Fetching the image height and width
    width = annotation['record']['size']['width']
    height = annotation['record']['size']['height']

    #Creating a label txt file for the image
    with open('../data/processed/labels/{}/{}.txt'.format(split, filename.split('.')[0]), 'w+') as label_file:
        for classname, box_coord in zip(classes, bbox_coords):
            line = "{} {} {} {} {}".format(get_class_index(classname), *coordinate_normalizer(box_coord, width, height))
            label_file.write(line + '\n')

def create_label_directory(split):
    """
    Function creates the label directory for a split containing the labels.txt for each image. This is 
    necessary for using the YOLO model.
    :param split: The split to create the labels directory for 
    Returns nothing
    """

    os.mkdir('../data/processed/labels/{}'.format(split))

    for filename in os.listdir('../data/processed/images/{}'.format(split)):
        create_label_file(filename, split)