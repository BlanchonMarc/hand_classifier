import argparse
import os
import cv2
import numpy as np
import shutil

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True,
                help="path to input folder")
args = vars(ap.parse_args())

folder_names = ['image_00', 'image_01', 'image_rebutal']

rebutal = os.path.join(args['input'], folder_names[2])
if not os.path.exists(rebutal):
    os.makedirs(rebutal)

rebutal00 = os.path.join(rebutal, folder_names[0])
if not os.path.exists(rebutal00):
    os.makedirs(rebutal00)

rebutal01 = os.path.join(rebutal, folder_names[1])
if not os.path.exists(rebutal01):
    os.makedirs(rebutal01)


path, dirs, files = next(os.walk(os.path.join(args['input'], folder_names[0])))
file_count = len(files)
# print(int(files[0].split('.')[0]))
#filesort = [int(x.split('.')[0]) for x in files]


# start = min(filesort)
start = 6813

end = 7517 + 1

for i in range(start, end):
    print(i)
    p_l = os.path.join(args['input'], folder_names[0],
                       f'{str(i).zfill(6)}.png')
    p_r = os.path.join(args['input'], folder_names[1],
                       f'{str(i).zfill(6)}.png')
    im_l = cv2.imread(p_l, cv2.IMREAD_UNCHANGED)
    im_r = cv2.imread(p_r, cv2.IMREAD_UNCHANGED)

    try:
        dim = (im_l.shape[1], im_l.shape[0])
        im_r = cv2.resize(im_r, dim, interpolation=cv2.INTER_AREA)

        col = np.vstack([im_l, im_r])
        cv2.namedWindow('test', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('test', im_l.shape[0] * 2, im_l.shape[1])
        cv2.imshow('test', col)
        key = cv2.waitKey(0)

        if key == 27:
            print(f'Moving {p_l} to rebutal')
            shutil.move(p_im, os.path.join(
                rebutal00, f'{str(i).zfill(6)}.png'))
            print(f'Moving {p_r} to rebutal')
            shutil.move(p_r, os.path.join(rebutal01, f'{str(i).zfill(6)}.png'))

    except:
        print('Corrupted Image')
        print(f'Moving {p_l} to rebutal')
        shutil.move(p_l, os.path.join(rebutal00, f'{str(i).zfill(6)}.png'))
        print(f'Moving {p_r} to rebutal')
        shutil.move(p_r, os.path.join(rebutal01, f'{str(i).zfill(6)}.png'))
    finally:
        cv2.destroyAllWindows()
