import reflex as rx
from datetime import datetime
import re

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

class ReservaForm(rx.State):
    nombre: str
    correo: str
    telefono: str
    actividad: str
    fecha: str
    metodo_pago: str

    def reservar(self):
        if not all([self.nombre, self.correo, self.telefono, self.actividad, self.fecha, self.metodo_pago]):
            return rx.toast.error("⚠️ Completa todos los campos antes de reservar")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            return rx.toast.error("⚠️ Correo inválido")
        try:
            datetime.strptime(self.fecha, "%Y-%m-%d")
        except ValueError:
            return rx.toast.error("⚠️ Fecha inválida (usa YYYY-MM-DD)")
        return rx.toast.success(
            f"✅ Reserva creada para {self.nombre} en {self.actividad} el {self.fecha}"
        )

def reservas() -> rx.Component:
    return rx.container(
        rx.vstack(
            navbar(),
            rx.heading("Reservar Actividad", size="8", color="blue"),

            rx.card(
                rx.form(
                    rx.vstack(
                        rx.input(placeholder="Nombre completo", bind=ReservaForm.nombre, border_radius="md", focus_border_color="blue"),
                        rx.input(placeholder="Correo electrónico", bind=ReservaForm.correo, border_radius="md", focus_border_color="blue"),
                        rx.input(placeholder="Teléfono", bind=ReservaForm.telefono, border_radius="md", focus_border_color="blue"),
                        rx.input(placeholder="Actividad", bind=ReservaForm.actividad, border_radius="md", focus_border_color="blue"),
                        rx.input(placeholder="Fecha (YYYY-MM-DD)", bind=ReservaForm.fecha, border_radius="md", focus_border_color="blue"),
                        rx.input(placeholder="Método de pago", bind=ReservaForm.metodo_pago, border_radius="md", focus_border_color="blue"),
                        rx.button("Reservar", color_scheme="green", size="4", border_radius="md", box_shadow="md", on_click=ReservaForm.reservar),  # ← corregido
                        spacing="4",
                        padding="1em"
                    )
                ),
                box_shadow="lg",
                border_radius="lg",
                padding="2em",
                width="500px"
            ),

            footer(),
            spacing="8",
            padding="2em",
            align="center"
        )
    )
