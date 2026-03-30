import matplotlib.pyplot as plt
# example of loading an image with the Keras API
from keras.preprocessing.image import load_img
# load the image
img_path = '/content/sample_data/1_Gammar 2021_1_2021_06_03-13-19-23-856.PNG'
img = load_img(img_path)
# report details about the image
print(type(img))
print(img.format)
print(img.mode)
print(img.size)
# show the image using matplotlib
plt.imshow(img)
plt.axis('off') # Turn off axis labels
plt.show()