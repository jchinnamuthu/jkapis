from jkapis.module import hello

class TestHello:
    def test_hello(self):
        assert hello() == "Hello, PyPI!"

    def test_hello_not_empty(self):
        assert hello() != ""

    def test_hello_type(self):
        assert isinstance(hello(), str)