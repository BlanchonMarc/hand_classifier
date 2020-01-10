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
if not os.path.exists(path_out):
    os.makedirs(path_out)

path_out00 = os.path.join(path_out, folder_names[0])
if not os.path.exists(path_out00):
    os.makedirs(path_out00)

path_out01 = os.path.join(path_out, folder_names[1])
if not os.path.exists(path_out01):
    os.makedirs(path_out01)

for index, file in enumerate(files):
    p_l = os.path.join(args['input'], folder_names[0], file)
    p_r = os.path.join(args['input'], folder_names[1], file)

    im_l = cv2.imread(p_l, cv2.IMREAD_UNCHANGED)
    im_r = cv2.imread(p_r, cv2.IMREAD_UNCHANGED)

    cv2.imwrite(os.path.join(
        path_out00, f'{str(index).zfill(6)}.png'), im_l, [cv2.IMWRITE_PNG_COMPRESSION, 4])
    cv2.imwrite(os.path.join(
        path_out01, f'{str(index).zfill(6)}.png'), im_r, [cv2.IMWRITE_PNG_COMPRESSION, 4])
