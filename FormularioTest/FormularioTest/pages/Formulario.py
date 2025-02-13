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
                max_length=50,
                value=State.text,  # Enlazamos el estado al input
                on_change=State.set_text,  # Capturamos cambios
            )
        ),
        rx.hstack(
            rx.text("Apellidos", id="lApellidos"),
            rx.input(
                id="iApellidos",
                type="text",
                max_length=50,
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

        rx.hstack(
            rx.text("Correo", id="lCorreo"),
            rx.input(
                id="iCorreo",
                type="text",
                placeholder="Introduce tu correo",
                width="300px",
                value=State.text,  
                on_change=State.set_text,  # Capturamos cambios
            )
        ),

        rx.hstack(
            rx.checkbox(
                id="iCasilla",
                default_checked=True
            ),
            rx.text("Deseo recibir información sobre novedades y ofertas", id="lCasilla"),
        ),

        rx.hstack(
            rx.checkbox(
                id="iCasilla2",
            ),
            rx.text("Declaro haber leido y aceptar las condiciones generales del programa y la normativa sobre protección de datos", id="lCasilla2"),
        ),

        rx.input(
            id="iButton",
            type="submit",
            value="Enviar",
        ),
    )
