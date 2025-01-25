import reflex as rx

from Portfolio.views.components.ButtonLinks import buttonLink

def barranavegacion() -> rx.Component:
    return rx.hstack(
        buttonLink("Home", "http/localhost:3000/", "#FFB200", "white"),
        buttonLink("Projects", "http/localhost:3000/", "#E05600", "white"),
        buttonLink("LinkedIn", "www.linkedin.com/in/lorenzo-bellido-barrena", "#008176", "white"),
        buttonLink("Contact", "http/localhost:3000/", "#007400", "white"),
        position="sticky",
        padding="10px",
        zindex="1",
        top = "10px",
    )