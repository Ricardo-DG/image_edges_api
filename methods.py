import cv2  # type: ignore
from items import Kernel


def get_edges_local_file(img_filename: str) -> list:
    # Read the original image
    img = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)
    # Apply kernel
    edg_img = cv2.filter2D(img, -1, kernel=Kernel.Laplacian)
    # Display original image
    return edg_img.tolist()


def sharpen_img_local_file(img_filename: str) -> list:
    # Read the original image
    img = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)
    # Apply kernel
    edg_img = cv2.filter2D(img, -1, kernel=Kernel.Sharpen)
    # Display original image
    return edg_img.tolist()


def blur_img_local_file(img_filename: str) -> list:
    # Read the original image
    img = cv2.imread(img_filename, cv2.IMREAD_GRAYSCALE)
    # Apply kernel
    edg_img = cv2.filter2D(img, -1, kernel=Kernel.Blur)
    # Display original image
    return edg_img.tolist()
