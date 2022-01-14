from app_helper_model import *
import pytest


@pytest.mark.parametrize(
    "input_image_path, expected_output_result_category, error",
    [
        ("./tests/pictures/plane.jpeg", "Aeroplane", None),
        ("./tests/pictures/frog.jpeg", "Frog", None),
        ("./tests/pictures/horse.jpeg", "Horse", None),
        ("notexistingfile.exe", "No Catetegory - Uploaded file is not an image!", None),
    ],
)
def test_get_predictions(
    input_image_path: str, expected_output_result_category: str, error: str
) -> None:
    """The function is automatically testing a predefined set of images with the predicted result category."""
    assert expected_output_result_category == get_predictions(input_image_path)
