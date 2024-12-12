import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
            src="https://www.w3schools.com/howto/img_avatar.png",
            size = "7"
        ),
        rx.text("Lorenzo Bellido", height="50px"),
        ),
        rx.text("Hola. Mi nombre es Lorenzo", height="50px"),
        

    )