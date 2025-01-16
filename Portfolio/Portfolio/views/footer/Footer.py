import datetime
import reflex as rx

from Portfolio.views.texts.texts import parrafo


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(
                rx.icon(
                    "github",
                    color="white",
                    size=35
                ),
                href="https://github.com/LorenzoBellidoB"
                
            ),
            rx.link(
            rx.icon(
                "twitter",
                color="white",
                size=35
            ),
            href="https://x.com/lorenzobeba2"
        ),
        rx.link(
            rx.icon(
                "instagram",
                color="white",
                size=35
            ),
            href="https://instagram.com/lorenzobellidoo"
        ),
        spacing="5"
        ),
        
        rx.hstack(
            rx.icon(
        "copyright",
        width="20px",
    ),
    rx.link(
        f"{datetime.date.today().year} Pagina de Lorenzo Bellido",
        href="http/localhost:3000/",
        color="white",
        underline="none",
        style={":hover":{"color":"white"}}
    )
        ),
        align="center"
    ) 
