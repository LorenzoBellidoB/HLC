from random import *

class Wordle:

#region Atributos
    PALABRAS = ['ANGEL', 'JAMON', 'LENTO', 'VERDE', 'PLAYA', 'HIELO', 'FUEGO', 'MANGO', 'BANCO', 'SALTO']
    
    numIntento = 0
    
#endregion

#region Constructores
    def __init__(self):
        self.pistas = [['-----','-----'],['-----','-----'],['-----','-----'],['-----','-----'],['-----','-----'],['-----','-----']]
        self.palabraJuego = ''
#endregion

#region Métodos
    def seleccionaJuego(self):
        numero = randint(0, len(self.PALABRAS) - 1)
        self.palabraJuego = self.PALABRAS[numero]
        return numero

    def realizaIntento(self, palabra):
        if(self.numIntento < 6):
            if self.pistas[0][0] == '-----':
                self.pistas[0][0] = palabra
                self.numIntento += 1
            elif self.pistas[1][0] == '-----':
                self.pistas[1][0] = palabra
                self.numIntento += 1
            elif self.pistas[2][0] == '-----':
                self.pistas[2][0] = palabra
                self.numIntento += 1
            elif self.pistas[3][0] == '-----':
                self.pistas[3][0] = palabra
                self.numIntento += 1
            elif self.pistas[4][0] == '-----':
                self.pistas[4][0] = palabra
                self.numIntento += 1
            elif self.pistas[5][0] == '-----':
                self.pistas[5][0] = palabra
                self.numIntento += 1

            

#endregion