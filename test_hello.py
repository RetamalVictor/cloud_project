from hello import *

def setup_funciton(function):
    print("Running Setup: %s" %{function.__name__})
    function.x = 10
def teardowm_function(function):
    print("Running Teardown: %s:" %{function.__name__})

#def test_hello_add():
    #assert add(test_hello_add.x) == 11

def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9