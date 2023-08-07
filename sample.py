import cv2
import httpx
import numpy as np


if __name__ == "__main__":
    local_host = "localhost"
    filename = ""
    # Uncomment one of the following to run the functionality

    # Blur
    response = httpx.post(f"http://localhost:8888/blur", data={"image": filename})
    result = response.json()
    new_image = result["img"]

    # Get Edges
    # response = httpx.post(f"{local_host}/getEdges", data={"image": filename})
    # result = response.json()
    # new_image = result["img"]

    # Sharpen
    # response = httpx.post(f"{local_host}/sharpen", data={"image": filename})
    # result = response.json()
    # new_image = result["img"]

    # Show image
    cv2.imshow("custom_window_name", np.array(new_image).astype(np.uint8))
    cv2.waitKey(0)
