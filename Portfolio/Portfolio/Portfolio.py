import reflex as rx
from Portfolio.styles.styles import *
from Portfolio.views.navBar.BarraNav import barranavegacion
from Portfolio.views.footer.Footer import footer
from Portfolio.views.home.Home import home
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
        home(),
        footer(),
        align="center",
        bg_color=Color.BACKGROUND_NIGHT.value
    )

app = rx.App(
    stylesheets=["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,200..900;1,8..60,200..900&display=swap", "https://fonts.googleapis.com/css2?family=Jersey+15&display=swap", "https://fonts.googleapis.com/css2?family=Tinos:ital,wght@0,400;0,700;1,400;1,700&display=swap"]
)
app._compile()
