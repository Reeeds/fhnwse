from keras.models import load_model
from keras.preprocessing import image
import numpy as np


def get_predictions(file_path):
    model = load_model("./model/model2.h5")
    print(model.summary())
    test_image = image.load_img(file_path, target_size=(32, 32))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = model.predict(test_image)

    print(result)
    if result[0][0] == 1:
        print("Aeroplane")
        resultCategory = "Aeroplane"
    elif result[0][1] == 1:
        print("Automobile")
        resultCategory = "Automobile"
    elif result[0][2] == 1:
        print("Bird")
        resultCategory = "Bird"
    elif result[0][3] == 1:
        print("Cat")
        resultCategory = "Cat"
    elif result[0][4] == 1:
        print("Deer")
        resultCategory = "Deer"
    elif result[0][5] == 1:
        print("Dog")
        resultCategory = "Dog"
    elif result[0][6] == 1:
        print("Frog")
        resultCategory = "Frog"
    elif result[0][7] == 1:
        print("Horse")
        resultCategory = "Horse"
    elif result[0][8] == 1:
        print("Ship")
        resultCategory = "Ship"
    elif result[0][9] == 1:
        print("Truck")
        resultCategory = "Truck"
    else:
        print("Error")
        resultCategory = "Error"

    return resultCategory
