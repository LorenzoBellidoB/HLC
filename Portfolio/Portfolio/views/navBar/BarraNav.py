import reflex as rx

from Portfolio.views.components.ButtonLinks import buttonLink

def barranavegacion() -> rx.Component:
    return rx.hstack(
        buttonLink("Home", "http/localhost:3000/", "#FFB43C"),
        buttonLink("Git", "https://github.com/LorenzoBellidoB?tab=repositories", "#E05600"),
        buttonLink("About", "http/localhost:3000/", "#008176"),
        position="sticky",
        padding="10px",
        zindex="1",
    )