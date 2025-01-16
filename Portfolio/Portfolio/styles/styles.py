# Constantes
from enum import Enum
import reflex as rx

MAX_WIDTH = "600px"

# Sizes
class Size(Enum):
    SMALL = "1"
    MEDIUM = "4"
    LARGE = "8"

# Colors
class Color(Enum):
    PRIMARY = "#FFB43C"
    SECONDARY = "#E05600"

# Styles
BASE_STYLE = {
    rx.button: {
        "width: 100%"
        "height: 100%"
}
}