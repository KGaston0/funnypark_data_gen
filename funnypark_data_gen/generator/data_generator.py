import datetime
import random
import os
import pandas as pd
from faker import Faker
from utils import random_date
from datetime import datetime, timedelta

faker = Faker("es_AR")

# Listas generales y adicionales (igual que antes)
nombres = ["Juan", "Ana", "Luis", "Sofía", "María", "Pedro", "Valentina", "Mateo", "Camila", "Lucas"]
apellidos = ["García", "Pérez", "López", "Martínez", "Sánchez", "Fernández", "Rodríguez", "Gómez"]
emails = [f"{n.lower()}.{a.lower()}@mail.com" for n in nombres for a in apellidos]
localidades = ["CABA", "La Plata", "Rosario", "Córdoba", "Mendoza"]
razones_sociales = ["Servicios S.A.", "Comercial SRL", "Proveedora SA", "Distribuciones SRL", "Parque SRL"]
escuelas = ["Esc. N°1", "Esc. N°2", "Esc. N°3", "Esc. N°4", "Esc. N°5"]
tipos_escuela = ["Pública", "Privada"]
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
parques = [
    "Parque Fantasía", "Parque Magia", "Parque Hadas",
    "Parque Dragón", "Parque Hechizo", "Parque Duende"
]
regiones = ["Norte", "Sur", "Este", "Oeste", "Centro"]
locales = [f"Local {i}" for i in range(1, 11)]
ofertas = ["Sin oferta", "2x1", "Descuento 10%", "Combo familiar", "Promo verano"]
zonas_local = ["Entrada", "Centro", "Salida", "Sector A", "Sector B"]
capacitaciones = ["Atención al cliente", "Seguridad", "Primeros auxilios", "Ventas", "Animación"]
tipos_cliente = ["Socio", "Visitante", "Escuela", "Corporativo"]

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
        if "tipo_escuela" in col:
            return random.choice(tipos_escuela)
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
        if "parque" in col:
            return random.choice(parques)
        if "region" in col:
            return random.choice(regiones)
        if "local" in col and "localidad" not in col:
            return random.choice(locales)
        if "oferta" in col:
            return random.choice(ofertas)
        if "zona" in col:
            return random.choice(zonas_local)
        if "capacitacion" in col:
            return random.choice(capacitaciones)
        if "tipo_cliente" in col:
            return random.choice(tipos_cliente)
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
    data = []
    for _ in range(num_rows):
        row = {col: generate_value(dtype, col) for col, dtype in columns}
        data.append(row)
    df = pd.DataFrame(data)
    return df

def generar_escuelas_csv(path="output/entradas/escuela.csv"):
    codigos_escuela = [f"Esc. N°{i}" for i in range(1, 6)]
    nombres_escuela = ["San Martín", "Belgrano", "Sarmiento", "Mitre", "Rivadavia"]
    tipos_escuela = ["Pública", "Privada"]
    data = []
    for codigo, nombre in zip(codigos_escuela, nombres_escuela):
        data.append({
            "codigo_escuela": codigo,
            "nombre_escuela": nombre,
            "direccion_escuela": faker.street_address(),
            "tipo_escuela": random.choice(tipos_escuela)
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_tipo_visita_csv(path="output/entradas/tipo_visita.csv", num_tipos=20, descripciones=None, categorias=None):
    if descripciones is None:
        descripciones = [
            "Duradero y confiable",
            "Edición limitada",
            "Ideal para eventos",
            "Presentación económica",
            "Producto de alta calidad"
        ]
    if categorias is None:
        categorias = list(range(1, 101))
    data = []
    codigos_usados = set()
    while len(data) < num_tipos:
        codigo = random.randint(1, 100)
        if codigo in codigos_usados:
            continue
        codigos_usados.add(codigo)
        descripcion = random.choice(descripciones)
        arancel = round(random.uniform(1000, 50000), 2)
        categoria = random.choice(categorias)
        data.append({
            "codigo_tipo_visita": codigo,
            "descripcion_tipo_visita": descripcion,
            "arancel_por_alumno": arancel,
            "codigo_categoria": categoria
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_telefonos_escuela_csv(path="output/entradas/telefono_escuela.csv", num_escuelas=5, telefonos_por_escuela=5):
    data = []
    for codigo_escuela in range(1, num_escuelas + 1):
        for _ in range(telefonos_por_escuela):
            telefono = f"011-{random.randint(4000, 4999)}-{random.randint(1000, 9999)}"
            data.append({
                "codigo_escuela": codigo_escuela,
                "telefono_escuela": telefono
            })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_item_venta_csv(path="output/entradas/item_venta.csv", num_items=100):
    codigos_tipo_visita = list(range(1, 101))
    data = []
    for nro_ticket in range(1, num_items + 1):
        data.append({
            "nro_ticket": f"{nro_ticket:05d}",
            "codigo_tipo_visita": random.choice(codigos_tipo_visita),
            "cantidad_alumnos_reales": random.randint(1, 10),
            "arancel_por_alumno": round(random.uniform(1000, 50000), 2)
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_ventas_csv(path="output/entradas/venta.csv", num_ventas=100, codigos_empleado=None, codigos_escuela=None):
    if codigos_empleado is None:
        codigos_empleado = list(range(1, 21))
    if codigos_escuela is None:
        codigos_escuela = list(range(1, 21))
    data = []
    nro_tickets_usados = set()
    while len(data) < num_ventas:
        nro_ticket = random.randint(1000, 9999)
        if nro_ticket in nro_tickets_usados:
            continue
        nro_tickets_usados.add(nro_ticket)
        fecha = (datetime.now() - timedelta(days=random.randint(0, 365))).date()
        codigo_empleado = random.choice(codigos_empleado)
        codigo_escuela = random.choice(codigos_escuela)
        data.append({
            "nro_ticket": nro_ticket,
            "fecha": fecha,
            "codigo_empleado": codigo_empleado,
            "codigo_escuela": codigo_escuela
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_empleados_csv(path="output/entradas/empleado.csv", num_empleados=100):
    nombres = ["Valentina", "Camila", "Juan", "Ana", "Pedro", "María", "Lucas", "Mateo", "Luis", "Sofía"]
    apellidos = ["López", "Rodríguez", "Sánchez", "García", "Fernández", "Gómez", "Martínez", "Pérez"]
    data = []
    for codigo in range(1, num_empleados + 1):
        data.append({
            "codigo_empleado": codigo,
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos)
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_categorias_csv(path="output/entradas/categoria.csv", num_categorias=20):
    codigos_categoria = range(1, num_categorias)
    descripciones = [
        "Presentación económica",
        "Ideal para eventos",
        "Edición limitada",
        "Producto de alta calidad",
        "Duradero y confiable",
        "Apto para niños",
        "Edición coleccionista",
        "Producto ecológico",
        "Formato familiar",
        "Edición aniversario",
        "Edición premium",
        "Producto artesanal",
        "Edición digital",
        "Producto importado",
        "Edición especial temporada",
        "Producto nacional",
        "Edición exclusiva",
        "Producto personalizado",
        "Edición limitada numerada",
        "Producto recomendado"
    ]
    data = []
    for codigo in codigos_categoria:
        data.append({
            "codigo_categoria": codigo,
            "descripcion_categoria": random.choice(descripciones)
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

# Diccionario de generadores especiales
special_generators = {
    "escuela": generar_escuelas_csv,
    "categoria": generar_categorias_csv,
    "empleado": generar_empleados_csv,
    "item_venta": generar_item_venta_csv,
    "telefono_escuela": generar_telefonos_escuela_csv,
    "tipo_visita": generar_tipo_visita_csv,
    "venta": generar_ventas_csv,
}

def generar_csv_especial(tabla, path, num_rows=None):
    """
    Llama al generador especial correspondiente si existe.
    """
    key = tabla.lower()
    if key in special_generators:
        if key == "venta" and num_rows is not None:
            special_generators[key](path, num_rows)
        else:
            special_generators[key](path)
        return True
    return False