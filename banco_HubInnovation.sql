create database HubInnovation;
use HubInnovation;

create table usuario(
id_usuario int auto_increment primary key,
nome varchar(30) not null,
email varchar(30) not null,
fone varchar(18)not null,
cpf varchar(20) not null,
data_nasc date not null,
sexo varchar (10) not null,
id_palestra int not null,
constraint foreign key (id_palestra) references palestra(id_palestra)
);

describe usuario;
alter table usuario modify column data_nasc varchar(30);
drop table palestra;
drop database HubInnovation;

create table palestra (
id_palestra int auto_increment key,
desc_palestra text(200)not null,
nome_palestra varchar(40)not null,
id_sala int not null ,
id_palestrante int not null,
nome_palestrante varchar(40)not null,
vagas int
);

describe usuario;

insert into usuario  (nome,email,fone,cpf,data_nasc,sexo,id_palestra)values
('dieguin','@gmail','999','999','2000-11-01','mascu',1),
('dieguin','@gmail','999','999','2000-11-01','mascu',1),
('dieguin','@gmail','999','999','2000-11-01','mascu',1),
('dieguin','@gmail','999','999','2000-11-01','mascu',1),
('dieguin','@gmail','999','999','2000-11-01','mascu',1),
('dieguin','@gmail','999','999','2000-11-01','mascu',1),
('dieguin','@gmail','999','999','2000-11-01','mascu',1)
;
select * from palestra;
select * from usuario;
insert into palestra  (desc_palestra,nome_palestra,id_sala,id_palestrante,nome_palestrante,vagas) values
('fjjhg','palestra',1,1,'dieguin',1),
('fjjhg','palestra',1,1,'dieguin',1),
('fjjhg','palestra',1,1,'dieguin',1),
('fjjhg','palestra',1,1,'dieguin',1),
('fjjhg','palestra',1,1,'dieguin',1),
('fjjhg','palestra',1,1,'dieguin',1),
('fjjhg','palestra',1,1,'dieguin',1)
;