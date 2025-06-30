import cv2
import numpy as np
from typing import Tuple


def apply_edge_detection(blurred_image: "np.ndarray") -> Tuple:
    """
    Apply Canny and Laplacian of Gaussian (LoG) edge detection algorithms to the preprocessed image.

    :param blurred_image: numpy.ndarray, preprocessed grayscale image
    :return: Tuple containing the results of the Canny and LoG edge detection algorithms
    """
    # Apply Canny edge detection
    canny_edges = cv2.Canny(blurred_image, 20, 120)
    # Apply Laplacian of Gaussian (LoG) edge detection
    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)
    _, log_edges = cv2.threshold(laplacian, 3, 250, cv2.THRESH_BINARY)
    return canny_edges, log_edges.astype("uint8")
