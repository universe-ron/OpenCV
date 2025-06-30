import numpy as np
import cv2


def fine_tune_and_save_result(
    image: "np.ndarray",
    canny_edges: "np.ndarray",
    log_edges: "np.ndarray",
    output_path: str,
) -> None:
    """
    Fine-tune edge detection results, combine them, and save the final output image.

    :param image: numpy.ndarray, original image
    :param canny_edges: numpy.ndarray, result of Canny edge detection
    :param log_edges: numpy.ndarray, result of LoG edge detection
    :param output_path: str, path to save the final output image
    """
    # Combine Canny and LoG edge detection results
    combined_edges = cv2.addWeighted(canny_edges, 0.5, log_edges, 0.5, 0)

    # Save the final output image
    cv2.imwrite(output_path, combined_edges)
    return combined_edges
