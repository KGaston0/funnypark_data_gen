import re
from utils import clean_name

def parse_create_table(sql_text):
    tables = {}
    current_table = None
    for line in sql_text.splitlines():
        line = line.strip()
        if line.upper().startswith("CREATE TABLE"):
            current_table = re.findall(r'CREATE TABLE\s+(\w+)', line, re.IGNORECASE)[0]
            current_table = clean_name(current_table)
            tables[current_table] = []
        elif current_table and line and not line.upper().startswith("PRIMARY") and not line.upper().startswith("FOREIGN"):
            parts = line.split()
            if len(parts) >= 2:
                column = clean_name(parts[0])
                dtype = parts[1].upper().split("(")[0]
                tables[current_table].append((column, dtype))
        elif line == ");":
            current_table = None
    return tables