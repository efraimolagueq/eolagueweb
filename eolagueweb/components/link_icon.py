import reflex as rx
import eolagueweb.styles.styles as styles

def  link_icon(url:str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="link",  
            width=styles.Size.MEDIUM.value,
            height=styles.Size.MEDIUM.value,
        ),
        href=url,
        is_external=True,
    )