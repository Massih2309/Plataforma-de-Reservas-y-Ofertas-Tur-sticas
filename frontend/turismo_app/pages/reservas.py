import reflex as rx
import httpx
from datetime import datetime
import re

API_URL = "https://plataforma-de-reservas-y-ofertas-tur.onrender.com"

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

def campo(placeholder, var, tipo="text") -> rx.Component:
    return rx.box(
        rx.input(
            placeholder=placeholder,
            bind=var,
            type=tipo,
            width="100%",
            padding="0.8em 1em",
            border="2px solid #e0e0e0",
            border_radius="8px",
            font_size="1em",
            bg=BLANCO,
            color=NEGRO,
            _focus={"border_color": VERDE, "outline": "none"},
            _placeholder={"color": "#999"},
        ),
        width="100%",
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
        if not all([self.nombre, self.correo, self.telefono, self.actividad, self.fecha, self.metodo_pago]):
            return rx.toast.error("⚠️ Completa todos los campos antes de reservar")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            return rx.toast.error("⚠️ Correo inválido")
        try:
            datetime.strptime(self.fecha, "%Y-%m-%d")
        except ValueError:
            return rx.toast.error("⚠️ Fecha inválida (usa YYYY-MM-DD)")

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
        except Exception as e:
            return rx.toast.error("❌ No se pudo conectar con el servidor.")
        finally:
            self.cargando = False


def reservas() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),

            # Hero
            rx.box(
                rx.vstack(
                    rx.text("RESERVA AHORA", color=VERDE, font_weight="600", letter_spacing="3px", font_size="0.85em"),
                    rx.heading("Tu aventura comienza aquí", size="9", color=NEGRO, text_align="center"),
                    rx.text(
                        "Completa el formulario y uno de nuestros asesores confirmará tu reserva.",
                        color=GRIS_TEXTO, font_size="1.1em", text_align="center", max_width="550px",
                    ),
                    spacing="4", align="center", padding="4em 2em",
                ),
                bg=VERDE_CLARO, width="100%",
            ),

            # Formulario + Info
            rx.hstack(
                # Formulario
                rx.box(
                    rx.vstack(
                        rx.text("DATOS DE RESERVA", color=VERDE, font_weight="600", letter_spacing="2px", font_size="0.85em"),
                        rx.heading("Información de contacto", size="6", color=NEGRO),
                        rx.vstack(
                            campo("Nombre completo", ReservaForm.nombre),
                            campo("Correo electrónico", ReservaForm.correo, "email"),
                            campo("Teléfono", ReservaForm.telefono, "tel"),
                            rx.divider(border_color="#e0e0e0"),
                            rx.text("Detalles de la actividad", font_weight="700", color=NEGRO, font_size="1em"),
                            campo("Actividad (ej: Playa Bávaro)", ReservaForm.actividad),
                            campo("Fecha (YYYY-MM-DD)", ReservaForm.fecha),
                            rx.select(
                                ["Tarjeta de crédito", "Tarjeta de débito", "Transferencia bancaria", "Efectivo"],
                                placeholder="💳 Método de pago",
                                on_change=ReservaForm.set_metodo_pago,
                                width="100%",
                                border="2px solid #e0e0e0",
                                border_radius="8px",
                                _focus={"border_color": VERDE},
                            ),
                            spacing="4", width="100%",
                        ),
                        rx.button(
                            rx.cond(
                                ReservaForm.cargando,
                                "Enviando...",
                                "Confirmar Reserva →",
                            ),
                            bg=VERDE,
                            color=BLANCO,
                            width="100%",
                            padding="0.9em",
                            border_radius="8px",
                            font_weight="700",
                            font_size="1.05em",
                            _hover={"bg": "#0a5c47"},
                            on_click=ReservaForm.reservar,
                            disabled=ReservaForm.cargando,
                        ),
                        spacing="5", align_items="start", width="100%",
                    ),
                    bg=BLANCO, border_radius="16px", padding="2.5em",
                    box_shadow="0 4px 30px rgba(0,0,0,0.08)", width="55%",
                ),

                # Info lateral
                rx.vstack(
                    rx.box(
                        rx.vstack(
                            rx.text("✅ Confirmación inmediata", font_weight="700", color=NEGRO),
                            rx.text("Recibirás un correo de confirmación al instante.", color=GRIS_TEXTO, font_size="0.9em"),
                            spacing="1", align_items="start",
                        ),
                        bg=BLANCO, border_radius="12px", padding="1.5em",
                        box_shadow="0 2px 10px rgba(0,0,0,0.06)", width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("🔒 Pago seguro", font_weight="700", color=NEGRO),
                            rx.text("Tus datos están protegidos con encriptación SSL.", color=GRIS_TEXTO, font_size="0.9em"),
                            spacing="1", align_items="start",
                        ),
                        bg=BLANCO, border_radius="12px", padding="1.5em",
                        box_shadow="0 2px 10px rgba(0,0,0,0.06)", width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("📞 Soporte 24/7", font_weight="700", color=NEGRO),
                            rx.text("Estamos disponibles para ayudarte en cualquier momento.", color=GRIS_TEXTO, font_size="0.9em"),
                            spacing="1", align_items="start",
                        ),
                        bg=BLANCO, border_radius="12px", padding="1.5em",
                        box_shadow="0 2px 10px rgba(0,0,0,0.06)", width="100%",
                    ),
                    rx.box(
                        rx.vstack(
                            rx.text("🌴 Destinos disponibles", font_weight="700", color=NEGRO),
                            rx.text("• Playa Bávaro", color=GRIS_TEXTO, font_size="0.9em"),
                            rx.text("• Pico Duarte", color=GRIS_TEXTO, font_size="0.9em"),
                            rx.text("• Bahía de Samaná", color=GRIS_TEXTO, font_size="0.9em"),
                            rx.text("• Altos de Chavón", color=GRIS_TEXTO, font_size="0.9em"),
                            spacing="1", align_items="start",
                        ),
                        bg=VERDE_CLARO, border_radius="12px", padding="1.5em",
                        border=f"1px solid {VERDE}", width="100%",
                    ),
                    spacing="4", width="40%",
                ),

                spacing="6", align="start", padding="3em", width="100%",
                max_width="1100px", margin="0 auto", flex_wrap="wrap",
            ),

            footer(),
            spacing="0", width="100%",
        ),
        bg=GRIS_CLARO, width="100%", font_family="'Inter', sans-serif",
    )
