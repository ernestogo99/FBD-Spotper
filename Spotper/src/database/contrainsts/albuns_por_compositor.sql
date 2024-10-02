CREATE OR REPLACE FUNCTION buscar_albuns_por_compositor(nome_comp VARCHAR)
RETURNS TABLE(album VARCHAR) AS 
$$
BEGIN	
    RETURN QUERY
    SELECT a.nome AS album 
    FROM album a
    INNER JOIN faixa f USING(cod_alb,meio)
    INNER JOIN faixa_compositor fc USING(cod_faixa, meio, cod_alb)
    INNER JOIN compositor c on c.cod_comp=fc.cod_comp
    WHERE c.nome ILIKE '%' || nome_comp || '%';  
END;
$$ LANGUAGE plpgsql; 

SELECT * FROM buscar_albuns_por_compositor('Johann Sebastian Bach');


