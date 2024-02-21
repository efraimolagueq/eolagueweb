import reflex as rx
from eolagueweb.styles.styles import Size  as Size
from eolagueweb.styles.colors import Color, TextColor

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.span(
                "EOlague",
                color=Color.PRIMARY.value,
            ),
            rx.chakra.span(
                "Dev",
                color=Color.SECONDARY.value,
            ),
        ),

        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0",
    )