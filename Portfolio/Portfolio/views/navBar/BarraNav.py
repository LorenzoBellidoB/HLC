import reflex as rx

from Portfolio.views.components.ButtonLinks import buttonLink

def barranavegacion() -> rx.Component:
    return rx.hstack(
        buttonLink("Home", "http/localhost:3000/", "#FFB200"),
        buttonLink("Git", "https://github.com/LorenzoBellidoB?tab=repositories", "#601d98"),
        buttonLink("Projects", "http/localhost:3000/", "#E05600"),
        buttonLink("Contact", "http/localhost:3000/", "#007400"),
        buttonLink("Curriculum", "http/localhost:3000/", "#008176"),
        position="sticky",
        padding="10px",
        zindex="1",
    )