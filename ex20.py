import tensorflow as tf

model = tf.keras.Sequential()
dense1 = tf.keras.layers.Dense(units=2, input_shape=(2,), activation='sigmoid')
dense2 = tf.keras.layers.Dense(units=1, activation='sigmoid')

model.add(dense1)
model.add(dense2)
model.compile(loss='MSE', optimizer=tf.keras.optimizers.SGD(learning_rate=0.5))

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]

model.fit(X, y, batch_size=1, epochs=5_000)