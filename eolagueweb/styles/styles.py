import reflex as rx
from enum import Enum
from .colors import Color, TextColor


# CONSTANTS
MAX_WIDTH = "600px"

#SIZES
class Size(Enum):
    ZERO = "0px !important"
    SMALL = ".5em"
    MEDIUM = ".8em"
    DEFAULT = "1em"
    BIG = "2em"
    
    
# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    rx.button: {
        "width": "100%",
        "height": "100%",
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.CONTENT.value,
        "color": TextColor.HEADER.value,
        "_hover": {
            "background_color": Color.SECONDARY.value,
        },
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
    color=TextColor.HEADER.value,
)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
)

title_style = dict(
    color=TextColor.HEADER.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
    
)