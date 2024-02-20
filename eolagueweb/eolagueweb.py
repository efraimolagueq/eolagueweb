import reflex as rx 

from eolagueweb.components.navbar import navbar
from eolagueweb.views.header.header import header
from eolagueweb.views.links.links import links
from eolagueweb.components.footer import footer

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )

app = rx.App()
app.add_page(index)