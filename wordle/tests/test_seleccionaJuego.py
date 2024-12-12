from wordle.Wordle import Wordle


def test_seleccionaJuego0():
    wordle = Wordle()
    assert wordle.seleccionaJuego() >= 0

def test_seleccionaJuego1():
    wordle = Wordle()
    assert wordle.seleccionaJuego() < len(wordle.PALABRAS)