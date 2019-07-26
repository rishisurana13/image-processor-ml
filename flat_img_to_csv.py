import numpy as np
import cv2 
import os as os
import csv
from pathlib import Path

img_width_parsed = input('Enter image pixel width (<500): ')
img_height_parsed = input('Enter image pixel height (<500): ')
img_width = int(img_width_parsed)
img_height = int(img_height_parsed)


path_to_directory = input('enter absolute path for directory to be processed: ')
filename_parsed = input('enter csv file output name: ')

filename = filename_parsed + '.csv'
print ('creating file',filename, '.....')


output_csv_file = Path(filename).touch()
print ('created file',filename)

sub_directory = []

for subdir_item in os.listdir(path_to_directory): # add all subdirectory items to a list for iteration purposes
	sub_directory.append(subdir_item)


def flatten_image(img_pixel_array):
	flat_img_array = np.ndarray.flatten(img_pixel_array)
	return flat_img_array


def resize_and_flatten_img (image, sub_dir):
	img = cv2.imread(path_to_directory + sub_dir + '/' + image, 0)
	img_resized = cv2.resize(img, (img_width,img_height))
	flat_img = flatten_image(img_resized)
	return flat_img

def post_to_csv(img):
	with open(filename, 'a', newline='') as csvfile:
   		writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
   		writer.writerow(img)


def image_final_output(sub_dir):
	for image in os.listdir(path_to_directory + sub_dir):
			flat_image = resize_and_flatten_img(image, sub_dir)
			post_to_csv(flat_image)
	

total_files = 0
for dir_index in os.listdir(path_to_directory): # iterate over every individual directory item 
	if dir_index == '.DS_Store':
		continue 

	num_files = len(os.listdir(path_to_directory + dir_index))
	print('processed', num_files, ' images for ', dir_index)
	total_files += num_files
	image_final_output(dir_index)


print ('processed ', total_files, ' pictures in total')

