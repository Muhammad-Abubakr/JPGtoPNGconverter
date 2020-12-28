import sys
import os, os.path
from PIL import Image

# grab first and second aguement
sys.argv[1]
sys.argv[2]

# check if new exists if now create one
if os.path.exists(f'{sys.argv[1]}/new'):
	pass
else:
	os.makedirs(f'{sys.argv[1]}/new')

# loop through pokedex
# convert JPG to PNG
# save to the new folder
for image in os.listdir(sys.argv[1]):
	if image.endswith('.jpg'):
		clean_name = os.path.splitext(image)[0] ## cleans the filename by removing previous extension
		print(clean_name)
		img = Image.open(f'{sys.argv[1]}/{image}') ## access the file for usage and processing.
		## img.save(f'{sys.argv[1]}/new/mod_img.png','png')
		## instead of giving file a new name use the previous one.
		## by calling the variable that stores file with its name.
		img.save(f'{sys.argv[1]}/new/{clean_name}.png','png')
		print('Conversion Complete!')
	else:
		continue


