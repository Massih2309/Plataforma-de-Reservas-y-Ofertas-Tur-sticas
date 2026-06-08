import reflex as rx
from pages.descripcion import descripcion
from pages.reservas import reservas

VERDE = "#0D7A5F"
VERDE_CLARO = "#E8F5F0"
TURQUESA = "#00B4D8"
BLANCO = "#FFFFFF"
GRIS_CLARO = "#F8F9FA"
GRIS_TEXTO = "#555555"
NEGRO = "#1A1A2E"

OFERTAS = [
    {
        "imagen": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=600",
        "titulo": "Paquete Playa Bávaro – 3 noches",
        "descripcion": "Disfruta de la playa más famosa del Caribe con hotel todo incluido y actividades acuáticas.",
        "precio": "$350 USD",
        "destino": "bavaro",
    },
    {
        "imagen": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=600",
        "titulo": "Excursión Pico Duarte – 2 días",
        "descripcion": "La aventura más alta del Caribe. Senderismo guiado hasta la cima más alta de las Antillas.",
        "precio": "$180 USD",
        "destino": "pico duarte",
    },
    {
        "imagen": "https://images.unsplash.com/photo-1439405326854-014607f694d7?w=600",
        "titulo": "Tour Samaná – Ballenas",
        "descripcion": "Observa las majestuosas ballenas jorobadas en la Bahía de Samaná con guía naturalista.",
        "precio": "$120 USD",
        "destino": "samana",
    },
]

class BusquedaState(rx.State):
    busqueda: str = ""

    def set_busqueda(self, valor: str):
        self.busqueda = valor.lower()

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
                rx.link("Destinos", href="/descripcion", color=NEGRO, font_weight="500", _hover={"color": VERDE}),
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

def oferta_card(imagen, titulo, descripcion_text, precio, destino) -> rx.Component:
    return rx.cond(
        (BusquedaState.busqueda == "") | BusquedaState.busqueda.contains(destino) | rx.Var.create(destino).contains(BusquedaState.busqueda),
        _card(imagen, titulo, descripcion_text, precio),
        rx.box(display="none"),
    )

def _card(imagen, titulo, descripcion_text, precio) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.image(src=imagen, width="100%", height="220px", object_fit="cover", border_radius="12px 12px 0 0"),
            rx.vstack(
                rx.text(titulo, font_weight="700", font_size="1.1em", color=NEGRO),
                rx.text(descripcion_text, color=GRIS_TEXTO, font_size="0.9em", line_height="1.5"),
                rx.hstack(
                    rx.text(f"Desde {precio}", font_weight="800", color=VERDE, font_size="1.1em"),
                    rx.link(
                        "Reservar →",
                        href="/reservas",
                        bg=VERDE, color=BLANCO, border_radius="full", font_weight="600",
                        padding="0.4em 1em", _hover={"bg": "#0a5c47"},
                        text_decoration="none",
                    ),
                    justify="between", width="100%", align="center",
                ),
                padding="1.2em", spacing="3", width="100%",
            ),
            spacing="0", width="100%",
        ),
        bg=BLANCO, border_radius="12px", box_shadow="0 4px 20px rgba(0,0,0,0.08)",
        overflow="hidden", width="320px",
        _hover={"transform": "translateY(-4px)", "box_shadow": "0 8px 30px rgba(0,0,0,0.12)"},
        transition="all 0.3s ease",
    )

def index() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),

            # Hero section
            rx.box(
                rx.vstack(
                    rx.text("🌴 República Dominicana", color=VERDE, font_weight="600", font_size="1em", letter_spacing="2px"),
                    rx.heading(
                        "Descubre tu próximo",
                        rx.text("destino soñado", as_="span", color=VERDE),
                        size="9", color=NEGRO, text_align="center", line_height="1.2",
                    ),
                    rx.text(
                        "Playas cristalinas, montañas majestuosas y cultura vibrante te esperan en el Caribe.",
                        color=GRIS_TEXTO, font_size="1.1em", text_align="center", max_width="600px",
                    ),
                    rx.hstack(
                        rx.input(
                            placeholder="🔍 ¿A dónde quieres ir?",
                            on_change=BusquedaState.set_busqueda,
                            width="280px", border_radius="full",
                            border="2px solid #e0e0e0", padding="0.7em 1.2em",
                            bg=BLANCO, color=NEGRO,
                            _focus={"border_color": VERDE},
                            _placeholder={"color": "#999"},
                        ),
                        rx.input(
                            placeholder="📅 Fecha",
                            width="180px", border_radius="full",
                            border="2px solid #e0e0e0", padding="0.7em 1.2em",
                            bg=BLANCO, color=NEGRO,
                            _focus={"border_color": VERDE},
                            _placeholder={"color": "#999"},
                        ),
                        rx.button(
                            "Buscar", bg=VERDE, color=BLANCO, border_radius="full",
                            font_weight="700", padding="0.7em 2em", font_size="1em",
                            _hover={"bg": "#0a5c47"},
                        ),
                        spacing="3", flex_wrap="wrap", justify="center",
                    ),
                    spacing="6", align="center", padding="5em 2em",
                ),
                bg=VERDE_CLARO, width="100%",
            ),

            # Stats bar
            rx.box(
                rx.hstack(
                    rx.vstack(rx.text("500+", font_weight="800", font_size="1.8em", color=VERDE), rx.text("Destinos", color=GRIS_TEXTO, font_size="0.9em"), spacing="0", align="center"),
                    rx.divider(orientation="vertical", height="40px"),
                    rx.vstack(rx.text("10K+", font_weight="800", font_size="1.8em", color=VERDE), rx.text("Viajeros felices", color=GRIS_TEXTO, font_size="0.9em"), spacing="0", align="center"),
                    rx.divider(orientation="vertical", height="40px"),
                    rx.vstack(rx.text("15+", font_weight="800", font_size="1.8em", color=VERDE), rx.text("Años de experiencia", color=GRIS_TEXTO, font_size="0.9em"), spacing="0", align="center"),
                    rx.divider(orientation="vertical", height="40px"),
                    rx.vstack(rx.text("4.9⭐", font_weight="800", font_size="1.8em", color=VERDE), rx.text("Calificación", color=GRIS_TEXTO, font_size="0.9em"), spacing="0", align="center"),
                    spacing="8", justify="center", flex_wrap="wrap", padding="2em",
                ),
                bg=BLANCO, width="100%", box_shadow="0 2px 10px rgba(0,0,0,0.05)",
            ),

            # Ofertas section
            rx.vstack(
                rx.vstack(
                    rx.text("NUESTROS DESTINOS", color=VERDE, font_weight="600", letter_spacing="3px", font_size="0.85em"),
                    rx.heading("Ofertas Turísticas", size="8", color=NEGRO),
                    rx.text("Experiencias únicas en los destinos más hermosos del Caribe", color=GRIS_TEXTO),
                    spacing="2", align="center",
                ),
                rx.hstack(
                    *[oferta_card(o["imagen"], o["titulo"], o["descripcion"], o["precio"], o["destino"]) for o in OFERTAS],
                    spacing="6", justify="center", flex_wrap="wrap", padding_x="2em",
                ),
                spacing="8", align="center", padding="4em 2em", width="100%", bg=GRIS_CLARO,
            ),

            # CTA section
            rx.box(
                rx.vstack(
                    rx.heading("¿Listo para tu aventura?", size="8", color=BLANCO, text_align="center"),
                    rx.text("Reserva ahora y obtén los mejores precios garantizados", color="#ccc", text_align="center"),
                    rx.link(
                        "Hacer una reserva →",
                        href="/reservas",
                        bg=BLANCO, color=VERDE, border_radius="full", font_weight="700",
                        font_size="1.1em", padding="0.8em 2.5em", _hover={"bg": VERDE_CLARO},
                        text_decoration="none",
                    ),
                    spacing="4", align="center", padding="5em 2em",
                ),
                bg=VERDE, width="100%",
            ),

            footer(),
            spacing="0", width="100%",
        ),
        bg=BLANCO, width="100%", font_family="'Inter', sans-serif",
    )

app = rx.App(
    stylesheets=["https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"],
)
app.add_page(index, route="/")
app.add_page(descripcion, route="/descripcion")
app.add_page(reservas, route="/reservas")
