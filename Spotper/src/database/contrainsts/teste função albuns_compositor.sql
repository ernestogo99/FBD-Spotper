INSERT INTO compositor (nome, dt_nasc, dt_morte, local_nascimento, cod_pm) VALUES 
('Johann Sebastian Bach', '1685-03-31', '1750-07-28', ROW('Eisenach', 'Alemanha'), NULL),
('Wolfgang Amadeus Mozart', '1756-01-27', '1791-12-05', ROW('Salzburgo', 'Áustria'), NULL),
('Ludwig van Beethoven', '1770-12-17', '1827-03-26', ROW('Bonn', 'Alemanha'), NULL);

INSERT INTO gravadora (nome, sede, home_pg) VALUES 
('Gravadora A', 'São Paulo', 'www.gravadoraA.com'),
('Gravadora B', 'Rio de Janeiro', 'www.gravadoraB.com');


INSERT INTO album (nome, meio, cod_grav, descricao, data_grav, pr_compra, tipo_compra) VALUES 
('Obras de Bach', 'CD', 1, 'Coletânea de obras de Bach', '2021-01-01', 25.00, 'CD'),
('Sinfonias de Mozart', 'VINIL', 3, 'Todas as sinfonias de Mozart', '2021-06-01', 30.00, 'VINIL'),
('Sonatas de Beethoven', 'DOWNLOAD', 1, 'Coletânea de sonatas de Beethoven', '2022-03-01', 20.00, 'DOWNLOAD');

-- Inserir Compositores
INSERT INTO compositor (nome, dt_nasc, dt_morte, local_nascimento, cod_pm) VALUES 
('Johann Sebastian Bach', '1685-03-31', '1750-07-28', ROW('Eisenach', 'Alemanha'), NULL),
('Wolfgang Amadeus Mozart', '1756-01-27', '1791-12-05', ROW('Salzburgo', 'Áustria'), NULL),
('Ludwig van Beethoven', '1770-12-17', '1827-03-26', ROW('Bonn', 'Alemanha'), NULL);

-- Inserir Gravadoras
INSERT INTO gravadora (nome, sede, home_pg) VALUES 
('Gravadora A', 'São Paulo', 'www.gravadoraA.com'),
('Gravadora B', 'Rio de Janeiro', 'www.gravadoraB.com');

-- Inserir Álbuns
INSERT INTO album (nome, meio, cod_grav, descricao, data_grav, pr_compra, tipo_compra) VALUES 
('Obras de Bach', 'CD', 1, 'Coletânea de obras de Bach', '2021-01-01', 25.00, 'CD'),
('Sinfonias de Mozart', 'VINIL', 2, 'Todas as sinfonias de Mozart', '2021-06-01', 30.00, 'VINIL'),
('Sonatas de Beethoven', 'DOWNLOAD', 1, 'Coletânea de sonatas de Beethoven', '2022-03-01', 20.00, 'DOWNLOAD');

select * from composicao

select * from album
-- Inserir Faixas
INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb) VALUES 
('Concerto de Brandeburgo', 1, '00:15:00', 'DDD', 1, 'CD', 36),
('Sinfonia nº 40', 2, '00:27:00', NULL, 2, 'VINIL', 37),
('Sonata ao Luar', 3, '00:14:00', NULL, 2, 'DOWNLOAD', 38);

-- Relacionar Faixas com Compositores
INSERT INTO faixa_compositor (cod_faixa, meio, cod_alb, cod_comp) VALUES 
(123, 'CD', 36, 4), -- Concerto de Brandeburgo é de Bach
(124, 'VINIL', 37, 5), -- Sinfonia nº 40 é de Mozart
(125, 'DOWNLOAD', 38, 6); -- Sonata ao Luar é de Beethoven

select * from compositor

select * from faixa