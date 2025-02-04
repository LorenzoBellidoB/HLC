import reflex as rx

@rx.page(
    route="/",
)
def index() -> rx.Component:
    
    return rx.vstack(
        rx.heading("Enlaces favoritos", id="enlaces"),
        rx.link("Buscadores", href="/buscadores", id="enlaceBuscadores"),
        rx.link("Redes Sociales", href="/redes_sociales", id="enlaceRedes"),
    )