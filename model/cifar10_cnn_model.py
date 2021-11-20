import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

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
model = keras.Sequential(
    [
        keras.layers.Flatten(input_shape=(32, 32, 3)),
        keras.layers.Dense(3000, activation="relu"),
        keras.layers.Dense(1000, activation="relu"),
        keras.layers.Dense(10, activation="sigmoid"),
    ]
)
# Compile model
print("******************")
print("hoi")
model.compile(
    optimizer="SGD",
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)
# plot diagnostic learning curves


def summarize_diagnostics(history: object):
    # plot loss
    plt.title("Cross Entropy Loss")
    plt.plot(history.history["loss"], color="blue", label="train")
    plt.plot(history.history["val_loss"], color="orange", label="test")
    plt.show()
    # plot accuracy
    plt.title("Classification Accuracy")
    plt.plot(history.history["accuracy"], color="blue", label="train")
    plt.plot(history.history["val_accuracy"], color="orange", label="test")
    plt.show()


# Run model


# save model
model.fit(
    X_train_scaled,
    y_train_categorial,
    validation_data=(
        X_test_scaled,
        y_test_categorial,
    ),
    epochs=1,
)
model.save("model/saved_model")
# learning curves
# summarize_diagnostics(history)
