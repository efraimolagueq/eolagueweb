import reflex as rx
import datetime


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(f"© 2023 - {datetime.datetime.today().year} EOlagueDev by Efraim Olague v1.", 
                href="https://github.com/efraimolagueq",
                is_external=True),
        rx.text("CREATING SOFTWARE WITH ♥ FROM MEXICO.")
    )