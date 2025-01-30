import reflex as rx

from Portfolio.styles.styles import Color, Routes

@rx.page(
    route=Routes.PROJECTS.value,
)

def project() -> rx.Component:
    return rx.vstack(
        rx.text("Projects", height="50px"),
    )