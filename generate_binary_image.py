import cv2
import numpy as np
import random


def generate_binary_image(width: int, height: int, num_shapes: int) -> np.ndarray:
    """
    Generates a binary image with a black background and randomly placed shapes.

    Args:
    width (int): The width of the generated image.
    height (int): The height of the generated image.
    num_shapes (int): The number of shapes to be placed randomly in the image.

    Returns:
    np.ndarray: The generated binary image.
    """
    image = np.zeros((height, width), dtype=np.uint8)

    for _ in range(num_shapes):
        shape_type = np.random.choice(["circle", "rectangle", "line"])
        color = int(np.random.choice([0, 255]))

        if shape_type == "circle":
            center = (np.random.randint(0, width - 1), np.random.randint(0, height - 1))
            radius = np.random.randint(1, min(width, height) // 8)
            cv2.circle(image, center, radius, color, -1)
        elif shape_type == "rectangle":
            pt1 = (np.random.randint(0, width - 1), np.random.randint(0, height - 1))
            pt2 = (
                np.random.randint(pt1[0], width - 1),
                np.random.randint(pt1[1], height - 1),
            )
            cv2.rectangle(image, pt1, pt2, color, -1)
        elif shape_type == "line":
            pt1 = (np.random.randint(0, width - 1), np.random.randint(0, height - 1))
            pt2 = (np.random.randint(0, width - 1), np.random.randint(0, height - 1))
            thickness = np.random.randint(1, 5)
            cv2.line(image, pt1, pt2, color, thickness)

    return image


if __name__ == "__main__":
    # 產生影像
    img = generate_binary_image(512, 512, 10)

    # 顯示影像
    cv2.imshow("Generated Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
