import reflex as rx
import httpx
from datetime import datetime
import re

# ← Cambia esta URL cuando despliegues en Render
API_URL = "https://plataforma-de-reservas-y-ofertas-tur-sticas.onrender.com"

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
    nombre: str = ""
    correo: str = ""
    telefono: str = ""
    actividad: str = ""
    fecha: str = ""
    metodo_pago: str = ""
    cargando: bool = False

    async def reservar(self):
        # Validaciones locales
        if not all([self.nombre, self.correo, self.telefono, self.actividad, self.fecha, self.metodo_pago]):
            return rx.toast.error("⚠️ Completa todos los campos antes de reservar")

        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            return rx.toast.error("⚠️ Correo inválido")

        try:
            datetime.strptime(self.fecha, "%Y-%m-%d")
        except ValueError:
            return rx.toast.error("⚠️ Fecha inválida (usa YYYY-MM-DD)")

        # Enviar al backend
        self.cargando = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{API_URL}/api/reservas",
                    json={
                        "nombre": self.nombre,
                        "correo": self.correo,
                        "telefono": self.telefono,
                        "actividad": self.actividad,
                        "fecha": self.fecha,
                        "metodo_pago": self.metodo_pago,
                    },
                    timeout=10,
                )

            if response.status_code == 201:
                # Limpiar formulario
                self.nombre = ""
                self.correo = ""
                self.telefono = ""
                self.actividad = ""
                self.fecha = ""
                self.metodo_pago = ""
                return rx.toast.success("✅ ¡Reserva registrada exitosamente!")
            else:
                detalle = response.json().get("detail", "Error desconocido")
                return rx.toast.error(f"❌ Error: {detalle}")

        except httpx.ConnectError:
            return rx.toast.error("❌ No se pudo conectar con el servidor. Verifica que el backend esté corriendo.")
        except Exception as e:
            return rx.toast.error(f"❌ Error inesperado: {str(e)}")
        finally:
            self.cargando = False


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
                        rx.button(
                            rx.cond(
                                ReservaForm.cargando,
                                "Enviando...",
                                "Reservar"
                            ),
                            color_scheme="green",
                            size="4",
                            border_radius="md",
                            box_shadow="md",
                            on_click=ReservaForm.reservar,
                            disabled=ReservaForm.cargando,
                        ),
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