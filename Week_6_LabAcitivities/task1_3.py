import matplotlib.pyplot as plt
import os
# example of saving an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import save_img
from keras.preprocessing.image import img_to_array
# load image as as grayscale
img_path = '/content/sample_data/1_Gammar 2021_1_2021_06_03-13-19-23-856.PNG'
img = load_img(img_path, color_mode='grayscale')
# convert image to a numpy array
img_array = img_to_array(img)
# save the image with a new filename
save_path_dir ='/content/sample_data/'
save_filename = '1_Gammar 2021_1_2021_06_03-13-19-23-856_grayscale.jpg'
full_save_path = os.path.join(save_path_dir, save_filename)
save_img(full_save_path, img_array)
# load the image to confirm it was saved correctly
img = load_img(full_save_path)
print(type(img))
print(img.format)
print(img.mode)
print(img.size)
# show the image using matplotlib
plt.imshow(img)
plt.axis('off') # Turn off axis labels
plt.show()