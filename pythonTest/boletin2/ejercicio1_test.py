from ejercicio1 import cifradoCesar

def test_cifrado():
    assert cifradoCesar("a", 5) == "f"

def test_cifrado2():
    assert cifradoCesar("a", 1) == "b"

def test_cifrado3():
    assert cifradoCesar("x", 4) == "b"

def test_cifrado4():
    assert cifradoCesar("ca", 1) == "db"

def test_cifrado4():
    assert cifradoCesar("za", 1) == "ab"

def test_cifrado5():
    assert cifradoCesar("za a", 1) == "ab b"

def test_cifrado6():
    assert cifradoCesar("hola me llamo marco", 1) == "ipmb nf mmbnp nbsdp"