from Portfolio.views.card.Card import card
from Portfolio.views.texts.texts import *
import reflex as rx
from Portfolio.styles.styles import *
from Portfolio.views.navBar.BarraNav import barranavegacion
from Portfolio.views.footer.Footer import footer
from Portfolio.views.perfil.Perfil import perfil

from Portfolio.utils import *

class State(rx.State):
    """The app state."""
    ...

@rx.page(
        route=Routes.HOME.value,
        title=index_title,
        description=index_description,
        meta=index_meta

)

def index() -> rx.Component:
    return rx.vstack(
        lang(),      
        perfil(),   
        barranavegacion(),
        cuerpo(),
        lenguajes(),
        footer(),
        align="center",
        bg_color=Color.BACKGROUND_NIGHT.value
    )

def cuerpo():
    return rx.vstack(
            textoSecundario("Hola mi nombre es Lorenzo", Color.TEXT_MEDIUM.value),
            textoPrincipal("Y soy Desarrollador de Aplicaciones Multiplataforma", Color.ACCENT_PURPLE.value),
            textoSecundario("Actualmente estoy cursando un Grado Superior en Desarrollo de Aplicaciones Multiplataforma, "
                        + "lo que me permite combinar creatividad y tecnología para crear soluciones innovadoras. "
                        + "Este portafolio refleja mis habilidades técnicas, proyectos y dedicación al aprendizaje continuo."
                        , Color.TEXT_MEDIUM.value),
            textoSecundario("¡Explora mi trabajo y descubre cómo puedo contribuir a tus proyectos!", Color.TEXT_MEDIUM.value),
            
        width="66%",
        margin_top="30px"
        ),

def lenguajes():
    return rx.vstack(
         textoPrincipal("Lenguajes Conocidos", Color.TEXT_MEDIUM.value),
         rx.hstack(
             card("Java", "Java es un lenguaje de programación orientado a objetos. ", "https://logodix.com/logo/283001.png"),
             card("Python", "Python es un lenguaje de programación interpretado.", "https://logodix.com/logo/283001.png"),
             card("C#", "C# .", "https://logodix.com/logo/283001.png"),
             card("ASP.NET", "ASP.NET .", "https://logodix.com/logo/283001.png"),
             card("Kotlin", "Kotlin .", "https://logodix.com/logo/283001.png"),
             margin_top="20px",
         ),
         rx.hstack(
             card("SQL", "SQL. ", "https://logodix.com/logo/283001.png"),
             card(".NET MAUI", ".NET MAUI.", "https://logodix.com/logo/283001.png"),
             card("JavaScript", "JavaScript.", "https://logodix.com/logo/283001.png"),
             card("XAML", "XAML", "https://logodix.com/logo/283001.png"),
             card("Angular", "Angular", "https://logodix.com/logo/283001.png"),
             margin_top="20px",
         ),
         width="66%",
         margin_top="60px",
    )

app = rx.App(
    stylesheets=["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap", "https://fonts.googleapis.com/css2?family=Jersey+15&display=swap", "https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap"]
)
app._compile()
