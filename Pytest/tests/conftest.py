import pytest 
import source.shapes as shape


@pytest.fixture
def my_rectangle():
    return shape.Rectangle(length= 10 , width= 20)

@pytest.fixture
def weird_rectangle():
    return shape.Rectangle(length=5, width=6)