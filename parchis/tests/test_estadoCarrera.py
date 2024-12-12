from parchis.JuegoParchis import Parchis


def test_estadoCarrera0():
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ1 = 1
    parchis.fichaJ2 = 1
    assert parchis.estadoCarrera() == "Empate"

def test_estadoCarrera1():
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ1 = 3
    parchis.fichaJ2 = 1
    assert parchis.estadoCarrera() == "Va ganando la carrera " + parchis.nombreJ1

def test_estadoCarrera3():
    parchis = Parchis("Marco", "Hector")
    parchis.fichaJ1 = 3
    parchis.fichaJ2 = 6
    assert parchis.estadoCarrera() == "Va ganando la carrera " + parchis.nombreJ2