import reflex as rx
import eolagueweb.styles.styles as styles

def  title(text) -> rx.Component:
    return rx.heading(
        text,
        size="7",
        style=styles.title_style,
    )