from parchis.JuegoParchis import Parchis

objeto = Parchis("Marco","Hector")

def test_pintaTablero1():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    objeto.fichaJ1 = 0
    objeto.fichaJ2 = 0
    res = objeto.pintaTablero()
    
    assert tablero == res


def test_pintaTablero2():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    objeto.fichaJ1 = 1
    objeto.fichaJ2 = 2
    res = objeto.pintaTablero()
    
    assert tablero == res

def test_pintaTablero3():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    objeto.fichaJ1 = 3
    objeto.fichaJ2 = 5
    res = objeto.pintaTablero()
    
    assert tablero == res

def test_pintaTablero4():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t\t\t\t\t\t\t\t\t\t\t\t0\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t\t\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    objeto.fichaJ1 = 12
    objeto.fichaJ2 = 6
    res = objeto.pintaTablero()
    
    assert tablero == res