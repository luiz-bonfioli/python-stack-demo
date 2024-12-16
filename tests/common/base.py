from unittest import TestCase

from fastapi.testclient import TestClient

from src.application.controller import app


class BaseTestCase(TestCase):
    def setUp(self):
        self.client = TestClient(app)
