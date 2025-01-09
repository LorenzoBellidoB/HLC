"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Portfolio.styles.styles import *
from Portfolio.views.footer.Footer import footer
from Portfolio.views.navBar.BarraNav import barranavegacion



class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.vstack(
        barranavegacion(),
        footer(),
        align="center",
    )

app = rx.App(
    stylesheets=["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap", "https://fonts.googleapis.com/css2?family=Jersey+15&display=swap", "https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap"]
    )
app.add_page(index)
app._compile()
