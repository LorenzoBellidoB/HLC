from reflextest.pages.Index import index
from reflextest.pages.Buscadores import buscadores
from reflextest.pages.Redes import redes_sociales
import reflex as rx



app = rx.App(
    state=rx.State,
    stylesheets=["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap", "https://fonts.googleapis.com/css2?family=Jersey+15&display=swap", "https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap"]
)

app._compile()
