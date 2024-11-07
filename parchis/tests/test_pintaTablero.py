from parchis.JuegoParchis import Parchis

objeto = Parchis("Marco","Hector")

def test_pintaTablero1():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    
    res = objeto.pintaTablero(0,0)
    
    assert tablero == res


def test_pintaTablero2():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    res = objeto.pintaTablero(1,2)
    
    assert tablero == res

def test_pintaTablero3():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    res = objeto.pintaTablero(3,5)
    
    assert tablero == res

def test_pintaTablero4():
    tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
    tablero += "Marco\tI\t\t\t\t\t\t\t\t\t\t\t\t0\t\t\t\t\t\t\t\tF\n"
    tablero += "Hector\tI\t\t\t\t\t\t0\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

    res = Parchis.pintaTablero(12,6)
    
    assert tablero == res