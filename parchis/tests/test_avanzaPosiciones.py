from parchis.JuegoParchis import Parchis

parchis = Parchis("Marco", "Hector")
def test_avanzaPosicionesJ11():
    parchis.dado1 = 1
    parchis.dado2 = 1
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == 2

def test_avanzaPosicionesJ21():
    parchis.dado1 = 1
    parchis.dado2 = 1
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 2

def test_avanzaPosicionesJ12():
    parchis.fichaJ1 = 0
    parchis.dado1 = 3
    parchis.dado2 = 2
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == 5

def test_avanzaPosicionesJ22():
    parchis.fichaJ2 = 0
    parchis.dado1 = 3
    parchis.dado2 = 2
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 5


def test_avanzaPosicionesJ13():
    parchis.fichaJ1 = 15
    parchis.dado1 = 5
    parchis.dado2 = 2
    parchis.avanzaPosiciones(1)
    assert parchis.fichaJ1 == 18

def test_avanzaPosicionesJ23():
    parchis.fichaJ2 = 15
    parchis.dado1 = 5
    parchis.dado2 = 2
    parchis.avanzaPosiciones(2)
    assert parchis.fichaJ2 == 18