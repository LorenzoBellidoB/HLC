import reflex as rx

@rx.page(
    route="/redes_sociales",
)
def redes_sociales() -> rx.Component:
    return rx.vstack(
        rx.link("Instagram", href="https://www.instagram.com/", id="instagram"),
        rx.link("Facebook", href="https://www.facebook.com/", id="facebook"),
        rx.link("TikTok", href="https://www.tiktok.com/explore", id="tiktok"),
        rx.link("Volver", href="/", id="volver"),
    )