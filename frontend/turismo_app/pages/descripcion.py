import reflex as rx

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
        box_shadow="md"
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

def descripcion() -> rx.Component:
    return rx.container(
        rx.vstack(
            navbar(),

            # Hero section
            rx.container(
                rx.vstack(
                    rx.heading("Tour Playa Bávaro", size="8", color="blue"),
                    rx.text("Un destino paradisíaco con aguas cristalinas y arena blanca.", size="5"),
                    spacing="3",
                    align="center"
                ),
                padding="2em",
                bg="aliceblue",
                border_radius="lg",
                box_shadow="lg"
            ),

            # Galería de imágenes
            rx.hstack(
                rx.image(src="playa1.jpg", height="200px", border_radius="md", alt="Playa Bávaro vista 1"),
                rx.image(src="playa2.jpg", height="200px", border_radius="md", alt="Playa Bávaro vista 2"),
                rx.image(src="playa3.jpg", height="200px", border_radius="md", alt="Playa Bávaro vista 3"),
                spacing="4",
                justify="center",
                padding="1em"
            ),

            # Tabla de detalles dentro de una tarjeta
            rx.card(
                rx.table.root(
                    rx.table.header(
                        rx.table.row(
                            rx.table.column_header_cell("Detalle"),
                            rx.table.column_header_cell("Valor"),
                        )
                    ),
                    rx.table.body(
                        rx.table.row(rx.table.cell("💰 Precio"), rx.table.cell("USD 350")),
                        rx.table.row(rx.table.cell("⏳ Duración"), rx.table.cell("3 noches / 4 días")),
                        rx.table.row(rx.table.cell("🌐 Idioma"), rx.table.cell("Español / Inglés")),
                    ),
                    variant="surface",
                    size="2"
                ),
                box_shadow="md",
                border_radius="md",
                padding="1em",
                width="500px",
                align="center"
            ),

            # Itinerario con íconos
            rx.vstack(
                rx.heading("Itinerario", size="6"),
                rx.text("📅 Día 1: Llegada y check-in"),
                rx.text("🏖️ Día 2: Excursión a la playa"),
                rx.text("🚤 Día 3: Actividades acuáticas"),
                rx.text("✈️ Día 4: Regreso"),
                spacing="2",
                padding="1em"
            ),

            footer(),
            spacing="8",
            padding="2em"
        )
    )
