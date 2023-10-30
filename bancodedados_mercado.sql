create database mercado;
set sql_safe_updates=0;


use mercado;

create table produtos (
referencia varchar(3) primary key,
descricao varchar(50) unique,
estoque int not null default 0);

insert into produtos values ('001',
'feijão',10);
insert into produtos values ('002',
'arroz',5);
insert into produtos values ('003',
'farinha',15);

create table itensvenda(
Venda int,
produto varchar(3),
quantidade int);

insert into itensvenda values(1,
'001',3);
insert into itensvenda values (1,
'002',1);
insert into itensvenda values (1,
'003',5);

insert into itensvenda values (1,
'003',5);

#delimiter ++
#select * from itensvenda ++
#delimiter ;
/*delimiter $
create trigger Trg_itensvenda_insert after insert
on itensvenda 
for each row
begin
update produtos set estoque = estoque -new.quantidade
where referencia = new.produto;
end$

 

create trigger Trg_itensvenda_delete after delete
on itensvenda 
for each row
begin
update produtos set estoque = estoque +old.quantidade
where referencia = old.produto;
end$

-- drop trigger Tgr_itensvenda_delete;
 */
delete from itensvenda where produto=002;
show triggers;

select * from produtos;

select * from itensvenda;

delete from itensvenda where produto=001;


drop trigger Trg_itensvenda_delete;
show triggers;


