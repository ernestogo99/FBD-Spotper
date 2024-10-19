-- Inserindo período musical
INSERT INTO periodo_musical (descricao, interv_tempo) 
VALUES ('barroco', '["1600-01-01", "1750-12-31"]');

-- Inserindo compositor associado ao período barroco
INSERT INTO compositor (nome, dt_nasc, cod_pm) 
VALUES ('Compositor Barroco', '1685-03-31', 1);

-- Inserindo gravadora
INSERT INTO gravadora (nome, sede, home_pg) 
VALUES ('Gravadora Exemplo', 'Cidade', 'www.exemplo.com');

-- Inserindo álbum (meio físico CD)
INSERT INTO album (meio, cod_grav, data_grav, pr_compra, tipo_compra) 
VALUES ('CD', 1, '2021-01-01', 30.00, 'CD');

-- Inserindo álbum (meio físico vinil)
INSERT INTO album (meio, cod_grav, data_grav, pr_compra, tipo_compra) 
VALUES ('VINIL', 1, '2021-01-01', 20.00, 'VINIL');



-- Inserindo álbum (meio físico download)
INSERT INTO album (meio, cod_grav, data_grav, pr_compra, tipo_compra) 
VALUES ('DOWNLOAD', 1, '2021-01-01', 10.00, 'DOWNLOAD');

SELECT * FROM album
-- Inserindo composição associada ao período barroco
INSERT INTO composicao (descricao, tipo) 
VALUES ('Composição Barroca', 'Sinfonia');

-- Inserindo faixas válidas para CD
-- Faixa 1 (gravação válida DDD)
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Faixa Barroca', 1, '00:03:00', 'DDD', 1, 'CD', 27);

select * from faixa

-- Faixa 2 (gravação válida ADD)
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Outra Faixa Barroca', 2, '00:02:30', 'DDD', 1, 'CD', 27);

-- Testando inserção inválida: tipo de gravação "AAA" (não permitido para CDs)
-- Deve falhar por causa da restrição de gravação inválida para CDs
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Outra Faixa Barroca', 3, '00:03:30', 'AAA', 1, 'CD', 1);

SELECT * FROM faixa
-- Testando inserção inválida: gravação não DDD para composição barroca
-- Deve falhar por causa da restrição do período barroco
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Outra Faixa Barroca', 4, '00:02:45', 'ADD', 1, 'CD', 1);

-- Inserindo faixa válida para vinil (sem gravação)
-- Deve passar, pois vinil não tem valor para tipo_grav
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Faixa Vinil Barroca', 1, '00:03:00', NULL, 1, 'VINIL', 28);

-- Testando inserção inválida para vinil (com gravação)
-- Deve falhar porque vinil não permite tipo_grav
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Faixa Inválida Vinil', 2, '00:03:00', 'DDD', 1, 'VINIL', 28);

-- Inserindo faixa válida para download (sem gravação)
-- Deve passar, pois download não tem valor para tipo_grav
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Faixa Download Barroca', 1, '00:03:00', NULL, 1, 'DOWNLOAD', 29);

-- Testando inserção inválida para download (com gravação)
-- Deve falhar porque download não permite tipo_grav
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) 
VALUES ('Faixa Inválida Download', 2, '00:03:00', 'DDD', 1, 'DOWNLOAD', 29);
