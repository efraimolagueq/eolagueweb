import reflex as rx


def header() -> rx.Component:
    return rx.vstack(
        rx.chakra.avatar(name="Efra Olague", size="xl"),
        rx.text("@efraolague", color="gray.500"),
        rx.text("HOLA 🖖 MI NOMBRE ES EFRAIM OLAGUE"),
        rx.text("""Soy un desarrollador de software, con experiencia en desarrollo FullStack. 
                Me gustan mucho utilizar Python y trabajo bastante con frameworks como FastAPI, 
                Django y Reflex. También he trabajado en redes de computadoras y me gustan 
                tecnologías como Android, Java y Go. Aprendiendo y aplicando herramientas 
                para la Nube como AWS."""),
        

    )