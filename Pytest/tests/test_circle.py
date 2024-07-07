import pytest
import source.shapes as shape
import math


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shape.Circle(10)
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle


    def test_radius(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.parameter()
        expected_value = 2 * math.pi * self.circle.radius

        assert expected_value == result    
