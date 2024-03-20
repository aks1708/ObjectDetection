
# Object Detection using ObjectNet3D dataset

The aim of this project is to use YOLO to detect objects in this dataset. 

To get started with this project, use the setup.py file by running:

```
pip install -e .
```

Inside the ```data/raw directory```, we want the following directories which can be extracted from the ObjectNet3D Dataset download:
 - Annotations
 - Image_sets
 - Images

In order to get the processed dataset, we need to run ```data_preprocessing.ipynb``` in the ```notebooks``` directory.
Run this notebook first before any other one.

We can get a feel for the problem using the ```data_exploration.ipynb``` notebook

```model``` contains the YOLO model and its weights

```source``` is a module that contains helper functions to process the data and create label txt files to use the YOLO model

```reports``` contains graphs depicting results during fine tuning.