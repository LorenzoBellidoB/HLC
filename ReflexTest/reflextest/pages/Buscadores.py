import reflex as rx

@rx.page(
    route="/buscadores",
)
def buscadores() -> rx.Component:
    return rx.vstack(
        rx.link("Google", href="https://www.google.com/", id="google"),
        rx.link("Bing", href="https://www.bing.com/?brdr=1", id="bing"),
        rx.link("Baidu", href="https://www.baidu.com/", id="baidu"),
        rx.link("Volver", href="/", id="volver"),
    )