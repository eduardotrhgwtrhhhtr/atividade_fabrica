
create database estrutura;
use estrutura;
create table EX2_CLIENTE(
codcliente int not null,
nome varchar(50) not null,
datanascimento date not null,
cpf varchar(18),
primary key(cpf)
);

create table EX2_PEDIDO(
codpedido int not null,
codcliente int not null,
datapedido int not null,
nf int not null,
valortotal float not null,
primary key(codpedido)
);

create table EX2_ITEMPEDIDO(
codpedido int not null,
numeroitem int  not null,
valorunitario float not null,
quantidade int not null,
codprotudo int not null,
primary key(numeroitem)
);

create table EX2_PRODUTO(
codproduto int not null, 
descricao varchar(300) not null,
quantidade int not null,
primary key(codproduto)
);

create table EX2_LOG(	
codlog int auto_increment,
data date not null,
descricao varchar(300),
primary key(codlog)
);

create table EX2_REQUISICAO_COMPRA(
codrequisicaocompra int auto_increment,
codproduto int not null,
data date not null,
quantidade int not null,
primary key(codrequisicaocompra)
); 


use estrutura;
insert into EX2_CLIENTE(codcliente, nome, datanascimento,cpf) values (1,"FELIPE", "2000-11-03","00.001.000-000");
INSERT INTO EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(2,'Fernando', '1999-03-01', '001.002.000-00');
insert into EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(3, 'FELIPE', '1988-05-02', '002.002.000-11');
INSERT INTO EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(4, 'RICARDO', '1999-05-04', '003.003.010-55');
INSERT INTO EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(5, 'JUNIOR', '200-03-02', '004.005.010-56');
insert into EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(6, 'KLEBER', '1988-04-03', '006.007.011-55');
insert into EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(7, 'aline', '1987-02-01', '007.008.012-58');
insert into EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(8, 'liza', '1955-02-03','000.005.013-551');
insert into EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(9, 'elise','1956-02-05','000.008.014-58');
insert into EX2_CLIENTE(codcliente, nome, datanascimento, cpf) values(10, 'beca','2011-03-09','011.005.007-96');

ALTER table EX2_PEDIDO ADD constraint FK_pedidoCliente foreign key(codcliente) references EX2_CLIENTE (codcliente);
select * from EX2_CLIENTE;


