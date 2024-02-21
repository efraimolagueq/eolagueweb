import reflex as rx
from eolagueweb.components.link_button import link_button
from eolagueweb.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Mis Links"),
        link_button("Github", 
                    "TEXTooooooooooooooooooooooooooooooooooooooooooooooo",  
                    "https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("LinkedIn", 
                    "TEXTooooooooooooooooooooooooooooooooooooooooooooooo",
                    "https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("Twitch", 
                    "TEXTooooooooooooooooooooooooooooooooooooooooooooooo",
                    "https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("Discord", 
                    "TEXTooooooooooooooooooooooooooooooooooooooooooooooo",
                    "https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        title("Mis Links"),
        link_button("Github", 
                    "TEXTooooooooooooooooooooooooooooooooooooooooooooooo",  
                    "https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("Github", 
                    "TEXTooooooooooooooooooooooooooooooooooooooooooooooo",  
                    "https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        link_button("Github", 
                    "TEXTooooooooooooooooooooooooooooooooooooooooooooooo",  
                    "https://www.linkedin.com/in/efraim-olague-garay-8853b7193/"),
        
        width="100%",
        spacing="4"
    )