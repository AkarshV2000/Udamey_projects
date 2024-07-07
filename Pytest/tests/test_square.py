import pytest
import source.shapes as shape

@pytest.mark.parametrize("side_length, expected_area" , [(5,25) ,(4,16) , (9,81) ])
def test_multiple_area(side_length, expected_area):
    assert shape.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_parameter",[(3,12), (4,16), (5,20)])
def test_multiple_parameter(side_length, expected_parameter):
    assert shape.Square(side_length).perimeter() == expected_parameter