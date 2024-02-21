import reflex as rx
from eolagueweb.components.link_icon import link_icon
from eolagueweb.styles.styles import Size
from eolagueweb.components.info_text import info_text


def header() -> rx.Component:
    return rx.vstack(
        
        rx.hstack(
            rx.chakra.avatar(name="Efra Olague", size="xl"),
            rx.vstack(
                rx.heading(
                    "Soy Efraim Olague  🖖", 
                    size="7"
                ),
                rx.text(
                    "@efraolague", 
                    color="gray.500",
                    margin_top="0px !important",
                ),
                rx.hstack(
                    link_icon("https://github.com/efraimolagueq"),
                    link_icon("https://github.com/efraimolagueq"),
                    link_icon("https://github.com/efraimolagueq"),
                    link_icon("https://github.com/efraimolagueq"),
                ),
                align_items="start",
                spacing="3",
            ),
        ),
        
        rx.flex(
            info_text("+3", "Años de experiencia"),
            rx.spacer(),
            info_text("+3", "Años de experiencia"),
            rx.spacer(),
            info_text("+3", "Años de experiencia"),
            width="100%",
        ),
        
        rx.text("""Soy un desarrollador de software, con experiencia en desarrollo FullStack. 
                Me gustan mucho utilizar Python y trabajo bastante con frameworks como FastAPI, 
                Django y Reflex. También he trabajado en redes de computadoras y me gustan 
                tecnologías como Android, Java y Go. Aprendiendo y aplicando herramientas 
                para la Nube como AWS."""),
        spacing="5",
        align_items="start",
        

    )