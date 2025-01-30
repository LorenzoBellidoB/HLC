from Portfolio.styles.styles import Color, SizeText
import reflex as rx
def perfil():        
    return rx.box(
        rx.hstack(
            rx.image(src="https://img.a.transfermarkt.technology/portrait/header/602105-1680698738.jpg?lm=1", alt="Tu cara", width="50px", height="50px", border_radius="50%"),
            rx.text(
                "Lorenzo Bellido", 
                font_size=SizeText.LARGE.value, 
                font_weight="bold", 
                color=Color.TEXT_MEDIUM.value,
                _hover=[{"cursor": "pointer"},{"text_decoration":"underline"},{"color":Color.TEXT_LIGHT.value}],
                ),
        ),
        position="absolute",  # Fijar la posición
        top="20px",  # Asegura que esté un poco abajo del borde superior
        left="100px",  # Asegura que esté un poco hacia la izquierda
        display="flex",
        align_items="center",  # Alinea la imagen y el texto
        z_index="10",  # Asegura que esté por encima de otros elementos
    ),