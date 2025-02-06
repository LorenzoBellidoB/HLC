import reflex as rx


class State(rx.State):
    
     text: str = ""
     option:str = "Hombre"

@rx.page(
    route="/formulario",
    title="Formulario de registro - Mi web.",
)
def formulario() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text("Nombre", id="lNombre"),
            rx.input(
                id="iNombre",
                type="text",
                placeholder="Introduce tu nombre",
                width="300px",
                value=State.text,  # Enlazamos el estado al input
                on_change=State.set_text,  # Capturamos cambios
            )
        ),
        rx.hstack(
            rx.text("Apellidos", id="lApellidos"),
            rx.input(
                id="iApellidos",
                type="text",
                placeholder="Introduce tus apellidos",
                width="300px",
                value=State.text,  
                on_change=State.set_text,  # Capturamos cambios
            )
        ),
        rx.hstack(
            rx.text("Sexo", id="lSexo"),
            rx.radio(
                id="rSexo",
                items=["Hombre", "Mujer"],
                direction="row", 
            )
        ),
    )
