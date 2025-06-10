import os
from config import SYSTEMS, OUTPUT_FOLDER, NUM_ROWS_PER_TABLE
from utils import ensure_folder
from parser.sql_parser import parse_create_table
from generator.data_generator import generate_table_data

def load_sql_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    ensure_folder(OUTPUT_FOLDER)

    for system_name, sql_path in SYSTEMS.items():
        print(f"Procesando sistema: {system_name}")
        sql_text = load_sql_file(sql_path)
        schema = parse_create_table(sql_text)

        # Crear subcarpeta para el sistema
        system_folder = os.path.join(OUTPUT_FOLDER, system_name)
        ensure_folder(system_folder)

        for table_name, columns in schema.items():
            print(f"  Generando datos para tabla: {table_name}")
            df = generate_table_data(table_name, columns, NUM_ROWS_PER_TABLE)
            output_file = os.path.join(system_folder, f"{table_name}.csv")
            df.to_csv(output_file, index=False)
            print(f"    -> {output_file} generado.")

if __name__ == "__main__":
    main()