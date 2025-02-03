import reflex as rx

class State(rx.State):
    """The app state."""
    ...

def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Enlaces favoritos", id="enlaces"),
        rx.link("Buscadores", href="/buscadores", id="enlaceBuscadores"),
        rx.link("Redes Sociales", href="/redes_sociales", id="enlaceRedes"),
    )

def buscadores() -> rx.Component:
    return rx.vstack(
        rx.link("Google", href="https://www.google.com/", id="google"),
        rx.link("Bing", href="https://www.bing.com/?brdr=1", id="bing"),
        rx.link("Baidu", href="https://www.baidu.com/", id="baidu"),
        rx.link("Volver", href="/", id="volver"),
    )

def redes_sociales() -> rx.Component:
    return rx.vstack(
        rx.link("Instagram", href="https://www.instagram.com/", id="instagram"),
        rx.link("Facebook", href="https://www.facebook.com/", id="facebook"),
        rx.link("TikTok", href="https://www.tiktok.com/explore", id="tiktok"),
        rx.link("Volver", href="/", id="volver"),
    )

app = rx.App()
app.add_page(index)
app.add_page(buscadores, route="/buscadores")
app.add_page(redes_sociales, route="/redes_sociales")
