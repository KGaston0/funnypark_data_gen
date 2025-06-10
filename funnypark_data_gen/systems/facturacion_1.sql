CREATE TABLE Categoria (
    id_categoria INT PRIMARY KEY,
    descripcion VARCHAR(50)
);

CREATE TABLE Subcategoria (
    id_subcategoria INT PRIMARY KEY,
    id_categoria INT,
    descripcion VARCHAR(50),
    FOREIGN KEY (id_categoria) REFERENCES Categoria(id_categoria)
);

CREATE TABLE Producto (
    id_producto INT PRIMARY KEY,
    id_subcategoria INT,
    descripcion VARCHAR(100),
    precio_actual DECIMAL(10,2),
    FOREIGN KEY (id_subcategoria) REFERENCES Subcategoria(id_subcategoria)
);

CREATE TABLE Venta (
    numero_ticket INT PRIMARY KEY,
    fecha_venta DATE,
    id_empleado INT,
    id_escuela INT
);

CREATE TABLE Item_venta (
    numero_ticket INT,
    id_producto INT,
    cantidad INT,
    precio DECIMAL(10,2),
    FOREIGN KEY (numero_ticket) REFERENCES Venta(numero_ticket),
    FOREIGN KEY (id_producto) REFERENCES Producto(id_producto)
);

CREATE TABLE Empleado (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

CREATE TABLE Escuela (
    id_escuela INT PRIMARY KEY,
    nombre VARCHAR(100),
    domicilio VARCHAR(100)
);

CREATE TABLE Telefono_escuela (
    id_escuela INT,
    telefono_escuela VARCHAR(20),
    FOREIGN KEY (id_escuela) REFERENCES Escuela(id_escuela)
);
