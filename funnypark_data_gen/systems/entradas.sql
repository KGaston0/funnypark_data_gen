CREATE TABLE Venta (
    nro_ticket INT PRIMARY KEY,
    fecha DATE,
    codigo_empleado INT,
    codigo_escuela INT
);

CREATE TABLE Empleado (
    codigo_empleado INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

CREATE TABLE Escuela (
    codigo_escuela INT PRIMARY KEY,
    nombre_escuela VARCHAR(100),
    direccion_escuela VARCHAR(100)
);

CREATE TABLE Telefono_escuela (
    codigo_escuela INT,
    telefono_escuela VARCHAR(20),
    FOREIGN KEY (codigo_escuela) REFERENCES Escuela(codigo_escuela)
);

CREATE TABLE Item_venta (
    nro_ticket INT,
    codigo_tipo_visita INT,
    cantidad_alumnos_reales INT,
    arancel_por_alumno DECIMAL(10,2),
    FOREIGN KEY (nro_ticket) REFERENCES Venta(nro_ticket)
);

CREATE TABLE Tipo_visita (
    codigo_tipo_visita INT PRIMARY KEY,
    descripcion_tipo_visita VARCHAR(100),
    arancel_por_alumno DECIMAL(10,2),
    codigo_categoria INT
);

CREATE TABLE Categoria (
    codigo_categoria INT PRIMARY KEY,
    descripcion_categoria VARCHAR(50)
);
