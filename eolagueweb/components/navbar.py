import reflex

def navbar() -> reflex.Component:
    return reflex.hstack(
        reflex.text(
                "Efra Olague Dev",
                height="40px",
            ),
        position="sticky",
        bg="blue",
        padding_x="16px",
        padding_y="8px",
        z_index=999,
    )