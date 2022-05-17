-- Generado por Oracle SQL Developer Data Modeler 21.4.2.059.0838
--   en:        2022-05-16 01:54:14 CLT
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE cargas_familiares (
    id_carga     VARCHAR2(10) NOT NULL,
    parentesco   VARCHAR2(50) NOT NULL,
    sexo         VARCHAR2(12) NOT NULL,
    personas_rut VARCHAR2(10) NOT NULL
);

ALTER TABLE cargas_familiares ADD CONSTRAINT cargas_familiares_pk PRIMARY KEY ( id_carga );

CREATE TABLE contactos_sos (
    id_contacto  VARCHAR2(10) NOT NULL,
    relacion     VARCHAR2(30) NOT NULL,
    telefono_1   VARCHAR2(15) NOT NULL,
    telefono_2   VARCHAR2(15),
    personas_rut VARCHAR2(10) NOT NULL
);

ALTER TABLE contactos_sos ADD CONSTRAINT contactos_sos_pk PRIMARY KEY ( id_contacto );

CREATE TABLE dep_area (
    id_dep_area  VARCHAR2(10) NOT NULL,
    nombre_depto VARCHAR2(90) NOT NULL,
    nombre_area  VARCHAR2(90) NOT NULL
);

ALTER TABLE dep_area ADD CONSTRAINT dep_area_pk PRIMARY KEY ( id_dep_area );

CREATE TABLE personas (
    rut              VARCHAR2(10) NOT NULL,
    primer_nombre    VARCHAR2(50) NOT NULL,
    segundo_nombre   VARCHAR2(50),
    primer_apellido  VARCHAR2(50) NOT NULL,
    segundo_apellido VARCHAR2(50)
);

ALTER TABLE personas ADD CONSTRAINT personas_pk PRIMARY KEY ( rut );

CREATE TABLE trabajadores (
    id_trabajador              VARCHAR2(10) NOT NULL,
    sexo                       VARCHAR2(10) NOT NULL,
    direccion                  VARCHAR2(150) NOT NULL,
    telefono_trabajador        VARCHAR2(15) NOT NULL,
    cargo                      VARCHAR2(90) NOT NULL,
    us                         VARCHAR2(50) NOT NULL,
    pw                         VARCHAR2(150) NOT NULL,
    estado_actividad           VARCHAR2(20) NOT NULL,
    rol_trabajador             VARCHAR2(45) NOT NULL,
    fecha_nacimiento           DATE NOT NULL,
    fecha_ingreso              DATE NOT NULL,
    fecha_inactividad          DATE,
    personas_rut               VARCHAR2(10) NOT NULL,
    cargas_familiares_id_carga VARCHAR2(10) NOT NULL,
    contactos_sos_id_contacto  VARCHAR2(10) NOT NULL,
    dep_area_id_dep_area       VARCHAR2(10) NOT NULL
);

COMMENT ON COLUMN trabajadores.sexo IS
    '					';

ALTER TABLE trabajadores ADD CONSTRAINT trabajadores_pk PRIMARY KEY ( id_trabajador );

ALTER TABLE cargas_familiares
    ADD CONSTRAINT cargas_familiares_personas_fk FOREIGN KEY ( personas_rut )
        REFERENCES personas ( rut );

ALTER TABLE contactos_sos
    ADD CONSTRAINT contactos_sos_personas_fk FOREIGN KEY ( personas_rut )
        REFERENCES personas ( rut );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE trabajadores
    ADD CONSTRAINT trabajadores_cargas_familiares_fk FOREIGN KEY ( cargas_familiares_id_carga )
        REFERENCES cargas_familiares ( id_carga );

ALTER TABLE trabajadores
    ADD CONSTRAINT trabajadores_contactos_sos_fk FOREIGN KEY ( contactos_sos_id_contacto )
        REFERENCES contactos_sos ( id_contacto );

ALTER TABLE trabajadores
    ADD CONSTRAINT trabajadores_dep_area_fk FOREIGN KEY ( dep_area_id_dep_area )
        REFERENCES dep_area ( id_dep_area );

ALTER TABLE trabajadores
    ADD CONSTRAINT trabajadores_personas_fk FOREIGN KEY ( personas_rut )
        REFERENCES personas ( rut );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             5
-- CREATE INDEX                             0
-- ALTER TABLE                             11
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   1
-- WARNINGS                                 0
