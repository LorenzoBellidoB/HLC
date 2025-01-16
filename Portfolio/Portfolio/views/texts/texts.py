import reflex as rx

from Portfolio.styles.styles import Size, Color

def titulo(texto, color):
    return rx.text(texto,
                   font_family="'Jersey 15'", 
                   size= Size.LARGE.value, 
                   font_weight="bold",
                   color=color)
def textoPrincipal(texto, color):
    return rx.text(texto,
                   font_family="Tinos", 
                   size= Size.LARGE.value, 
                   color=color)

def textoSecundario(texto, color):
    return rx.text(texto,
                   font_family="Tinos", 
                   size= Size.MEDIUM.value, 
                   color=color)

def parrafo(texto, color):
    return rx.text(texto,
                   font_family="Source Serif 4", 
                   size= Size.SMALL.value, 
                   color=color)