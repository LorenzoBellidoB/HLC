from parchis.JuegoParchis import Parchis


def test_esGanador0():
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ1 = 0
    parchis.fichaJ2 = 0
    assert parchis.esGanador() == ""

def test_esGanador1():
    
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ1 = 20
    assert parchis.esGanador() == parchis.nombreJ1 + " es el ganador"

def test_esGanador2():
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ2 = 20
    assert parchis.esGanador() == parchis.nombreJ2 + " es el ganador"ç

def test_esGanador3():
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ1 = 25
    assert parchis.esGanador() == ""

def test_esGanador3():
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ2 = 25
    assert parchis.esGanador() == ""