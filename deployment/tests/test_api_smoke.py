import importlib
import sys
import types
import unittest

from fastapi.testclient import TestClient


def build_client(should_raise: bool = False) -> TestClient:
    fake_model = types.ModuleType("app.model.model")
    fake_model.__version__ = "test-model-v1"

    def fake_classifier(_image_path: str) -> int:
        if should_raise:
            raise RuntimeError("bad image")
        return 1

    fake_model.perform_image_classification = fake_classifier
    sys.modules["app.model.model"] = fake_model

    if "app.main" in sys.modules:
        del sys.modules["app.main"]

    app_module = importlib.import_module("app.main")
    return TestClient(app_module.app)


class ApiSmokeTests(unittest.TestCase):
    def test_home_endpoint_returns_health(self) -> None:
        client = build_client()
        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["health_check"], "OK")
        self.assertEqual(response.json()["model_version"], "test-model-v1")

    def test_predict_endpoint_returns_prediction(self) -> None:
        client = build_client()
        response = client.post(
            "/predict",
            files={"image": ("sample.jpg", b"fake-image-bytes", "image/jpeg")},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"predicted_class": 1})

    def test_predict_endpoint_handles_model_errors(self) -> None:
        client = build_client(should_raise=True)
        response = client.post(
            "/predict",
            files={"image": ("sample.jpg", b"fake-image-bytes", "image/jpeg")},
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Bad Request"})


if __name__ == "__main__":
    unittest.main()
