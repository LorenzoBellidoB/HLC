import reflex as rx

def lang() -> rx.Component:
    return rx.script("document.documentElement.lang = 'es'")

index_title = "Lorenzo Bellido - Portfolio"
index_description = "Portafolio de Lorenzo Bellido - Desarrollador de Aplicaciones Multiplataforma"
index_meta = [
    {"name": "og:title", "content": index_title}, 
    {"name": "og:description", "content": index_description},
]