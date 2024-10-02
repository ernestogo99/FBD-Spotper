CREATE MATERIALIZED VIEW album_playlist AS
SELECT 
    p.nome AS playlist,
    COUNT(DISTINCT fp.cod_alb) AS qtd_albuns
FROM 
    playlist p
INNER JOIN faixa_playlist fp ON fp.cod_play = p.cod_play
GROUP BY p.cod_play, p.nome
ORDER BY qtd_albuns DESC;



REFRESH MATERIALIZED VIEW album_playlist;

select * from album_playlist



