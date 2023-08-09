from flask import Flask, jsonify, request  # type: ignore
from methods import get_edges_local_file, sharpen_img_local_file, blur_img_local_file


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def go_home():
        return "Welcome to the Image Edges API!"

    @app.route("/getEdges", methods=["POST"])
    def get_edges():
        img = request.form["image"]
        edges_img = get_edges_local_file(img)
        return jsonify({"img": edges_img})

    @app.route("/sharpen", methods=["POST"])
    def sharpen_img():
        img = request.form["image"]
        edges_img = sharpen_img_local_file(img)
        return jsonify({"img": edges_img})

    @app.route("/blur", methods=["POST"])
    def blur_img():
        img = request.form["image"]
        edges_img = blur_img_local_file(img)
        return jsonify({"img": edges_img})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8888)
    """
    # Example of usage
    # Imports
    import cv2
    import httpx
    import numpy as np
    # Main Logic
    local_host = "YOUR_LOCAL_HOST"
    filename = "PATH_TO_LOCAL_FILE_IMAGE"
    response = httpx.post(f"{local_host}/getEdges", data={"image": filename})
    result = response.json()
    new_image = result["img"]
    cv2.imshow("custom_window_name", np.array(new_image).astype(np.uint8))
    cv2.waitKey(0)
    """
