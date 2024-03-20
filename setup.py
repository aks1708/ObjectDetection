from setuptools import setup

with open('requirements.txt') as req:
    requirements = req.readlines()

setup(
   name='Object-Detection',
   version='1.0',
   python_requires='>=3.11',
   packages=['source'],
   install_requires=requirements,
   author='Anuj Singhal',
   description='Object Detection using ObjectNet3D Dataset')