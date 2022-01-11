from flask import Flask, request, render_template
from app_helper_model import *
from werkzeug.utils import secure_filename
import os
import logging
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import logging
from PIL import Image
import pytest


# Test picture
#Wie bekommt man ein test Bild hier hinein

test_picture_aeroplane={
        # Bild von einem Flugzeug von tests\pictures
    }
def test_get_predictions():
    response=get_predictions(test_picture_aeroplane)
    assert response.resultCategory == "Aeroplane"

test_picture_truck={
        # Bild von einem Flugzeug von tests\pictures
    }
def test_get_predictions():
    response=get_predictions(test_picture_truck)
    assert response.resultCategory == "truck"


