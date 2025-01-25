import reflex as rx

def darken_color(hex_color, factor=0.7):
    """Oscurece un color hexadecimal multiplicando los valores RGB por un factor."""
    hex_color = hex_color.lstrip("#")
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    darker_rgb = tuple(max(0, int(c * factor)) for c in rgb)
    return "#{:02x}{:02x}{:02x}".format(*darker_rgb)

def buttonLink(text, url, color, text_color="white"):
    # Oscurece el color inicial
    dark_color = darken_color(color, factor=0.7)

    return rx.button(
        rx.link(
            text,
            href=url,
            underline="none",  # Elimina el subrayado
            color=text_color,  # Color inicial del texto
            _hover={
                "color": text_color,  # Mantén el texto blanco al pasar el ratón
                "textDecoration": "none",  # Asegúrate de que no se subraye
            },
            z_index="2",  # Asegura que el texto esté por encima del fondo
        ),
        bg=color,  # Color inicial del fondo
        size="3",
        position="relative",  # Necesario para el efecto de borde animado
        overflow="hidden",  # Evita que el borde se salga de los límites del botón
        border="2px solid transparent",  # Borde inicial transparente
        _before={
            "content": "''",  # Pseudo-elemento para la animación
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "0%",
            "height": "100%",
            "background": dark_color,  # Color oscuro para el hover
            "transition": "width 0.6s ease-out",  # Transición de izquierda a derecha
            "z-index": "1",  # Asegura que esté debajo del texto
        },
        _hover={
            "border": "2px solid white",  # Borde blanco brillante al pasar el ratón
            "_before": {
                "width": "100%",  # Llena el ancho del botón
            },
        },
        z_index="2",  # Asegura que el texto esté por encima de la animación
    )
