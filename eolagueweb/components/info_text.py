import reflex as rx
import eolagueweb.styles.styles as styles

def  info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.chakra.span(title, font_weight="bold", color="blue"),
        f" {body}", 
        font_size=styles.Size.MEDIUM.value,
    )