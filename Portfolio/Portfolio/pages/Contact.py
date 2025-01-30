import reflex as rx
from Portfolio.styles.styles import Color, Routes

@rx.page(
    route=Routes.CONTACT.value,
)

def contact() -> rx.Component:
    return rx.vstack(
        rx.text("Contacto", height="50px"),
    )
