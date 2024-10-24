from ejercicio3 import codigo_Barras

def test_CodigoBarras1():
    assert codigo_Barras("1") == False

def test_CodigoBarras2():
    assert codigo_Barras("0") == True

def test_CodigoBarras3():
    assert codigo_Barras("65839522") == True

def test_CodigoBarras4():
    assert codigo_Barras("512936577942541234212") == False

def test_CodigoBarras5():
    assert codigo_Barras("65839521") == False

def test_CodigoBarras6():
    assert codigo_Barras("65839522") == True

def test_CodigoBarras7():
    assert codigo_Barras("8414533043847") == True

def test_CodigoBarras8():
    assert codigo_Barras("5029365779425") == True

def test_CodigoBarras9():
    assert codigo_Barras("5129365779425") == False
