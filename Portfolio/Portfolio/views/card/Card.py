from Portfolio.styles.styles import Color
import reflex as rx

def card(titulo, descripcion, url,colorT,color, colorBg):
    return rx.card(
        rx.link(
            rx.flex(
                rx.avatar(src=url, size="5", border_radius="full"),
                rx.box(
                    rx.heading(titulo, size="3", color=colorT),
                    rx.text(
                        descripcion, 
                        font_size="1", 
                        color=color, 
                        no_of_lines=2  # Limitar el texto a 2 líneas para evitar overflow
                    ),
                ),
                spacing="4",  # Más espacio entre avatar y texto
                align_items="center",
            ),
            href="#",  # Asegúrate de actualizar el enlace si es necesario
            text_decoration="none",  # Quitar el subrayado del enlace
        ),
        as_child=True,
        width="250px",  # Hacer la tarjeta un poco más ancha
        border_radius="5",  # Bordes redondeados
        box_shadow="5",  # Sombra para darle profundidad
        padding="4",  # Relleno interno
        bg=colorBg,  # Fondo blanco para contraste
        _hover={"box_shadow": "xl", "transform": "scale(1.05)", "transition": "0.2s"},  # Animación al pasar el ratón
    )
