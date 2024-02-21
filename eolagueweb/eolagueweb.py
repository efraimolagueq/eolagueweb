import reflex as rx 

from eolagueweb.components.navbar import navbar
from eolagueweb.views.header.header import header
from eolagueweb.views.links.links import links
from eolagueweb.components.footer import footer

import eolagueweb.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
            ),
        ),
        footer(),
    )

rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )

app = rx.App(style=styles.BASE_STYLE)
app.add_page(index)