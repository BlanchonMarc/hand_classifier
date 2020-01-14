import argparse
import os
import cv2
import numpy
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input folder")
ap.add_argument("-o", "--output", required=True,
                help="path to output folder")
args = vars(ap.parse_args())

folder_names = ['image_00', 'image_01']

path, dirs, files = next(os.walk(os.path.join(args['input'], folder_names[0])))

path_out = args['output']

with open(path_out, 'w') as f:
    for item in files:
        f.write("%s\n" % item)
