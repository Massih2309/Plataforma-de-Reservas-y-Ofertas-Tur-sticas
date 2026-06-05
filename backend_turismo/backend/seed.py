"""
Script para poblar la BD con datos de ejemplo.
Ejecutar UNA vez después de crear las tablas:
    python seed.py
"""
from app.database import SessionLocal, engine, Base
from app.models import Oferta

Base.metadata.create_all(bind=engine)

ofertas_iniciales = [
    {
        "nombre": "Paquete Playa Bávaro – 3 noches",
        "descripcion": "Disfruta de la playa más famosa del Caribe con hotel todo incluido, actividades acuáticas y traslados desde Santo Domingo.",
        "precio": 350.00,
        "duracion": "3 noches / 4 días",
        "destino": "Bávaro",
        "imagen_url": "playa.jpg",
    },
    {
        "nombre": "Excursión Pico Duarte – 2 días",
        "descripcion": "La aventura más alta del Caribe. Senderismo guiado hasta la cima del Pico Duarte, la montaña más alta de las Antillas.",
        "precio": 180.00,
        "duracion": "2 días / 1 noche",
        "destino": "La Vega",
        "imagen_url": "montana.jpg",
    },
    {
        "nombre": "Tour Samaná – Ballenas Jorobadas",
        "descripcion": "Observa las majestuosas ballenas jorobadas en la Bahía de Samaná entre enero y marzo. Incluye bote y guía naturalista.",
        "precio": 120.00,
        "duracion": "1 día",
        "destino": "Samaná",
        "imagen_url": "ballenas.jpg",
    },
]

db = SessionLocal()
try:
    if db.query(Oferta).count() == 0:
        for data in ofertas_iniciales:
            db.add(Oferta(**data))
        db.commit()
        print("✅ Datos de ejemplo insertados correctamente.")
    else:
        print("ℹ️  La tabla 'ofertas' ya tiene datos. No se insertó nada.")
finally:
    db.close()
