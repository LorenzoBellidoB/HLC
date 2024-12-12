import reflex as rx

from ProyectoWeb.views.components.Button_link import buttonLink

def content_view() -> rx.Component:
    return rx.vstack(
        buttonLink("Intagram", "https://www.instagram.com/", "linear-gradient(204deg, #5851DB,#C13584 50%,#F77737)"),
        buttonLink("Youtube", "https://www.youtube.com/", "red"),
        buttonLink("X", "https://twitter.com/", "linear-gradient(204deg,#2f2f2f,#241d1d 30%, #000000)"),
        align="center",
    )