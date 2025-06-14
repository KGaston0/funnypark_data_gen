import os
from config import SYSTEMS, OUTPUT_FOLDER, NUM_ROWS_PER_TABLE
from utils import ensure_folder
from parser.sql_parser import parse_create_table
from generator.data_generator import (
    generate_table_data,
    generar_escuelas_csv,
    generar_categorias_csv,
    generar_empleados_csv,
    generar_empleados_rrhh_csv,  # Importa la función para rrhh
    generar_item_venta_csv,
    generar_telefonos_escuela_csv,
    generar_tipo_visita_csv,
    generar_ventas_csv,
    generar_telefonos_empleado_csv,
    generar_subcategoria_csv,
    generar_producto_csv
)

def load_sql_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

special_generators = {
    "escuela": (generar_escuelas_csv, "especial escuelas"),
    "categoria": (generar_categorias_csv, "especial categorias"),
    "empleado": (None, "especial empleados"),  # Se decide en el main
    "item_venta": (generar_item_venta_csv, "especial item_venta"),
    "telefono_escuela": (generar_telefonos_escuela_csv, "especial telefono_escuela"),
    "tipo_visita": (generar_tipo_visita_csv, "especial tipo_visita"),
    "venta": (generar_ventas_csv, "especial venta"),
    "subcategoria": (generar_subcategoria_csv, "especial subcategoria"),
    "producto": (generar_producto_csv, "especial producto")
}

def main():
    ensure_folder(OUTPUT_FOLDER)

    for system_name, sql_path in SYSTEMS.items():
        print(f"Procesando sistema: {system_name}")
        sql_text = load_sql_file(sql_path)
        schema = parse_create_table(sql_text)

        system_folder = os.path.join(OUTPUT_FOLDER, system_name)
        ensure_folder(system_folder)

        for table_name, columns in schema.items():
            print(f"  Generando datos para tabla: {table_name}")
            output_file = os.path.join(system_folder, f"{table_name}.csv")
            key = table_name.lower()
            if key in special_generators:
                func, desc = special_generators[key]
                if key == "venta":
                    func(output_file, NUM_ROWS_PER_TABLE)
                elif key == "empleado":
                    # Selecciona la función según el sistema
                    if system_name == "rrhh":
                        legajos = generar_empleados_rrhh_csv(output_file)
                    else:
                        legajos = generar_empleados_csv(output_file)
                    generar_telefonos_empleado_csv(
                        os.path.join(system_folder, "telefono_empleado.csv"),
                        legajos,
                        telefonos_por_empleado=2
                    )
                elif key == "producto":
                    func(output_file, NUM_ROWS_PER_TABLE)
                else:
                    func(output_file)
                print(f"    -> {output_file} generado ({desc}).")
            else:
                df = generate_table_data(table_name, columns, NUM_ROWS_PER_TABLE)
                df.to_csv(output_file, index=False)
                print(f"    -> {output_file} generado.")

if __name__ == "__main__":
    main()