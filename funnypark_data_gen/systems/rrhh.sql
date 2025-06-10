CREATE TABLE Empleado (
    legajo INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    direccion VARCHAR(100),
    sueldo DECIMAL(10,2),
    horas_capacitacion INT,
    fecha_ingreso DATE,
    id_local INT
);

CREATE TABLE Telefono_empleado (
    legajo INT,
    telefono_empleado VARCHAR(20),
    FOREIGN KEY (legajo) REFERENCES Empleado(legajo)
);
