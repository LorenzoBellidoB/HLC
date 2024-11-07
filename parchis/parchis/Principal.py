from JuegoParchis import Parchis


tablero = "\tI\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\tF\n"
tablero += "Marco\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"
tablero += "Hector\tI\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tF\n"

prueba = Parchis("Marco", "Hector")

res = prueba.pintaTablero(0,0)

print(tablero)
print (res)