import reflex as rx



def buttonLink(text, url, color):
    return rx.button(
        rx.link(
            text,
            href=url,
            underline="none",
            color="white",
        ),
        bg=color,
        size="3",
    )
