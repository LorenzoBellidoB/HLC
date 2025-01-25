from Portfolio.views.texts.texts import *
import reflex as rx

def home():
    return rx.vstack(
        textoSecundario("Hola mi nombre es Lorenzo", Color.TEXT_MEDIUM.value),
        textoPrincipal("Y soy Desarrollador de Aplicaciones Multiplataforma", Color.ACCENT_PURPLE.value),
        textoSecundario("Actualmente estoy cursando un Grado Superior en Desarrollo de Aplicaciones Multiplataforma, "
                        + "lo que me permite combinar creatividad y tecnología para crear soluciones innovadoras. "
                        + "Este portafolio refleja mis habilidades técnicas, proyectos y dedicación al aprendizaje continuo."
                        , Color.TEXT_MEDIUM.value),
        textoSecundario("¡Explora mi trabajo y descubre cómo puedo contribuir a tus proyectos!", Color.TEXT_MEDIUM.value),
        width="66%",
        
    )