import datetime
import reflex as rx

from Portfolio.views.texts.texts import parrafo


def footer() -> rx.Component:
    return rx.hstack(
        rx.icon(
        "copyright",
        width="20px",
    ),
    parrafo("2025", "#FFB43C"),
    rx.link(
        "Pagina de Lorenzo Bellido",
        href="http/localhost:3000/",
        underline="none",
    )
    ) 
