create table interprete(
	cod_inter serial primary key,
	nome varchar(255) not null,
	tipo varchar(255) not null
)TABLESPACE ts_tertiary



create table composicao(
	cod_comp serial primary key,
	descricao TEXT default '',
	tipo varchar(255) not null
)TABLESPACE ts_tertiary

create table gravadora(
	cod_grav serial primary key,
	nome varchar(255) not null,
	sede varchar(255) not null,
	home_pg varchar(255) not null
)TABLESPACE ts_tertiary


create table telefone_gravadora(
	cod_grav integer,
	numero char(15),
	primary key(cod_grav,numero),
	foreign key(cod_grav)
	references gravadora(cod_grav)
	on delete cascade
)TABLESPACE ts_tertiary




CREATE TYPE meio_fisico AS ENUM ('CD', 'VINIL', 'DOWNLOAD');

create table album(
	cod_alb serial,
	nome varchar(255),
	meio meio_fisico,
	cod_grav integer,
	descricao text default '',
	data_grav DATE not null check(data_grav> '2000-01-01'),
	pr_compra NUMERIC(10,2),
	tipo_compra meio_fisico,
	primary key(cod_alb,meio),
	foreign key(cod_grav)
	references gravadora(cod_grav)
	on delete set null
	
)TABLESPACE ts_tertiary



	
CREATE TYPE gravacao AS ENUM ( 'ADD', 'DDD' );
	
create table faixa(
	cod_faixa serial,
	descricao TEXT default '',
	num_faixa integer,
	t_execucao TIME not null,
	tipo_grav gravacao,
	cod_comp int not null,
	meio meio_fisico,
	cod_alb integer,
	primary key(cod_faixa,cod_alb,meio),
	foreign key(cod_comp)
	references composicao(cod_comp)
	on delete cascade,
	foreign key(cod_alb,meio)
	references album(cod_alb,meio)
	on delete cascade 
)TABLESPACE ts_secondary


create table faixa_interprete(
	cod_faixa integer,
	cod_alb integer,
	meio meio_fisico,
	cod_inter integer,

	primary key(cod_faixa,cod_alb,meio,cod_inter),
	foreign key(cod_inter)
	references interprete(cod_inter),
	foreign key(cod_faixa,cod_alb,meio)
	references faixa(cod_faixa,cod_alb,meio)
	
)TABLESPACE ts_tertiary;


create table playlist(
	cod_play serial primary key,
	nome varchar(255),
	dt_criacao date default current_date,
	t_exec TIME DEFAULT '00:00:00'
)TABLESPACE ts_secondary


create table faixa_playlist(
	cod_play integer,
	cod_faixa integer,
	meio meio_fisico,
	cod_alb integer,
	dt_ultima_reproducao date,
	qtd_reproducoes int default 0,

	primary key(cod_play,cod_faixa,meio,cod_alb),
	foreign key(cod_play)
	references playlist(cod_play),
	foreign key(cod_faixa,meio,cod_alb)
	references faixa(cod_faixa,meio,cod_alb)
	on delete cascade
)TABLESPACE ts_secondary;


create type periodo as enum('idade média','renascença','barroco','clássico','romântico','moderno');

create table periodo_musical(
	cod_pm serial primary key,
	descricao periodo,
	interv_tempo TSRANGE not null
)TABLESPACE ts_tertiary;


create type local_nascimento AS(
	cidade varchar(255),
	pais varchar(255)
);

create table compositor(
	cod_comp serial primary key,
	nome varchar(255),
	dt_nasc date not null,
	dt_morte date,
	local_nascimento local_nascimento,

	cod_pm integer,
	foreign key(cod_pm)
	references periodo_musical(cod_pm)
	on delete no action
)TABLESPACE ts_tertiary;

create table faixa_compositor(
	cod_faixa integer,
	meio meio_fisico,
	cod_alb integer,

	cod_comp integer,

	primary key(cod_faixa,meio,cod_alb,cod_comp),
	foreign key(cod_comp)
	references compositor(cod_comp),
	foreign key(cod_faixa,meio,cod_alb)
	references faixa(cod_faixa,meio,cod_alb)
	on delete cascade
)TABLESPACE ts_tertiary;


