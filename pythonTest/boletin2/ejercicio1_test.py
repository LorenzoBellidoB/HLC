from ejercicio1 import cifradoCesar

def test_cifrado():
    assert cifradoCesar("a", 5) == "f"

def test_cifrado2():
    assert cifradoCesar("a", 1) == "b"

def test_cifrado3():
    assert cifradoCesar("x", 3) == "a"