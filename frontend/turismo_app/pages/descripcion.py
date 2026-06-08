import reflex as rx

VERDE = "#0D7A5F"
VERDE_CLARO = "#E8F5F0"
TURQUESA = "#00B4D8"
BLANCO = "#FFFFFF"
GRIS_CLARO = "#F8F9FA"
GRIS_TEXTO = "#555555"
NEGRO = "#1A1A2E"

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.text("🌴", font_size="1.5em"),
                rx.text("TurismoRD", font_weight="800", font_size="1.3em", color=VERDE),
                spacing="2", align="center",
            ),
            rx.hstack(
                rx.link("Inicio", href="/", color=NEGRO, font_weight="500", _hover={"color": VERDE}),
                rx.link("Destinos", href="/descripcion", color=VERDE, font_weight="700", border_bottom=f"2px solid {VERDE}"),
                rx.link("Reservar", href="/reservas", color=BLANCO, font_weight="600",
                        bg=VERDE, padding="0.5em 1.2em", border_radius="full", _hover={"bg": "#0a5c47"}),
                spacing="6", align="center",
            ),
            justify="between", align="center", width="100%", padding_x="3em", padding_y="1em",
        ),
        bg=BLANCO, position="sticky", top="0", z_index="100",
        box_shadow="0 2px 20px rgba(0,0,0,0.08)", width="100%",
    )

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("🌴 TurismoRD", font_weight="800", font_size="1.2em", color=BLANCO),
                    rx.text("Descubre la magia del Caribe", color="#aaa", font_size="0.9em"),
                    align_items="start", spacing="1",
                ),
                rx.vstack(
                    rx.text("Contacto", font_weight="700", color=BLANCO),
                    rx.text("📧 contacto@turismord.com", color="#aaa", font_size="0.9em"),
                    rx.text("📞 +1-809-555-1234", color="#aaa", font_size="0.9em"),
                    align_items="start", spacing="1",
                ),
                rx.vstack(
                    rx.text("Síguenos", font_weight="700", color=BLANCO),
                    rx.link("📸 Instagram", href="https://instagram.com", color=TURQUESA, font_size="0.9em"),
                    rx.link("📘 Facebook", href="https://facebook.com", color=TURQUESA, font_size="0.9em"),
                    align_items="start", spacing="1",
                ),
                justify="between", width="100%", padding_x="3em", padding_y="2em", flex_wrap="wrap", spacing="6",
            ),
            rx.divider(color="#333"),
            rx.text("© 2025 TurismoRD — Todos los derechos reservados", color="#666", font_size="0.8em", padding_y="1em"),
            spacing="0", align="center", width="100%",
        ),
        bg=NEGRO, width="100%",
    )

def dia_itinerario(dia, titulo, descripcion) -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.text(dia, color=BLANCO, font_weight="800", font_size="0.9em"),
            bg=VERDE, border_radius="full", width="45px", height="45px",
            display="flex", align_items="center", justify_content="center",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(titulo, font_weight="700", color=NEGRO),
            rx.text(descripcion, color=GRIS_TEXTO, font_size="0.9em"),
            spacing="1", align_items="start",
        ),
        spacing="4", align="start", width="100%",
    )

def descripcion() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),

            # Hero
            rx.box(
                rx.vstack(
                    rx.text("DESTINO DESTACADO", color=VERDE, font_weight="600", letter_spacing="3px", font_size="0.85em"),
                    rx.heading("Tour Playa Bávaro", size="9", color=NEGRO, text_align="center"),
                    rx.text(
                        "Un paraíso de aguas cristalinas, arena blanca y palmeras infinitas en el corazón del Caribe.",
                        color=GRIS_TEXTO, font_size="1.1em", text_align="center", max_width="600px",
                    ),
                    spacing="4", align="center", padding="4em 2em",
                ),
                bg=VERDE_CLARO, width="100%",
            ),

            # Galería
            rx.box(
                rx.hstack(
                    rx.image(
                        src="https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
                        width="100%", height="400px", object_fit="cover", border_radius="12px",
                    ),
                    rx.vstack(
                        rx.image(
                            src="https://images.unsplash.com/photo-1439405326854-014607f694d7?w=400",
                            width="100%", height="190px", object_fit="cover", border_radius="12px",
                        ),
                        rx.image(
                            src="https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400",
                            width="100%", height="190px", object_fit="cover", border_radius="12px",
                        ),
                        spacing="3", width="45%",
                    ),
                    spacing="4", align="start", width="100%",
                ),
                padding="3em", width="100%", max_width="1100px", margin="0 auto",
            ),

            # Detalles + Itinerario
            rx.hstack(
                # Detalles
                rx.box(
                    rx.vstack(
                        rx.text("DETALLES DEL TOUR", color=VERDE, font_weight="600", letter_spacing="2px", font_size="0.85em"),
                        rx.heading("Lo que incluye", size="6", color=NEGRO),
                        rx.vstack(
                            rx.hstack(rx.text("💰", font_size="1.3em"), rx.vstack(rx.text("Precio", font_weight="700", color=NEGRO), rx.text("$350 USD por persona", color=GRIS_TEXTO, font_size="0.9em"), spacing="0"), spacing="3"),
                            rx.hstack(rx.text("⏳", font_size="1.3em"), rx.vstack(rx.text("Duración", font_weight="700", color=NEGRO), rx.text("3 noches / 4 días", color=GRIS_TEXTO, font_size="0.9em"), spacing="0"), spacing="3"),
                            rx.hstack(rx.text("🌐", font_size="1.3em"), rx.vstack(rx.text("Idiomas", font_weight="700", color=NEGRO), rx.text("Español / Inglés", color=GRIS_TEXTO, font_size="0.9em"), spacing="0"), spacing="3"),
                            rx.hstack(rx.text("🏨", font_size="1.3em"), rx.vstack(rx.text("Alojamiento", font_weight="700", color=NEGRO), rx.text("Hotel 4★ todo incluido", color=GRIS_TEXTO, font_size="0.9em"), spacing="0"), spacing="3"),
                            rx.hstack(rx.text("🚌", font_size="1.3em"), rx.vstack(rx.text("Traslados", font_weight="700", color=NEGRO), rx.text("Incluidos desde Santo Domingo", color=GRIS_TEXTO, font_size="0.9em"), spacing="0"), spacing="3"),
                            spacing="4", align_items="start", width="100%",
                        ),
                        rx.link(
                            "Reservar este tour →",
                            href="/reservas",
                            bg=VERDE, color=BLANCO, border_radius="full",
                            font_weight="700", padding="0.8em 2em", width="100%",
                            _hover={"bg": "#0a5c47"},
                            text_decoration="none",
                            display="block",
                            text_align="center",
                        ),
                        spacing="5", align_items="start", width="100%",
                    ),
                    bg=BLANCO, border_radius="16px", padding="2em",
                    box_shadow="0 4px 20px rgba(0,0,0,0.08)", width="45%",
                ),

                # Itinerario
                rx.box(
                    rx.vstack(
                        rx.text("PROGRAMA", color=VERDE, font_weight="600", letter_spacing="2px", font_size="0.85em"),
                        rx.heading("Itinerario día a día", size="6", color=NEGRO),
                        dia_itinerario("D1", "Llegada y bienvenida", "Traslado desde el aeropuerto, check-in y cena de bienvenida en el resort."),
                        dia_itinerario("D2", "Playa y actividades", "Día libre en la playa. Deportes acuáticos, snorkeling y masaje opcional."),
                        dia_itinerario("D3", "Excursión cultural", "Tour por La Romana, Altos de Chavón y regreso al hotel para cena temática."),
                        dia_itinerario("D4", "Despedida", "Desayuno, check-out y traslado al aeropuerto. ¡Hasta pronto!"),
                        spacing="5", align_items="start", width="100%",
                    ),
                    bg=GRIS_CLARO, border_radius="16px", padding="2em", width="50%",
                ),
                spacing="6", align="start", padding="3em", width="100%", max_width="1100px",
                margin="0 auto", flex_wrap="wrap",
            ),

            footer(),
            spacing="0", width="100%",
        ),
        bg=BLANCO, width="100%", font_family="'Inter', sans-serif",
    )
