import tensorflow as tf
import matplotlib.pyplot as plt

(train_images, train_labels),(test_images, test_labels) = tf.keras.datasets.mnist.load_data()

print(train_images.shape)
print(test_images.shape)

# plt.imshow(train_images[0], cmap="Greys")

model = tf.keras.models.Sequential()

dense1 = tf.keras.layers.Dense(512, activation='relu', input_shape=(784,))
dense2 = tf.keras.layers.Dense(10, activation='sigmoid')
model.add(dense1)
model.add(dense2)

model.compile(optimizer='rmsprop',loss='mse',metrics=['accuracy'])

train_images = train_images.reshape((60000, 784))
train_images = train_images.astype('float32') / 255.0
test_images = test_images.reshape((10000, 784))
test_images = test_images.astype('float32') / 255.0