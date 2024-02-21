import reflex as rx
import eolagueweb.styles.styles as styles
from eolagueweb.styles.styles import TextColor, Color

def  info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.chakra.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value,
        ),
        f" {body}", 
        font_size=styles.Size.MEDIUM.value,
        color=TextColor.BODY.value,
    )