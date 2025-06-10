import random
import pandas as pd
from faker import Faker
from utils import random_date

faker = Faker("es_AR")

# Listas generales
nombres = ["Juan", "Ana", "Luis", "Sofía", "María", "Pedro", "Valentina", "Mateo", "Camila", "Lucas"]
apellidos = ["García", "Pérez", "López", "Martínez", "Sánchez", "Fernández", "Rodríguez", "Gómez"]
emails = [f"{n.lower()}.{a.lower()}@mail.com" for n in nombres for a in apellidos]
localidades = ["CABA", "La Plata", "Rosario", "Córdoba", "Mendoza"]
razones_sociales = ["Servicios S.A.", "Comercial SRL", "Proveedora SA", "Distribuciones SRL", "Parque SRL"]
escuelas = ["Esc. N°1", "Esc. N°2", "Esc. N°3", "Esc. N°4", "Esc. N°5"]
puestos = ["Administrativo", "Animador", "Cajero", "RRHH", "Operador", "Gerente"]
turnos = ["Mañana", "Tarde", "Noche"]
metodos_pago = ["Efectivo", "Tarjeta", "Transferencia", "MercadoPago"]
tipos_entrada = ["General", "VIP", "Niño", "Jubilado"]
tipos_producto = ["Comida", "Bebida", "Merchandising"]
nombres_producto = ["Hamburguesa", "Gaseosa", "Llaverito", "Pancho", "Agua", "Remera"]
descripciones = [
    "Producto de alta calidad",
    "Ideal para eventos",
    "Presentación económica",
    "Duradero y confiable",
    "Edición limitada"
]
tipos_visita = ["Preventiva", "Correctiva", "Inspección", "Capacitación"]
categorias = ["Alimentos", "Limpieza", "Papelería", "Electrónica"]
subcategorias = ["Snacks", "Bebidas", "Detergentes", "Cuadernos", "Cables"]


def generate_value(dtype, col_name=None):
    dtype = dtype.upper()

    if col_name:
        col = col_name.lower()
        if col in ["categoria", "cat"]:
            return random.choice(categorias)
        if col in ["subcat", "subcategoria"]:
            return random.choice(subcategorias)
        if col in ["producto", "productos", "prod", "nombre_producto"]:
            return random.choice(nombres_producto)
        if "descripcion" in col:
            return random.choice(descripciones)
        if col == "telefono_escuela":
            return f"011-{random.randint(4000, 4999)}-{random.randint(1000, 9999)}"
        if col == "tipo_visita":
            return random.choice(tipos_visita)
        if col == "tipo_entrada":
            return random.choice(tipos_entrada)
        if col == "turno":
            return random.choice(turnos)
        if col == "metodo_pago":
            return random.choice(metodos_pago)
        if "nombre" in col and "producto" not in col:
            return random.choice(nombres)
        if "apellido" in col:
            return random.choice(apellidos)
        if "escuela" in col:
            return random.choice(escuelas)
        if "localidad" in col:
            return random.choice(localidades)
        if "puesto" in col or "cargo" in col:
            return random.choice(puestos)
        if "email" in col:
            return random.choice(emails)
        if ("telefono" in col or "celular" in col) and col != "telefono_escuela":
            return faker.phone_number()
        if "direccion" in col:
            return faker.street_address()
        if "dni" in col:
            return random.randint(10000000, 50000000)
        if "legajo" in col or "matricula" in col:
            return random.randint(1000, 9999)
        if "cuit" in col:
            return f"{random.randint(20, 33)}-{random.randint(10000000, 99999999)}-{random.randint(0, 9)}"
        if "razon_social" in col:
            return random.choice(razones_sociales)
        if "sueldo" in col or "importe" in col or "monto" in col or "precio" in col or "costo" in col:
            return round(random.uniform(1000, 50000), 2)
        if "horas" in col:
            return random.randint(0, 200)
        if "fecha" in col:
            return random_date().strftime("%Y-%m-%d")
        if "cantidad" in col:
            return random.randint(1, 10)
        if "id" in col:
            return random.randint(1, 9999)
    # Por tipo si no hay nombre específico
    if "INT" in dtype:
        return random.randint(1, 100)
    elif "CHAR" in dtype or "TEXT" in dtype:
        return faker.word()[:8]
    elif "DATE" in dtype:
        return random_date().strftime("%Y-%m-%d")
    elif "DECIMAL" in dtype or "NUMERIC" in dtype or "FLOAT" in dtype or "DOUBLE" in dtype:
        return round(random.uniform(1000.0, 50000.0), 2)
    elif "BOOL" in dtype:
        return random.choice([True, False])
    else:
        return faker.word()[:8]


def generate_table_data(table_name, columns, num_rows):
    """
    Genera un DataFrame con datos sintéticos.
    columns: lista de tuplas (columna, tipo)
    """
    data = []
    for _ in range(num_rows):
        row = {col: generate_value(dtype, col) for col, dtype in columns}
        data.append(row)
    df = pd.DataFrame(data)
    return df
