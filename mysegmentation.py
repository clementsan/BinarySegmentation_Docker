import numpy as np
import nibabel
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--input', required=True, help='input')
parser.add_argument('--output', required=True, help='output')

args = parser.parse_args()

MyInput = args.input
MyOutput = args.output

nib_img = nibabel.load(MyInput)
img = nib_img.get_data()
#print (img.shape, img.dtype)

binary_img = img > 250

from skimage import morphology
closed_img = morphology.binary_closing(binary_img, selem=morphology.ball(radius=2))

out_img = nibabel.Nifti1Image(closed_img.astype(np.uint8), nib_img.affine)
out_img.to_filename(MyOutput)
