CREATE TABLE Cat (
    cod_cat INT PRIMARY KEY,
    descripcion VARCHAR(50)
);

CREATE TABLE Subcat (
    cod_subcat INT PRIMARY KEY,
    cod_cat INT,
    desc VARCHAR(50),
    FOREIGN KEY (cod_cat) REFERENCES Cat(cod_cat)
);

CREATE TABLE Prod (
    cod_prod INT PRIMARY KEY,
    cod_subcat INT,
    desc VARCHAR(100),
    precio_actual DECIMAL(10,2),
    FOREIGN KEY (cod_subcat) REFERENCES Subcat(cod_subcat)
);

CREATE TABLE Venta (
    nro_ticket INT PRIMARY KEY,
    fecha_venta DATE,
    cod_empleado INT,
    cod_escuela INT
);

CREATE TABLE Item_Venta (
    nro_ticket INT,
    cod_prod INT,
    cantidad INT,
    precio DECIMAL(10,2),
    FOREIGN KEY (nro_ticket) REFERENCES Venta(nro_ticket),
    FOREIGN KEY (cod_prod) REFERENCES Prod(cod_prod)
);

CREATE TABLE Empleado (
    cod_empleado INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

CREATE TABLE Escuela (
    cod_escuela INT PRIMARY KEY,
    nombre VARCHAR(100),
    domicilio VARCHAR(100)
);

CREATE TABLE Telefono_escuela (
    cod_escuela INT,
    tel_escuela VARCHAR(20),
    FOREIGN KEY (cod_escuela) REFERENCES Escuela(cod_escuela)
);
