
CREATE OR REPLACE FUNCTION public.check_barroco_ddd()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
DECLARE
    is_barroco BOOLEAN;
BEGIN
  
    SELECT TRUE INTO is_barroco 
    FROM compositor c
    JOIN periodo_musical pm ON c.cod_pm = pm.cod_pm
    WHERE c.cod_comp = NEW.cod_comp AND pm.descricao = 'barroco';


    IF is_barroco THEN
        IF NEW.tipo_grav != 'DDD' THEN
            RAISE EXCEPTION 'Álbuns com faixas do período barroco devem ter gravação DDD';
        END IF;
    END IF;

    RETURN NEW;
END
$function$



create trigger tg_check_barroco_ddd
before insert or update
on faixa
for each row
execute function check_barroco_ddd();


CREATE OR REPLACE FUNCTION public.check_max_faixas()
 RETURNS trigger
 LANGUAGE plpgsql
AS $function$
DECLARE
    faixa_count INT;
BEGIN

    SELECT COUNT(cod_faixa) INTO faixa_count 
    FROM faixa 
    WHERE cod_alb = NEW.cod_alb;
    
 
    IF faixa_count >= 64 THEN
        RAISE EXCEPTION 'Um álbum não pode ter mais que 64 faixas';
    END IF;

    RETURN NEW;
END;
$function$

create trigger tg_check_max_faixas
before insert or update
on faixa
for each row
execute function check_max_faixas();



CREATE OR REPLACE FUNCTION check_preco_max()
RETURNS TRIGGER AS $$
DECLARE
    media_ddd DECIMAL(10,2);
BEGIN
  
    SELECT AVG(pr_compra)
    INTO media_ddd
    FROM album a
    JOIN faixa f ON a.cod_alb = f.cod_alb
    WHERE f.tipo_grav = 'DDD';


    IF media_ddd IS NULL THEN
        RETURN NEW;
    END IF;

 
    IF media_ddd > 0 AND NEW.pr_compra > 3 * media_ddd THEN
        RAISE EXCEPTION 'O preço de compra do álbum não pode ser superior a três vezes a média dos álbuns com gravação DDD';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


create trigger tg_check_preco_max
before insert or update
on album
for each row
execute function check_preco_max()



CREATE OR REPLACE FUNCTION check_meio_fisico (_cod_alb INT, _meio meio_fisico, _tipo_grav gravacao)
RETURNS BOOLEAN AS $$
DECLARE
    tipo_meio    meio_fisico;
BEGIN
  
    SELECT meio INTO tipo_meio FROM album
    WHERE cod_alb = _cod_alb and meio=_meio;

 
    IF tipo_meio = 'CD' THEN
        IF _tipo_grav NOT IN ('ADD', 'DDD') THEN
            RAISE EXCEPTION 'Para álbuns em CD, o tipo de gravação deve ser ADD ou DDD. Tipo encontrado: %', _tipo_grav;
        END IF;
        RETURN TRUE;
    
  
    ELSIF tipo_meio IN ('VINIL', 'DOWNLOAD') THEN
        IF _tipo_grav IS NOT NULL THEN
            RAISE EXCEPTION 'Para álbuns em Vinil ou Download, o tipo de gravação deve ser NULL. Tipo encontrado: %', _tipo_grav;
        END IF;
        RETURN TRUE;
    
  
    ELSE
        RETURN TRUE;
    END IF;
END
$$ LANGUAGE PLPGSQL;


ALTER TABLE faixa DROP CONSTRAINT IF EXISTS meio_fisico_gravacao;
ALTER TABLE faixa ADD CONSTRAINT meio_fisico_gravacao CHECK (check_meio_fisico(cod_alb, meio, tipo_grav));


