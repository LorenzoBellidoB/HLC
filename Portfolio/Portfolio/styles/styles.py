# Constantes
from enum import Enum
import reflex as rx

MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    SMALL = "1"
    MEDIUM = "5"
    LARGE = "8"

# Colors
class Color(Enum):
    # Colores para el fondo
    BACKGROUND_DARK = "#121212"  # Negro ahumado para fondo oscuro
    BACKGROUND_MIDNIGHT = "#1A202C"  # Gris azulado oscuro, elegante y moderno
    BACKGROUND_OCEAN = "#2D3748"  # Gris oscuro con un toque azul para un ambiente sofisticado
    BACKGROUND_NIGHT = "#0D1117"  # Azul noche profundo, ideal para modo oscuro
    
    # Colores para textos
    TEXT_LIGHT = "#E2E8F0"  # Gris muy claro, perfecto para texto sobre fondo oscuro
    TEXT_MEDIUM = "#CBD5E0"  # Gris claro, para títulos o subtítulos
    TEXT_DARK = "#2D3748"  # Gris oscuro para texto principal (bueno para páginas oscuras)
    TEXT_VIVID = "#F5A623"  # Naranja cálido para destacar texto o llamados a la acción

    # Colores para botones
    BUTTON_PRIMARY = "#3182CE"  # Azul vibrante, moderno para botones de acción primaria
    BUTTON_SECONDARY = "#38A169"  # Verde esmeralda para botones secundarios o positivos
    BUTTON_WARNING = "#E53E3E"  # Rojo oscuro para botones de advertencia
    BUTTON_NEUTRAL = "#A0AEC0"  # Gris suave para botones neutrales o deshabilitados
    
    # Colores adicionales
    ACCENT_TEAL = "#4FD1C5"  # Teal brillante, perfecto para acentos y detalles llamativos
    ACCENT_PINK = "#D53F8C"  # Rosa fucsia, ideal para elementos que necesitan resaltar
    ACCENT_PURPLE = "#AC1ECF"  # Morado intenso, utilizado para áreas interactivas o decorativas
    ACCENT_YELLOW = "#D69E2E"  # Amarillo mostaza para detalles importantes o llamados a la acción
    ACCENT_SUNSET = "#F6AD55"  # Naranja suave, menos vibrante pero igualmente llamativo

class Routes(Enum):
    HOME = "/"
    PROJECTS = "/projects"
    LINKEDIN = "/linkedin"
    CONTACT = "/contact"


# Styles
BASE_STYLE = {
    rx.button: {
        "width: 100%"
        "height: 100%"
}
}

