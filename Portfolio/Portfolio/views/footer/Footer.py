import datetime
import reflex as rx

from Portfolio.views.texts.texts import parrafo


def footer() -> rx.Component:
    return rx.hstack(
        rx.icon(
        "copyright",
        width="20px",
    ),
    rx.link(
        f"{datetime.date.today().year} Pagina de Lorenzo Bellido",
        href="http/localhost:3000/",
        underline="none",
    )
    ) 
