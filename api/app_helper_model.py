from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import logging
from PIL import Image


logger = logging.getLogger(__name__)


def get_predictions(file_path: str) -> str:
    """The function returns the category of the image based on the model trained in Cifar 10.
    trained model.
    Possible output:
    Aeroplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship or Truck.
    """
    try:
        Image.open(file_path)
        model = load_model("./model/model2.h5")
        logger.info("Model summary: %s", model.summary())
        logger.info("Filepath: % s", file_path)
        image_to_predict = image.load_img(file_path, target_size=(32, 32))
        image_to_predict = image.img_to_array(image_to_predict)
        image_to_predict = np.expand_dims(image_to_predict, axis=0)
        result = model.predict(image_to_predict)
        logger.info("Result Vector: % s", result)

        if result[0][0] == 1:
            resultCategory = "Aeroplane"
            logger.info("Aeroplane predicted")
        elif result[0][1] == 1:
            logger.info("Automobile predicted")
            resultCategory = "Automobile"
        elif result[0][2] == 1:
            logger.info("Bird predicted")
            resultCategory = "Bird"
        elif result[0][3] == 1:
            logger.info("Cat predicted")
            resultCategory = "Cat"
        elif result[0][4] == 1:
            logger.info("Deer predicted")
            resultCategory = "Deer"
        elif result[0][5] == 1:
            logger.info("Dog predicted")
            resultCategory = "Dog"
        elif result[0][6] == 1:
            logger.info("Frog predicted")
            resultCategory = "Frog"
        elif result[0][7] == 1:
            logger.info("Horse predicted")
            resultCategory = "Horse"
        elif result[0][8] == 1:
            logger.info("Ship predicted")
            resultCategory = "Ship"
        elif result[0][9] == 1:
            logger.info("Truck predicted")
            resultCategory = "Truck"

        return resultCategory
    except IOError:
        logger.warning("Uploaded file is not an image!")
        return "No Catetegory - Uploaded file is not an image!"
