
DO $$
DECLARE
    i INT;
BEGIN
  
    FOR i IN 1..64 LOOP
        INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb)
        VALUES ('Faixa ' || i, i, '00:03:00', 'DDD', 1, 'CD', 1);
    END LOOP;


    BEGIN
        INSERT INTO faixa (descricao, num_faixa, t_execucao, tipo_grav, cod_comp, meio, cod_alb)
        VALUES ('Faixa 65', 65, '00:03:00', 'DDD', 1, 'CD', 1);
    EXCEPTION
        WHEN OTHERS THEN
            RAISE NOTICE 'Erro ao inserir: %', SQLERRM;
    END;
END $$;


