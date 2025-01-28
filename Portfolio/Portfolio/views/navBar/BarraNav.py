import reflex as rx

from Portfolio.styles.styles import Routes
from Portfolio.views.components.ButtonLinks import buttonLink

def barranavegacion() -> rx.Component:
    return rx.hstack(
        buttonLink("Home", Routes.HOME.value, "#FFB200", "white"),
        buttonLink("Projects", "http/localhost:3000/", "#E05600", "white"),
        buttonLink("LinkedIn", "www.linkedin.com/in/lorenzo-bellido-barrena", "#008176", "white"),
        buttonLink("Contact", Routes.CONTACT.value, "#007400", "white"),
        position="sticky",
        padding="10px",
        zindex="1",
        top = "10px",
    )