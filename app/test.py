import requests
import io
from PIL import Image
from pathlib import Path
import base64

url = "http://localhost:8000/{path}"


def test_alive():
    response = requests.get(url.format(path="health"))

    assert response.status_code == 200

    print("TEST ALIVE PASSED")


def test_models():
    response = requests.get(url.format(path="models"))

    assert response.status_code == 200

    response = response.json()

    assert response == ["yolov5s", "yolov5m", "yolov5l"]

    print("TEST MODELS PASSED")


def test_processing():
    path = Path(__file__).parent / "cats.jpg"
    image = Image.open(path)
    with io.BytesIO() as buffer:
        image.save(buffer, format="PNG")
        buffer: str = base64.b64encode(buffer.getvalue()).decode("utf-8")

        data = {"model": "yolov5s", "image": buffer}

        response = requests.post(url.format(path="predict"), json=data)

    print(response.text)

    assert response.status_code == 200

    print(response.json())

    assert "time" in response

    assert "model" in response


if __name__ == "__main__":
    test_alive()
    test_models()
    test_processing()
