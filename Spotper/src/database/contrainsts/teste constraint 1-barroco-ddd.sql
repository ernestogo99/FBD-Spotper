INSERT INTO periodo_musical (descricao, interv_tempo) VALUES ('barroco', '["1600-01-01", "1750-12-31"]');

INSERT INTO compositor (nome, dt_nasc, cod_pm) VALUES ('Compositor Barroco', '1685-03-31', 1);

INSERT INTO gravadora (nome, sede, home_pg) VALUES ('Gravadora Exemplo', 'Cidade', 'www.exemplo.com');

INSERT INTO album (meio, cod_grav, data_grav, pr_compra, tipo_compra) 
VALUES ('CD', 1, '2021-01-01', 30.00, 'CD');

INSERT INTO album (meio, cod_grav, data_grav, pr_compra, tipo_compra) 
VALUES ('VINIL', 1, '2021-01-01', 30.00, 'VINIL');



INSERT INTO composicao (descricao, tipo) VALUES ('Composição Barroca', 'tipo_exemplo');


INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Faixa Barroca', 1, '00:03:00', 'DDD', 1, 'CD', 1);


INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Outra Faixa Barroca', 2, '00:02:30', 'ADD', 1, 'CD', 1);


INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Outra Faixa Barroca', 3, '00:03:30', 'tetste', 1, 'CD', 1);




