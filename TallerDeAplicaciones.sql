
CREATE TABLE `rrhh`.`personas` (
    `rut`               VARCHAR(10) NOT NULL ,
    `primer_nombre`     VARCHAR(50) NOT NULL , 
    `segundo_nombre`    VARCHAR(50) NULL , 
    `primer_apellido`   VARCHAR(50) NOT NULL , 
    `segundo_apellido`  VARCHAR(50) NULL , 
    `fecha_nacimiento`  DATE NOT NULL ,
    `sexo`              VARCHAR(1)  NOT NULL ,
    PRIMARY KEY (`rut`)
) ENGINE = InnoDB;

CREATE TABLE `rrhh`.`cargos` ( 
    `id_cargo`      INT NOT NULL , 
    `nombre_cargo`  VARCHAR(50) NOT NULL , 
    PRIMARY KEY (`id_cargo`)
) ENGINE = InnoDB;

CREATE TABLE `rrhh`.`laborales` ( 
    `id_laborales`      INT NOT NULL , 
    `area`              VARCHAR(50) NOT NULL ,
    `departamento`      VARCHAR(50) NOT NULL ,
    PRIMARY KEY (`id_laborales`)
) ENGINE = InnoDB;

CREATE TABLE `rrhh`.`trabajadores` (
    `rut`               VARCHAR(10) NOT NULL ,
    `id_trabajador`     INT NOT NULL ,
    `estado`            VARCHAR(10) NOT NULL ,
    `telefono`          VARCHAR(15) ,
    `direccion`         VARCHAR(100) NOT NULL ,
    `rol`               VARCHAR(15) NOT NULL ,
    `clave`             VARCHAR(100) NOT NULL ,
    `fecha_ingreso`     DATE NOT NULL ,
    `fecha_inactividad` DATE NOT NULL ,
    `id_laborales`      INT NOT NULL ,
    `id_cargo`          INT NOT NULL  ,
    PRIMARY KEY (`id_trabajador`)
) ENGINE = InnoDB;

ALTER TABLE `trabajadores` ADD FOREIGN KEY (`rut`)          REFERENCES `personas`(`rut`)            ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `trabajadores` ADD FOREIGN KEY (`id_laborales`) REFERENCES `laborales`(`id_laborales`)  ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `trabajadores` ADD FOREIGN KEY (`id_cargo`)     REFERENCES `cargos`(`id_cargo`)         ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE `rrhh`.`cargas` (
    `rut`           VARCHAR(10) NOT NULL ,
    `id_trabajador` INT NOT NULL ,
    `relacion`      VARCHAR(15) NOT NULL    
) ENGINE = InnoDB;

ALTER TABLE `cargas` ADD FOREIGN KEY (`rut`)            REFERENCES `personas`(`rut`)                ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `cargas` ADD FOREIGN KEY (`id_trabajador`)  REFERENCES `trabajadores`(`id_trabajador`)  ON DELETE RESTRICT ON UPDATE RESTRICT;

CREATE TABLE `rrhh`.`contactos` ( 
    `nombre`    VARCHAR(100) NOT NULL , 
    `relacion`  VARCHAR(15) NULL , 
    `numero1`   VARCHAR(15) NOT NULL , 
    `numero2`   VARCHAR(15) NULL , 
    `id_trabajador` INT NOT NULL
) ENGINE = InnoDB;

ALTER TABLE `contactos` ADD FOREIGN KEY (`id_trabajador`)  REFERENCES `trabajadores`(`id_trabajador`)  ON DELETE RESTRICT ON UPDATE RESTRICT;