import random
import os
import pandas as pd
import re
from faker import Faker
from utils import random_date
from datetime import datetime, timedelta

faker = Faker("es_AR")

# Listas de datos
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
locales = [i for i in range(1, 11)]
ofertas = ["Sin oferta", "2x1", "Descuento 10%", "Combo familiar", "Promo verano"]
zonas_local = ["Entrada", "Centro", "Salida", "Sector A", "Sector B"]
capacitaciones = ["Atención al cliente", "Seguridad", "Primeros auxilios", "Ventas", "Animación"]
tipos_cliente = ["Socio", "Visitante", "Escuela", "Corporativo"]

# Generadores por columna
def gen_categoria(): return random.choice(categorias)
def gen_subcategoria(): return random.choice(subcategorias)
def gen_producto(): return random.choice(nombres_producto)
def gen_descripcion(): return random.choice(descripciones)
def gen_telefono_escuela(): return f"011-{random.randint(4000, 4999)}-{random.randint(1000, 9999)}"
def gen_tipo_visita(): return random.choice(tipos_visita)
def gen_tipo_entrada(): return random.choice(tipos_entrada)
def gen_turno(): return random.choice(turnos)
def gen_metodo_pago(): return random.choice(metodos_pago)
def gen_nombre(): return random.choice(nombres)
def gen_apellido(): return random.choice(apellidos)
def gen_escuela(): return random.choice(escuelas)
def gen_tipo_escuela(): return random.choice(tipos_escuela)
def gen_localidad(): return random.choice(localidades)
def gen_puesto(): return random.choice(puestos)
def gen_email(): return random.choice(emails)
def gen_telefono(): return faker.phone_number()
def gen_direccion(): return faker.street_address()
def gen_dni(): return random.randint(10000000, 50000000)
def gen_legajo(): return random.randint(1000, 9999)
def gen_cuit(): return f"{random.randint(20, 33)}-{random.randint(10000000, 99999999)}-{random.randint(0, 9)}"
def gen_razon_social(): return random.choice(razones_sociales)
def gen_sueldo(): return round(random.uniform(1000, 50000), 2)
def gen_horas(): return random.randint(0, 200)
def gen_fecha(): return random_date().strftime("%Y-%m-%d")
def gen_cantidad(): return random.randint(1, 10)
def gen_id(): return random.randint(1, 9999)
def gen_parque(): return random.choice(parques)
def gen_region(): return random.choice(regiones)
def gen_local(): return random.choice(locales)
def gen_oferta(): return random.choice(ofertas)
def gen_zona(): return random.choice(zonas_local)
def gen_capacitacion(): return random.choice(capacitaciones)
def gen_tipo_cliente(): return random.choice(tipos_cliente)

# Mapeo directo
column_generators = {
    "categoria": gen_categoria,
    "cat": gen_categoria,
    "subcat": gen_subcategoria,
    "subcategoria": gen_subcategoria,
    "producto": gen_producto,
    "productos": gen_producto,
    "prod": gen_producto,
    "nombre_producto": gen_producto,
    "telefono_escuela": gen_telefono_escuela,
    "tipo_visita": gen_tipo_visita,
    "tipo_entrada": gen_tipo_entrada,
    "turno": gen_turno,
    "metodo_pago": gen_metodo_pago,
}

# Patrones regex a función
pattern_generators = [
    (r"descripcion", gen_descripcion),
    (r"nombre(?!_producto)", gen_nombre),
    (r"apellido", gen_apellido),
    (r"escuela", gen_escuela),
    (r"tipo_escuela", gen_tipo_escuela),
    (r"localidad", gen_localidad),
    (r"(puesto|cargo)", gen_puesto),
    (r"email", gen_email),
    (r"(telefono|celular)", gen_telefono),
    (r"direccion", gen_direccion),
    (r"dni", gen_dni),
    (r"(legajo|matricula)", gen_legajo),
    (r"cuit", gen_cuit),
    (r"razon_social", gen_razon_social),
    (r"(sueldo|importe|monto|precio|costo)", gen_sueldo),
    (r"horas", gen_horas),
    (r"fecha", gen_fecha),
    (r"cantidad", gen_cantidad),
    (r"id", gen_id),
    (r"parque", gen_parque),
    (r"region", gen_region),
    (r"local(?!idad)", gen_local),
    (r"oferta", gen_oferta),
    (r"zona", gen_zona),
    (r"capacitacion", gen_capacitacion),
    (r"tipo_cliente", gen_tipo_cliente),
]

def generate_value(dtype, col_name=None):
    dtype = dtype.upper()
    if col_name:
        col = col_name.lower()
        if col in column_generators:
            return column_generators[col]()
        for pattern, func in pattern_generators:
            if re.search(pattern, col):
                return func()
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

def generar_tipo_visita_csv(path="output/entradas/tipo_visita.csv", num_tipos=19, descripciones=None, categorias=None):
    import random
    import os
    import pandas as pd

    if descripciones is None:
        descripciones = [
            "Visita escolar", "Visita guiada", "Visita libre", "Visita corporativa",
            "Visita familiar", "Visita especial", "Visita técnica", "Visita de inspección",
            "Visita de capacitación", "Visita institucional", "Visita cultural", "Visita recreativa",
            "Visita científica", "Visita artística", "Visita nocturna", "Visita temática",
            "Visita internacional", "Visita local", "Visita privada"
        ]
    if categorias is None:
        categorias = list(range(1, 20))  # 1 a 19 inclusive
    data = []
    for codigo in range(num_tipos):
        descripcion = descripciones[codigo % len(descripciones)]
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
    import random
    import os
    import pandas as pd

    data = []
    for nro_ticket in range(num_items):
        codigo_tipo_visita = random.randint(0, 18)  # Solo valores de 0 a 18
        cantidad_alumnos_reales = random.randint(1, 10)
        arancel_por_alumno = round(random.uniform(2000, 50000), 2)
        data.append({
            "nro_ticket": nro_ticket,
            "codigo_tipo_visita": codigo_tipo_visita,
            "cantidad_alumnos_reales": cantidad_alumnos_reales,
            "arancel_por_alumno": arancel_por_alumno
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_ventas_csv(path="output/entradas/venta.csv", num_ventas=100):
    import random
    import os
    import pandas as pd

    data = []
    for nro_ticket in range(num_ventas):
        fecha = pd.Timestamp('2024-06-01') + pd.to_timedelta(random.randint(0, 365), unit='D')
        codigo_empleado = random.randint(1, 100)
        codigo_escuela = random.randint(1, 5)  # Ahora solo valores del 1 al 5
        data.append({
            "nro_ticket": nro_ticket,
            "fecha": fecha.date(),
            "codigo_empleado": codigo_empleado,
            "codigo_escuela": codigo_escuela
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
def generar_empleados_entradas_csv(path="output/entradas/empleado.csv", num_empleados=100):
    empleados = []
    for codigo in range(1, num_empleados + 1):
        empleados.append({
            "codigo_empleado": codigo,
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos)
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(empleados)
    df.to_csv(path, index=False)

def generar_empleados_csv(path="output/rrhh/empleado.csv", num_empleados=100):
    empleados = []
    for codigo in range(1, num_empleados + 1):
        empleados.append({
            "id": codigo,
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "direccion": faker.street_address(),
            "sueldo": round(random.uniform(1000, 50000), 2),
            "horas_capacitacion": random.randint(0, 200),
            "fecha_ingreso": (datetime.now() - timedelta(days=random.randint(0, 3650))).strftime("%Y-%m-%d"),
            "id_local": random.choice(locales)
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(empleados)
    df.to_csv(path, index=False)
    return [e["id"] for e in empleados]

def generar_telefonos_empleado_csv(path="output/rrhh/telefono_empleado.csv", legajos=None, telefonos_por_empleado=1):
    if legajos is None:
        raise ValueError("Se requiere la lista de legajos de empleados.")
    data = []
    for legajo in legajos:
        for _ in range(telefonos_por_empleado):
            data.append({
                "legajo": legajo,
                "telefono_empleado": faker.phone_number()
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
    "empleado_entradas": generar_empleados_entradas_csv,
    "empleado": generar_empleados_csv,
    "item_venta": generar_item_venta_csv,
    "telefono_escuela": generar_telefonos_escuela_csv,
    "tipo_visita": generar_tipo_visita_csv,
    "venta": generar_ventas_csv,
}

def generar_tipo_item_venta_csv(path="output/entradas/tipo_item_venta.csv", num_items=100):
    import random
    import os
    import pandas as pd

    data = []
    for codigo in range(num_items):
        descripcion = f"Item {codigo}"
        precio = round(random.uniform(500, 10000), 2)
        codigo_tipo_visita = random.randint(0, 18)  # 0 a 18 para 19 tipos
        data.append({
            "codigo_tipo_item_venta": codigo,
            "descripcion_tipo_item_venta": descripcion,
            "precio": precio,
            "codigo_tipo_visita": codigo_tipo_visita
        })
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)

def generar_csv_especial(tabla, path, num_rows=None):
    key = tabla.lower()
    if key in special_generators:
        if key == "venta" and num_rows is not None:
            special_generators[key](path, num_rows)
        else:
            special_generators[key](path)
        return True
    return False