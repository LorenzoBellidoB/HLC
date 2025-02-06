import reflex as rx

from rxconfig import config
from FormularioTest.pages.Formulario import formulario

app = rx.App(
    state=rx.State,
    stylesheets=["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap", "https://fonts.googleapis.com/css2?family=Jersey+15&display=swap", "https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap"]
)
# class State(rx.State):
    
#     ...


def index() -> rx.Component:
    return rx.container(
        
    )

app._compile()

