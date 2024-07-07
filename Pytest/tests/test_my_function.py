import pytest
import time
import source.my_function as my_function

def test_add():
    result = my_function.add(num1= 1, num2= 4 )
    assert result == 5

def test_divide():
    result  = my_function.divide(num1= 10 , num2 = 5)
    assert result == 2

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        result = my_function.divide(num1 = 10 , num2=0)
    assert True

def test_add_string():
    result = my_function.add(num1= "Akarsh " , num2= "Verma")

    assert result == "Akarsh Verma"


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_function.divide(num1 = 10 , num2=5)
    assert True

@pytest.mark.skip(reason= "This feature is broken")
def test_add():
    assert my_function.add(num1= 1, num2=3) == 2

@pytest.mark.xfail(reason = "dividing by Zero")
def test_divide_zero():
    my_function.divide(num1=4, num2=0)