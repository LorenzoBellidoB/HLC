from random import *


class Parchis:
    TAM_TABLERO = 20
    dado1 = 0
    dado2 = 0

    def __init__(self,nombreJ1,nombreJ2):
        self.fichaJ1 = 0
        self.fichaJ2 = 0
        self.nombreJ1 = nombreJ1
        self.nombreJ2 = nombreJ2

    def tiraDados():
        Parchis.dado1 = randint(1, 6)
        Parchis.dado2 = randint(1, 6)

    def pintaTablero(self,fichaJ1, fichaJ2):
        res = ""

        for i in range (1,4):
            if i == 1:
                for j in range(0,Parchis.TAM_TABLERO + 1):
                    if j == 0:
                        res += "\tI"
                    elif j == Parchis.TAM_TABLERO:
                        res += "\tF\n"
                    else:
                        res += "\t" + str(j)
            elif i == 2:
                res += self.nombreJ1
                for j in range(0,Parchis.TAM_TABLERO + 1):
                    if j == 0:
                        res += "\tI"
                    elif j == Parchis.TAM_TABLERO:
                        res += "\tF\n"
                    elif j == fichaJ1 and fichaJ1 != 0:
                        res == "\t0"
                    else:
                        res += "\t"
            else:
                res += self.nombreJ2
                for j in range(0,Parchis.TAM_TABLERO + 1):
                    if j == 0:
                        res += "\tI"
                    elif j == Parchis.TAM_TABLERO:
                        res += "\tF\n"
                    elif j == fichaJ2 and fichaJ2 != 0:
                        res == "\t0"
                    else:
                        res += "\t"
        return res