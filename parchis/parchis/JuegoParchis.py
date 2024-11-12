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

    def pintaTablero(self):
        res = ""

        for i in range (1,4):
            if i == 1:
                for j in range(0,self.TAM_TABLERO + 1):
                    if j == 0:
                        res += "\tI"
                    elif j == self.TAM_TABLERO:
                        res += "\tF\n"
                    else:
                        res += "\t" + str(j)
            elif i == 2:
                res += self.nombreJ1
                for j in range(0,self.TAM_TABLERO + 1):
                    if j == 0:
                        res += "\tI"
                    elif j == self.TAM_TABLERO:
                        res += "\tF\n"
                    elif j == self.fichaJ1 and self.fichaJ1 != 0:
                        res += "\t0"
                    else:
                        res += "\t"
            else:
                res += self.nombreJ2
                for j in range(0,self.TAM_TABLERO + 1):
                    if j == 0:
                        res += "\tI"
                    elif j == self.TAM_TABLERO:
                        res += "\tF\n"
                    elif j == self.fichaJ2 and self.fichaJ2 != 0:
                        res += "\t0"
                    else:
                        res += "\t"
        return res
    
    def avanzaPosiciones(self,turno):
        if turno == 1:
            self.fichaJ1 += self.dado1 + self.dado2
            if self.fichaJ1 > self.TAM_TABLERO:
                self.fichaJ1 = self.TAM_TABLERO - (self.fichaJ1 - self.TAM_TABLERO)
        else:
            self.fichaJ2 += self.dado1 + self.dado2
            if self.fichaJ2 > self.TAM_TABLERO:
                self.fichaJ2 = self.TAM_TABLERO - (self.fichaJ2 - self.TAM_TABLERO)

    def estadoCarrera():
        return 0