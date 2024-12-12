import reflex as rx

from ProyectoWeb.views.components.Button_link import buttonLink

def barranavegacion() -> rx.Component:
    return rx.hstack(
        buttonLink("Home", "http/localhost:3000/", "tomato"),
        buttonLink("About", "http/localhost:3000/", "teal"),
        position="sticky",
        padding="10px",
        zindex="1",
    )