from wordle.Wordle import Wordle


def test_realizaIntento0():
    wordle = Wordle()
    wordle.palabraJuego = 'VERDE'

    wordle.realizaIntento('MANCO')
    assert wordle.pistas == [['MANCO','-----'],['-----','-----'],['-----','-----'],['-----','-----'],['-----','-----'],['-----','-----']]

def test_realizaIntento1():
    wordle = Wordle()

    wordle.palabraJuego = 'VERDE'

    wordle.realizaIntento('MANOS')

    wordle.realizaIntento('MANCO')

    assert wordle.pistas == [['MANOS','-----'],['MANCO','-----'],['-----','-----'],['-----','-----'],['-----','-----'],['-----','-----']]

def test_realizaIntento2():
    wordle = Wordle()

    wordle.palabraJuego = 'VERDE'

    wordle.realizaIntento('MANOS')

    wordle.realizaIntento('MANCO')

    assert wordle.pistas == [['MANOS','-----'],['MANCO','-----'],['-----','-----'],['-----','-----'],['-----','-----'],['-----','-----']]

def test_realizaIntento3():
    wordle = Wordle()

    wordle.palabraJuego = 'VERDE'

    wordle.realizaIntento('MANOS')
    wordle.realizaIntento('MANCO')
    wordle.realizaIntento('PALOS')
    wordle.realizaIntento('PELOS')
    wordle.realizaIntento('VIUDA')
    wordle.realizaIntento('VERDE')

    assert wordle.pistas == [['MANOS','-----'],['MANCO','-----'],['PALOS','-----'],['PELOS','-----'],['SALTA','-----'],['CUOTA','-----']]