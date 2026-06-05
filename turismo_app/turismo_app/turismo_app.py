import reflex as rx
from pages.descripcion import descripcion
from pages.reservas import reservas

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link("🏠 Inicio", href="/", color="blue"),
        rx.link("📖 Descripción", href="/descripcion", color="blue"),
        rx.link("📝 Reservas", href="/reservas", color="blue"),
        spacing="6",
        padding="1em",
        bg="lightblue",
        position="sticky",
        top="0",
        z_index="10",
        box_shadow="md"   # sombra elegante
    )

def footer() -> rx.Component:
    return rx.hstack(
        rx.text("📧 contacto@turismoapp.com"),
        rx.text("📞 +1-809-555-1234"),
        rx.link("📸 Instagram", href="https://instagram.com/turismoapp"),
        spacing="6",
        justify="center",
        padding="1em",
        bg="lightgray"
    )

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            navbar(),

            # Hero section
            rx.container(
                rx.vstack(
                    rx.heading("Descubre tu próximo destino", size="9", color="blue"),
                    rx.text("Explora ofertas turísticas únicas en República Dominicana.", size="5"),
                    spacing="3",
                    align="center"
                ),
                padding="3em",
                bg="aliceblue",
                border_radius="lg",
                box_shadow="lg"
            ),

            # Buscador central
            rx.hstack(
                rx.input(placeholder="Destino", width="250px", border_radius="md", focus_border_color="blue"),
                rx.input(placeholder="Fecha (YYYY-MM-DD)", width="200px", border_radius="md", focus_border_color="blue"),
                rx.button("Buscar", color_scheme="blue", size="4", border_radius="md", box_shadow="md"),  # ← corregido
                spacing="4",
                justify="center",
                padding="1em"
            ),

            # Tarjetas de ofertas
            rx.grid(
                rx.card(
                    rx.vstack(
                        rx.image(src="playa.jpg", height="200px", border_radius="md"),
                        rx.heading("Paquete Playa Bávaro - 3 noches", size="5"),
                        rx.text("Disfruta de la playa más famosa del Caribe."),
                        rx.button("Reservar", color_scheme="blue", on_click=lambda: rx.redirect("/reservas")),
                        spacing="3"
                    ),
                    box_shadow="lg",
                    border_radius="lg",
                    padding="1em",
                    width="300px"
                ),
                rx.card(
                    rx.vstack(
                        rx.image(src="montana.jpg", height="200px", border_radius="md"),
                        rx.heading("Excursión Pico Duarte - 2 días", size="5"),
                        rx.text("La aventura más alta del Caribe."),
                        rx.button("Reservar", color_scheme="blue", on_click=lambda: rx.redirect("/reservas")),
                        spacing="3"
                    ),
                    box_shadow="lg",
                    border_radius="lg",
                    padding="1em",
                    width="300px"
                ),
                columns="2",
                spacing="6",
                justify="center"
            ),

            footer(),
            spacing="8",
            padding="2em"
        )
    )

app = rx.App()
app.add_page(index, route="/")
app.add_page(descripcion, route="/descripcion")
app.add_page(reservas, route="/reservas")
