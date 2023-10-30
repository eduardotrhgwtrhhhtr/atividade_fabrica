
drop database Senac;
create database senac CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use senac;
create table alunos (id int auto_increment, name varchar(30) not null, fone varchar(30) not null, email varchar(30) not null, primary key(id));
create table carros (id int auto_increment, name varchar(30) not null, fone varchar(30) not null, email varchar(30) not null, primary key(id));
describe carros;



create database metflix CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use metflix;

create table usuario (
cpf int auto_increment, #auto icrement para o cpf
name varchar(50) not null, 
fone varchar(15) not null, 
email varchar(30) not null, 
senha varchar(30) not null, 
endereço varchar(50),
cartao varchar (30), 
primary key(cpf)
);

create table mensalidade(
mes_ano date, 
valorpago float not null,
data_pagm date not null,
primary key(mes_ano)
);

create table video(
 temporada int,
 epsodio int,
 titulo varchar (50) not null,
 ano date not null,
 duraçao varchar (30)not null,
 produtora varchar(20)not null,
 tipo varchar(20)not null
 );

create table ator(
nome varchar(50),
data_nasc date ,
loc_nasc varchar(50),
primary key(nome)
);

show tables;
drop table ator;

drop table video;

drop table mensalidade;

drop table usuario;


