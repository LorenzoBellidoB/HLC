
import reflex as rx

from Portfolio.styles.styles import Color, Routes
from Portfolio.utils import lang
from Portfolio.views.card.Card import card
from Portfolio.views.footer.Footer import footer
from Portfolio.views.navBar.BarraNav import barranavegacion
from Portfolio.views.perfil.Perfil import perfil
from Portfolio.views.texts.texts import *

class State(rx.State):
    pass


@rx.page(
        route = "/",
)

def principal() -> rx.Component:
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
    card("Java", "Java es un lenguaje de programación orientado a objetos.", "https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg"),
    card("Python", "Python es un lenguaje de programación interpretado.", "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"),
    card("C#", "C# es un lenguaje desarrollado por Microsoft.", "https://upload.wikimedia.org/wikipedia/commons/4/4f/Csharp_Logo.png"),
    card("ASP.NET", "ASP.NET es un framework desarrollado por Microsoft.", "https://upload.wikimedia.org/wikipedia/commons/0/0e/Microsoft_.NET_logo.png"),
    card("Kotlin", "Kotlin es un lenguaje de programación estáticamente tipado.", "https://upload.wikimedia.org/wikipedia/commons/7/74/Kotlin_Icon.png"),
    margin_top="20px",
),
rx.hstack(
    card("SQL", "SQL es un lenguaje de consulta para gestionar BBDD relacionales.", "https://seeklogo.com/images/A/azure-sql-database-logo-D7A32C9CD9-seeklogo.com.png"),
    card(".NET MAUI", ".NET MAUI sirve para la creación de aplicaciones multiplataforma.", "https://upload.wikimedia.org/wikipedia/commons/0/0e/Microsoft_.NET_logo.png"),
    card("JavaScript", "JavaScript es un lenguaje interpretado que se utiliza en el desarrollo web.", "https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png"),
    card("Angular", "Angular es un framework de aplicaciones web de código abierto.", "https://upload.wikimedia.org/wikipedia/commons/c/cf/Angular_full_color_logo.svg"),
    margin_top="20px",
),

         width="66%",
         margin_top="60px",
         align="center"
    )

