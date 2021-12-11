import tensorflow as tf
from tensorflow import keras

# Info GPU
gpu = len(tf.config.list_physical_devices("GPU")) > 0
print("GPU is", "available" if gpu else "NOT AVAILABLE")

# Load Datenset CIFAR10
# Load into data set and test set
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()
# Preprocessing
# Classify the images
classes = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]
# Scaling of the images
X_train_scaled = X_train / 255
X_test_scaled = X_test / 255
# One Hot Encoding in 10 categorial features
y_train_categorial = keras.utils.to_categorical(
    y_train,
    num_classes=10,
    dtype="float32",
)
y_test_categorial = keras.utils.to_categorical(
    y_test,
    num_classes=10,
    dtype="float32",
)
# Creating a test model
# Define cnn model
# model = keras.Sequential(
#     [
#         keras.layers.Flatten(input_shape=(32, 32, 3)),
#         keras.layers.Dense(3000, activation="relu"),
#         keras.layers.Dense(1000, activation="relu"),
#         keras.layers.Dense(10, activation="sigmoid"),
#     ]
# )


model = tf.keras.models.Sequential()
model.add(
    tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=3,
        padding="same",
        activation="relu",
        input_shape=[32, 32, 3],
    )
)
model.add(
    tf.keras.layers.Conv2D(filters=32, kernel_size=3, padding="same", activation="relu")
)
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding="valid"))
model.add(
    tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding="same", activation="relu")
)
model.add(
    tf.keras.layers.Conv2D(filters=64, kernel_size=3, padding="same", activation="relu")
)
model.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2, padding="valid"))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.5, noise_shape=None, seed=None))
model.add(tf.keras.layers.Dense(units=128, activation="relu"))
model.add(tf.keras.layers.Dense(units=10, activation="softmax"))


# Compile model
model.compile(
    optimizer="Adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)


# test_loss, test_accuracy = model.evaluate(X_test, y_test)
# print("Test accuracy: {}".format(test_accuracy))

model.fit(
    X_train_scaled,
    y_train_categorial,
    validation_data=(
        X_test_scaled,
        y_test_categorial,
    ),
    epochs=15,
)

test_loss, test_accuracy = model.evaluate(X_test, y_test)
print("Test accuracy: {}".format(test_accuracy))


model.save("model/model.h5")
