import pytest
def greet():
    print("Hello")
def test_greet(capsys):
    greet()
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"