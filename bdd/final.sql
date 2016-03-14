PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "SINTOMATOLOGIA" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "RUN" TEXT,
    "FECHA" DATE,
    "SINTOMAVOCAL1" INTEGER,
    "DESCRSINTOMA1" TEXT,
    "SINTOMAVOCAL2" INTEGER,
    "DESCRSINTOMA2" TEXT,
    "SINTOMAVOCAL3" INTEGER,
    "DESCRSINTOMA3" TEXT,
    "SINTOMAVOCAL4" INTEGER,
    "DESCRSINTOMA4" TEXT,
    "OSINTOMA1" INTEGER,
    "DESCROSINTOMA1" TEXT,
    "OSINTOMA2" INTEGER,
    "DESCROSINTOMA2" TEXT,
    "OSINTOMA3" INTEGER,
    "DESCROSINTOMA3" TEXT,
    "OSINTOMA4" INTEGER,
    "DESCROSINTOMA4" TEXT,
    "ANTMEDICOS" TEXT,
    "MEDICAMENTOS" TEXT,
    "CABUSOVOCAL1" INTEGER,
    "DETALLECONDUCTA1" TEXT,
    "CABUSOVOCAL2" INTEGER,
    "DETALLECONDUCTA2" TEXT,
    "CABUSOVOCAL3" INTEGER,
    "DETALLECONDUCTA3" TEXT,
    "CABUSOVOCAL4" INTEGER,
    "DETALLECONDUCTA4" TEXT,
    "HHDUERME" INTEGER
);
CREATE TABLE "paciente" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "RUN" TEXT,
    "NOMBRE" TEXT,
    "APELLIDO" TEXT,
    "FNACIMIENTO" DATE,
    "OCUPACION" TEXT,
    "HHOCUPACION" INTEGER,
    "OEXTRA" TEXT,
    "HHOEXTRA" INTEGER,
    "CODAREA" INTEGER,
    "FONO" INTEGER,
    "EMAIL" TEXT,
    "MOTIVO" TEXT
);
INSERT INTO "paciente" VALUES(1,'123','dfa','sdasdf','01-01-2000','safsdf',0,'asdfasdf',0,123,123123,'ASD','dASDAS');
INSERT INTO "paciente" VALUES(2,'16.514.499-6','Miguel','Chandia','07-04-1987','Estrella de rock',5,'Ninguna',0,9,81224811,'miguelchandia@gmail.com','Dolor de garganta con cuatica.');
INSERT INTO "paciente" VALUES(3,'11.111.111-1','Wladito','Soto','08-12-1980','Trolo',8,'Blowjob',8,9,7766554433,'wladito@trolaso.com.ar','Potito Roto');
CREATE TABLE "EVALUACION" (
    "ID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "RUT" TEXT,
    "FECHA" DATE,
    "VHIFUN" INTEGER,
    "VHIFIS" INTEGER,
    "VHIEMO" INTEGER,
    "VHITOT" INTEGER,
    "TRREPOSO" INTEGER,
    "TRFONACION" INTEGER,
    "MRREPOSO" INTEGER,
    "MRFONACION" INTEGER,
    "CORDFONORESP" INTEGER,
    "NINSPIRACIONES" INTEGER,
    "TMAXFONACION" INTEGER,
    "TMAXESPIRACION" INTEGER,
    "INDICESA" INTEGER,
    "APOYORESP" INTEGER,
    "POSPF1" INTEGER,
    "POSPF2" INTEGER,
    "POSPF3" INTEGER,
    "POSPL1" INTEGER,
    "POSPL2" INTEGER,
    "POSPL3" INTEGER,
    "POSPP1" INTEGER,
    "POSPP2" INTEGER,
    "POSPP3" INTEGER,
    "POSOBS" TEXT,
    "TONICGRAL" INTEGER,
    "TONICINFR" INTEGER,
    "TONICSUPR" INTEGER,
    "TONICERV" INTEGER,
    "TONICESCA" INTEGER,
    "TONICALTU" INTEGER,
    "HIPERPHA" INTEGER,
    "HIPEREDC" INTEGER,
    "HIPERPDP" INTEGER,
    "HIPERDEE" INTEGER,
    "HIPERREH" INTEGER,
    "HIPERPT" INTEGER,
    "RASATIRON" INTEGER,
    "RASATIASP" INTEGER,
    "RASATISOP" INTEGER,
    "RASATIAST" INTEGER,
    "RASATITEN" INTEGER,
    "RASATIINE" INTEGER,
    "TMH" INTEGER,
    "PAJITTER" REAL,
    "PASHIMMER" REAL,
    "PANHR" INTEGER,
    "VOZCFF" INTEGER,
    "VOZCRF" INTEGER,
    "VOZCRTET" INTEGER,
    "VOZCTESI" INTEGER,
    "VOZCTIPO" INTEGER,
    "VOZCCVH" INTEGER,
    "VOZCCVM" INTEGER
);
ANALYZE sqlite_master;
INSERT INTO "sqlite_stat1" VALUES('paciente',NULL,'3');
DELETE FROM sqlite_sequence;
INSERT INTO "sqlite_sequence" VALUES('paciente',3);
COMMIT;
