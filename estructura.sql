-- Crear tabla para el Lunes
CREATE TABLE lunes (
    id SERIAL PRIMARY KEY,
    actividad VARCHAR(255) NOT NULL
);

-- Crear tabla para el Martes
CREATE TABLE martes (
    id SERIAL PRIMARY KEY,
    actividad VARCHAR(255) NOT NULL
);

-- Crear tabla para el Miercoles 
CREATE TABLE miercoles (
    id SERIAL PRIMARY KEY,
    actividad VARCHAR(255) NOT NULL
);

-- Crear tabla para el Jueves (incluye observacion)
CREATE TABLE jueves (
    id SERIAL PRIMARY KEY,
    actividad VARCHAR(255) NOT NULL,
    observacion TEXT
);

-- Datos de ejemplo para verificar el funcionamiento
INSERT INTO lunes (actividad) VALUES ('Estudiar Flask');
INSERT INTO martes (actividad) VALUES ('Realizar una app de recetas');
INSERT INTO miercoles (actividad) VALUES ('Hacer la cuarta tarea de POO');
INSERT INTO jueves (actividad, observacion) VALUES ('Realizar una exposicion', 'Unicamente se permite grupos de 7 personas');

select * from lunes
select * from martes
select * from miercoles
select * from jueves