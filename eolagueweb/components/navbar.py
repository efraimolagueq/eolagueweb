import reflex
from eolagueweb.styles.styles import Size  as Size

def navbar() -> reflex.Component:
    return reflex.hstack(
        reflex.text(
                "EOlagueDev",
            ),
        position="sticky",
        bg="lightgray",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999",
        top="0",
    )