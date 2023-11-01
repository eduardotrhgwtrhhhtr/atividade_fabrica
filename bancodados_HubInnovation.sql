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



create table palestra (
id_palestra int auto_increment key,
desc_palestra text(200)not null,
nome_palestra varchar(40)not null,
id_sala int not null ,
id_palestrante int not null,
nome_palestrante varchar(40)not null,
vagas int
);



insert into usuario  (nome,email,fone,cpf,data_nasc,sexo,id_palestra)values
('dieguin','@gmail','999','999','2000-11-01','feminino',1),
('pontes','@gmail','999','999','2000-11-01','mascu',2),
('chris','@gmail','999','999','2000-11-01','mascu',3),
('gleiton','@gmail','999','999','2000-11-01','mascu',4),
('graveto','@gmail','999','999','2000-11-01','mascu',5),
('vinicin','@gmail','999','999','2000-11-01','mascu',6),
('fofinho','@gmail','999','999','2000-11-01','mascu',7)
;


insert into palestra  (desc_palestra,nome_palestra,id_sala,id_palestrante,nome_palestrante,vagas) values
('ssssssss','palestra',1,1,'dieguin',1),
('dddddddd','palestra',2,2,'pontes',2),
('ffffffff','palestra',3,3,'chris',3),
('gggggg','palestra',4,4,'gleiton',4),
('hhhhhhhh','palestra',5,5,'graveto',5),
('jjjjjjjjjjj','palestra',6,6,'vinicin',6),
('kkkkkkkkkkk','palestra',7,7,'fofinho',7)
;

describe usuario;
describe palestra;
select * from palestra;
select * from usuario;