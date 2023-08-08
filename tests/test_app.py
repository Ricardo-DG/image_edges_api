import os
from app.main import create_app

dir_path = os.path.dirname(os.path.realpath(__file__))


class TestApp:
    test_img_url = "data/python_logo.png"

    @staticmethod
    def init_app():
        return create_app()

    def test_app_homepage(self):
        flask_app = self.init_app()
        with flask_app.test_client() as test_client:
            response = test_client.get("/")
            assert response.text == "Welcome to the Image Edges API!"

    def test_app_get_edges(self):
        flask_app = self.init_app()
        with flask_app.test_client() as test_client:
            response = test_client.post("/getEdges", data={"image": os.path.join(dir_path, self.test_img_url)})
            response_data = response.json
            assert isinstance(response_data["img"], list)

    def test_app_sharpen(self):
        flask_app = self.init_app()
        with flask_app.test_client() as test_client:
            response = test_client.post("/sharpen", data={"image": os.path.join(dir_path, self.test_img_url)})
            response_data = response.json
            assert isinstance(response_data["img"], list)

    def test_app_blur(self):
        flask_app = self.init_app()
        with flask_app.test_client() as test_client:
            response = test_client.post("/blur", data={"image": os.path.join(dir_path, self.test_img_url)})
            response_data = response.json
            assert isinstance(response_data["img"], list)
