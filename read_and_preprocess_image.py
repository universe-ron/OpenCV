import cv2
from typing import Tuple


def read_and_preprocess_image(
    image_path: str, kernel_size: Tuple[int, int] = (5, 5)
) -> Tuple:
    """
    Read an image file, convert it to grayscale, and apply Gaussian Blur to reduce noise.

    :param image_path: str, path to the input image file
    :param kernel_size: Tuple[int, int], kernel size for Gaussian Blur, default is (5, 5)
    :return: Tuple containing the original image and preprocessed grayscale image
    """
    # Read the image file
    image = cv2.imread(image_path)
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian Blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, kernel_size, 0)
    return image, blurred_image
