"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from Portfolio.views.navBar.BarraNav import barranavegacion



class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    return rx.vstack(
        barranavegacion()
    )

app = rx.App(state=State)
app.add_page(index)
app._compile()
