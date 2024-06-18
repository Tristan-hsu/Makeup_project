import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from PIL import Image
import os
from tensorflow import keras
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, losses
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Model

images = []
folder = 'C:/Users/User/Makeup_project/'
filename = 'test.jpg'
img_path = os.path.join(folder, filename)
img = Image.open(img_path)
img = img.convert('L')  # Ensure the image is in gray format
img = img.resize((128, 128))  # Resize image to a fixed size
img_array = np.array(img)
x_images = img_array.astype('float32') / 255.0
x_images = x_images.reshape((1, 128, 128))
new_model = keras.models.load_model('saved_model')
encoded_imgs = new_model.encoder(x_images).numpy()
result = new_model.decoder(encoded_imgs).numpy()
result = (result * 255).astype(np.uint8)

# Remove the batch dimension and reshape if necessary
result = result.reshape((128, 128))

# Convert to an image and save
output_image = Image.fromarray(result)
output_image.save("outcome.jpg")