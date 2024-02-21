import reflex as rx
import eolagueweb.constants as constants
from eolagueweb.components.link_button import link_button
from eolagueweb.components.title import title


def links() -> rx.Component:
    return rx.vstack(
        title("Dev Links"),
        link_button("LinkedIn", 
                    "Aqui puedes encontrar mi perfil profesional",  
                    constants.LINKEDIN_URL),
        link_button("Github", 
                    "Mi repositorio de proyectos",
                    constants.GITHUB_URL),

        title("Sobre Mí"),
        link_button("Instagram", 
                    "Puedes ver algunas de mis fotos favoritas",  
                    constants.INSTAGRAM_URL),
        link_button("Facebook", 
                    "Pasa a ver memes divertidos conmigo",  
                    constants.FACEBOOK_URL),
        link_button("Spotify", 
                    "Intercambiemos música",  
                    constants.SPOTIFY_URL),
        link_button("Last.fm", 
                    "Veamos que escuchamos juntos",  
                    constants.LASTFM_URL),
        link_button("Youtube", 
                    "Ve mis jugadas favoritas en videojuegos",  
                    constants.YOUTUBE_URL),
        link_button("Twitch", 
                    "Puedes verme perder partidas en vivo",  
                    constants.TWITCH_URL),
        link_button("Steam", 
                    "Agregame y juguemos juntos",  
                    constants.STEAM_URL),
        width="100%",
        spacing="4"
    )