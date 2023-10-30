create database Client_Cadastro character set utf8mb4 collate utf8mb4_unicode_ci;
use Client_Cadastro;
create table Estado(
id_estado int auto_increment primary key,
estado varchar(30) not null
);

create table Cidade(
id_cidade int auto_increment primary key,
cidade varchar(50) not null
);

create table Sexo(
id_sexo int auto_increment primary key,
sexo varchar(10) not null
);

create table Nacionalidade(
id_nacionalidade int auto_increment primary key,
nacionalidade varchar(30) not null
);

create table Raca(
id_raca int auto_increment primary key,
raca varchar(30) not null
);

create table Escolaridade(
id_escolaridade int auto_increment primary key,
escolaridade varchar(30) not null
);

create table Cadastro_de_Clientes(
CPF int not null,
nome varchar(100) not null,
RG int not null,
id_estado int not null,
constraint foreign key (id_estado) references Estado(id_estado),
id_cidade int not null,
constraint foreign key (id_cidade) references Cidade(id_cidade),
id_sexo int not null,
constraint foreign key (id_sexo) references Sexo(id_sexo),
id_nacionalidade int not null,
constraint foreign key (id_nacionalidade) references Nacionalidade(id_nacionalidade),
fone int not null,
id_raca int not null,
constraint foreign key (id_raca) references Raca(id_raca),
id_escolaridade int not null,
constraint foreign key (id_escolaridade) references Escolaridade(id_escolaridade)
);

insert into Estado(estado) values 
('Acre'),
('Amazonas'),
('Amapá'),
('Roraima'),
('Pará'),
('Maranhão'),
('Rondônia'),
('Tocantins'),
('Piauí'),
('Ceará'),
('Rio Grande do Norte'),
('Paraíba'),
('Pernambuco'),
('Alagoas'),
('Sergipe'),
('Bahia'),
('Goiás'),
('Distrito Federal'),
('Mato Grosso'),
('Mato Grosso do Sul'),
('Minas Gerais'),
('Espirito Santo'),
('Rio de Janeiro'),
('São Paulo'),
('Paraná'),
('Santa Catarina'),
('Rio Grande do Sul');

insert into Cidade(cidade) values
('Rio Branco'),
('Acrelândia'),
('Feijó'),
('Sena Madureira'),
('Taruacá'),
('Manaus'),
('Barcelos'),
('Itacoatiara'),
('Borba'),
('Maués'),
('Macapá'),
('Mazagão'),
('Tartarugalzinho'),
('Porto Grande'),
('Calçoene'),
('Caracaraí'),
('Iracema'),
('Bonfim'),
('Pacaraima'),
('Alto Alegre'),
('Ananindeua'),
('Abaetetuba'),
('Breves'),
('Santarém'),
('Belém'),
('São Luís'),
('Araioses'),
('Açailândia'),
('Bacabal'),
('Codó'),
('Porto Velho'),
('Vilhena'),
('Ariquemes'),
('Buritis'),
('Jaru'),
('Palmas'),
('Araguantins'),
('Arraias'),
('Gurupi'),
('Porto Nacional'),
('Teresina'),
('Oeiras'),
('Picos'),
('Floriano'),
('Pedro II'),
('Fortaleza'),
('Sobral'),
('Quixadá'),
('Juazeiro do Norte'),
('Itapipoca'),
('Natal'),
('Santo Antônio'),
('Mossoró'),
('Macau'),
('Lagoa Nova'),
('João Pessoa'),
('Campina Grande'),
('Patos'),
('Pombal'),
('Santa Rita'),
('Caruaru'),
('Garanhuns'),
('Moreno'),
('Petrolina'),
('Recife'),
('Maceío'),
('Campo Alegre'),
('União dos Palmares'),
('Viçosa'),
('Murici'),
('Aracaju'), 
('Propriá'),
('Lagarto'),
('Neópolis'),
('Areia Branca'),
('Jaquié'),
('Bareiras'),
('Salvador'),
('Porto Seguro'),
('Irecê'),
('Goiânia'),
('Formorsa'),
('Anápolis'),
('Cristalina'),
('Luziânia'),
('Brasília'),
('Taguatinga'),
('Ceilândia'),
('Gama'),
('Sobradinho'),
('Rondonópolis'),
('Várzea Grande'),
('Cuiabá'),
('Sinop'),
('Cáceres'),
('Campo Grande'),
('Três Lagoas'),
('Dourados'),
('Corumbá'),
('Bonito'),
('Belo Horizonte'),
('Uberaba'),
('Ouro Preto'),
('Tiradentes'),
('Juiz de Fora'),
('Vitória'),
('Vila Velha'),
('Guarapari'),
('Aracruz'),
('Serra'),
('Rio de Janeiro'),
('Angra dos Reis'),
('Barra Mansa'),
('Areal'),
('Arraial do Cabo'),
('São Paulo'),
('Praia Grande'),
('Atibaia'),
('Santo André'),
('Embu das Artes'),
('Foz do Iguaçu'),
('Guarapuava'),
('Paranaguá'),
('Cascavel'),
('São José dos Pinhais'),
('Florianópolis'),
('Joinville'),
('Brusque'),
('Balneário Camboriú'),
('Itajaí'),
('Rio Grande'),
('Porto Alegre'),
('Caxias do Sul'),
('Bento Gonçalves'),
('Pelotas');

insert into Sexo(sexo) values
('Feminino'),
('Masculino'),
('Femsculino');

insert into Nacionalidade(nacionalidade) values
('Brasileiro(a)'),
('Estrangeiro(a)');

insert into Raca(raca) values
('Branco'),
('Negro'),
('Asiático'),
('Pardo'),
('Indigena');

insert into Escolaridade(escolaridade) values
('Analfabeto'),
('Fundamental Incompleto'),
('Fundamental Completo'),
('Médio Completo'),
('Médio Incompleto'),
('Superior'),
('Pós-graduação'),
('Mestrado'),
('Doutorado');

insert into Cadastro_de_Clientes(CPF, nome, RG, id_estado, id_cidade, id_sexo, id_nacionalidade,
fone, id_raca, id_escolaridade) values
(766991600, 'Vinicius', 2791078, 1, 1, 2, 1, 15400922, 1, 6),
(644429306, 'Laura', 2436807, 1, 2, 1, 1, 16438933, 3, 7),
(453465391, 'Luan', 1626142, 1, 3, 2, 1, 17448944, 2, 8),
(859043048, 'Paula', 4367245, 1, 4, 1, 1, 18058955, 4, 9),
(448896088, 'Wallace', 1553178, 1, 5, 2, 1, 19068966, 5, 5),
(130055308, 'Bruna', 1038419, 2, 6, 1, 1, 20478977, 1, 4),
(211354002, 'Victor', 3262604, 2, 7, 2, 1, 21488988, 2, 3),
(875757503, 'Sabrina', 4940845, 2, 8, 1, 1, 22498999, 3, 2),
(494304701, 'Murilo', 3153599, 2, 9, 2, 1, 23018911, 2, 1),
(710229605, 'Leticia', 3405463, 2, 10, 1, 1, 24428922, 3, 2),
(824869000, 'Roberto', 2611893, 3, 11, 2, 1, 25408933, 4, 3),
(793878205, 'Maria', 34554732, 3, 12, 1, 1, 26448944, 5, 4),
(745345308, 'Luis', 1076474, 3, 13, 2, 1, 27408955, 1, 5),
(037480301, 'Camila', 3085509, 3, 14, 1, 1, 28408966, 2, 7),
(181622508, 'Mario', 4873250, 3, 15, 2, 1, 29400977, 3, 8),
(641853901, 'Dalva', 1379573, 4, 16, 1, 1, 30400888, 4, 9),
(855251401, 'Severino', 4323703, 4, 17, 2, 1, 31408999, 5, 1),
(263341507, 'Gabriela', 1941135, 4, 18, 1, 1, 32400911, 1, 2),
(392812906, 'Arthur', 3678362, 4, 19, 2, 1, 33400282, 2, 3),
(712863109, 'Cristina', 3767396, 4, 20, 1, 1, 34400389, 3, 4);


#apresentar um select com apenas o nome da cidade 
SELECT cad.nome, cid.cidade FROM Cadastro_de_Clientes cad INNER JOIN Cidade cid ON cad.id_cidade = cid.id_cidade;

#apresentar um select apenas com o nome e o estado
SELECT cad.nome, est.estado FROM Cadastro_de_Clientes cad INNER JOIN Estado est ON cad.id_estado = est.id_estado;

#apresentar um select apenas com o nome, cpf e a raça
SELECT cad.nome, cad.CPF, rac.raca FROM Cadastro_de_Clientes cad INNER JOIN Raca rac ON cad.id_raca = rac.id_raca;

#apresentar um select com apenas o nome e a nacionalidade 
SELECT cad.nome, nac.nacionalidade FROM Cadastro_de_Clientes cad INNER JOIN Nacionalidade nac ON cad.id_nacionalidade = nac.id_nacionalidade;

#apresentar um select com apenas o nome e a escolaridade 
SELECT cad.nome, esc.escolaridade FROM Cadastro_de_Clientes cad INNER JOIN Escolaridade esc ON cad.id_escolaridade = esc.id_escolaridade;

#apresentar um select com apenas o nome, cidade e estado
SELECT cad.nome, cid.cidade, est.estado FROM Cadastro_de_Clientes cad INNER JOIN Cidade cid ON cad.id_cidade = cid.id_cidade INNER JOIN Estado est ON cad.id_estado = est.id_estado;

#apresentar um select com nome, cidade, estado, fone, rg, sexo, nacionalidade, raça e escolaridade
SELECT cad.nome, cid.cidade, est.estado, cad.fone, cad.rg, sex.sexo, nac.nacionalidade, rac.raca, esc.escolaridade FROM Cadastro_de_Clientes cad INNER JOIN Cidade cid ON cad.id_cidade = cid.id_cidade INNER JOIN Estado est ON cad.id_estado = est.id_estado INNER JOIN Sexo sex ON cad.id_sexo = sex.id_sexo INNER JOIN Nacionalidade nac ON cad.id_nacionalidade = nac.id_nacionalidade INNER JOIN Raca rac ON cad.id_raca = rac.id_raca INNER JOIN Escolaridade esc ON cad.id_escolaridade = esc.id_escolaridade;

