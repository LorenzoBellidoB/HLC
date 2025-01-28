

import reflex as rx

@rx.page(
        route="/contact",

)

def contact() -> rx.Component:
    return rx.vstack(
        rx.text("Contacto", height="50px"),
    )
