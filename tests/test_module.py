from jkapis.module import hello

def test_hello():
    assert hello() == "Hello, PyPI!"

def test_hello_not_empty():
    assert hello() != ""

def test_hello_type():
    assert isinstance(hello(), str)