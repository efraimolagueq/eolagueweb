import reflex as rx
from eolagueweb.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Github","https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("LinkedIn","https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("Twitch","https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("Discord","https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
    )