import reflex as rx

from Portfolio.styles.styles import Size

def titulo(text, color):
    return rx.text(text,
                   font_family="'Jersey 15'", 
                   size= Size.LARGE, 
                   font_weight="bold",
                   color=color)
def textoPrincipal(text, color):
    return rx.text(text,
                   font_family="Tinos", 
                   size= Size.LARGE, 
                   color=color)

def textoSecundario(text, color):
    return rx.text(text,
                   font_family="Tinos", 
                   size= Size.MEDIUM, 
                   color=color)

def parrafo(text, color):
    return rx.text(text,
                   font_family="Source Serif 4", 
                   size= Size.SMALL, 
                   color=color)