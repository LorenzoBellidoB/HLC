import datetime
import reflex as rx

def footer() -> rx.Component:
    return rx.hstack(
        rx.icon(
        "hand-metal"
    ),
    rx.text(f"{datetime.date.today().year}", height="50px"),
    rx.link(
        "Pagina de Lorenzo Bellido",
        href="http/localhost:3000/",
        underline="none",
    )
    ) 
