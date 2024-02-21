import reflex as rx
from enum import Enum

# CONSTANTS
MAX_WIDTH = "600px"

#SIZES
class Size(Enum):
    SMALL = ".5em"
    MEDIUM = ".8em"
    DEFAULT = "1em"
    BIG = "2em"
    
    
# Styles
BASE_STYLE = {
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
    },
    rx.link: {
        "text_decoration": "none",
        "hover": {
            "text_decoration": "none",
        },
    },
}

button_title_style = dict(
    font_size=Size.DEFAULT.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
)

title_style = dict(
    size="md",
    width="100%",
    padding_top=Size.DEFAULT.value,
)