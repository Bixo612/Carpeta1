--crear tabla cargos
CREATE TABLE `rrhh`.`cargos` ( 
    `id_cargo` INT NOT NULL , 
    `nombre_cargo` VARCHAR(50) NOT NULL 
    , PRIMARY KEY (`id_cargo`)) ENGINE = InnoDB;
--Crear tabla areas
CREATE TABLE `rrhh`.`areas` ( 
    `id_area` INT NOT NULL , 
    `nombre_area` VARCHAR(50) NOT NULL ,
    PRIMARY KEY (`id_area`)) ENGINE = InnoDB;
--crear tabla departamentos
CREATE TABLE `rrhh`.`departamentos` ( `id_departamento` INT NOT NULL , `nombre_departamento` VARCHAR(50) NOT NULL , PRIMARY KEY (`id_departamento`)) ENGINE = InnoDB;
--crear tabla trabajadores
CREATE TABLE `rrhh`.`trabajadores` ( 
    `rut_trabajador` VARCHAR(10) NOT NULL , 
    `primer_nombre` VARCHAR(50) NOT NULL , 
    `segundo_nombre` VARCHAR(50) NULL , 
    `primer_apellido` VARCHAR(50) NOT NULL , 
    `segundo_apellido` VARCHAR(50) NULL , 
    `fecha_nacimiento` DATE NOT NULL , 
    `fecha_ingreso` DATE NOT NULL , 
    `sexo` VARCHAR(1)  NOT NULL , 
    `estado` BOOLEAN NOT NULL ,
    `clave` VARCHAR(200) NOT NULL,
    PRIMARY KEY (`rut_trabajador`)) ENGINE = InnoDB;
--agregar columnas de tablas primaras
ALTER TABLE `trabajadores` 
    ADD `id_cargo` INT NOT NULL AFTER `estado`, 
    ADD `id_area` INT NOT NULL AFTER `id_cargo`, 
    ADD `id_departamento` INT NOT NULL AFTER `id_area`;
--agragar relaciones de datos laborales
ALTER TABLE `trabajadores` ADD FOREIGN KEY (`id_area`) REFERENCES `areas`(`id_area`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `trabajadores` ADD FOREIGN KEY (`id_cargo`) REFERENCES `cargos`(`id_cargo`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `trabajadores` ADD FOREIGN KEY (`id_departamento`) REFERENCES `departamentos`(`id_departamento`) ON DELETE RESTRICT ON UPDATE RESTRICT;
--crear tabla cargas
CREATE TABLE `rrhh`. ( 
    `rut_carga` VARCHAR(10) NOT NULL , 
    `primer_nombre` VARCHAR(50) NOT NULL , 
    `segundo_nombre` VARCHAR(50) NOT NULL , 
    `primer_apellido` VARCHAR(50) NOT NULL , 
    `segundo_apellido` VARCHAR(50) NOT NULL , 
    `fecha_nacimiento_carga` DATE NOT NULL , 
    `relacion` VARCHAR(20) NOT NULL , 
    `rut_trabajador` VARCHAR(10) NOT NULL 
    , PRIMARY KEY (`rut_carga`)) ENGINE = InnoDB;
--agregar relacion
ALTER TABLE `cargas` ADD FOREIGN KEY (`rut_trabajador`) REFERENCES `trabajadores`(`rut_trabajador`) ON DELETE RESTRICT ON UPDATE RESTRICT;
--crear tabla contactos
CREATE TABLE `rrhh`.`contactos_emergencia` ( 
    `nombre` VARCHAR(100) NOT NULL , 
    `relacion` VARCHAR(50) NULL , 
    `numero1` VARCHAR(25) NOT NULL , 
    `numero2` TEXT NULL , 
    `rut_trabajador` VARCHAR(10) NOT NULL ) ENGINE = InnoDB;
--agregar relacion
ALTER TABLE `contactos_emergencia` ADD FOREIGN KEY (`rut_trabajador`) REFERENCES `trabajadores`(`rut_trabajador`) ON DELETE RESTRICT ON UPDATE RESTRICT;