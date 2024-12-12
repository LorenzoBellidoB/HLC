import reflex as rx

from ProyectoWeb.views.contenido.Content import content_view
from ProyectoWeb.views.footer.Footer import footer
from ProyectoWeb.views.header.Header import header
from ProyectoWeb.views.navbar.Navbar import barranavegacion
from ProyectoWeb.views.components.Button_link import buttonLink

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        barranavegacion(),
        header(),
        content_view(),
        footer(),
        align="center",
    )

app = rx.App(state=State)
app.add_page(index)
app._compile()
