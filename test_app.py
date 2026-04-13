import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertIn("Jatin", greet("Jatin"))

    def test_farewell(self):
        self.assertIn("Jatin", farewell("Jatin"))

if __name__ == "__main__":
    unittest.main()
