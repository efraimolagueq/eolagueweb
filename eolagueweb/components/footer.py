import reflex as rx
import datetime

from eolagueweb.styles.styles import Size as Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© 2023 - {datetime.datetime.today().year} EOlagueDev by Efraim Olague v1.", 
            href="https://github.com/efraimolagueq",
            is_external=True,
            font_size=Size.MEDIUM.value,
        ),
        
        rx.text(
            "CREATING SOFTWARE WITH ♥ FROM MEXICO.",
            font_size=Size.MEDIUM.value,
        ),
        margin_bottom=Size.BIG.value,
        align_items="center",
    )