CREATE OR REPLACE FUNCTION generate_player_performance_report()
RETURNS TABLE (
    jogador_id INT,
    nome VARCHAR,
    apelido VARCHAR,
    trofeus_ganhos BIGINT,
    escalaoes_ativas BIGINT,
    time_atual TEXT,
    times TEXT
) AS $$
BEGIN
    RETURN QUERY
    WITH PlayerPerformance AS (
        SELECT
            j.id AS jogador_id,
            j.name AS nome,
            j.apelido AS apelido,
            COUNT(DISTINCT t.evento_id) AS trofeus_ganhos,
            COUNT(DISTINCT e.id) AS escalaoes_ativas,
            STRING_AGG(DISTINCT t_atual.name, ', ') AS time_atual,
            STRING_AGG(DISTINCT time.name, ', ') AS times
        FROM
            jogador j
        LEFT JOIN escalacao_jogador ej ON j.id = ej.jogador_id
        LEFT JOIN escalacao e ON ej.escalacao_id = e.id AND e.ativo = true
        LEFT JOIN escalacao es ON ej.escalacao_id = es.id
        LEFT JOIN time t_atual ON e.time_id = t_atual.id
        LEFT JOIN time  ON es.time_id = time.id
        LEFT JOIN time_partida tp ON time.id = tp.time_id
        LEFT JOIN partida p ON tp.partida_id = p.id
        LEFT JOIN evento ev ON p.evento_id = ev.id
        LEFT JOIN jogador_trofeu jt ON j.id = jt.jogador_id
        LEFT JOIN trofeu t ON t.evento_id = jt.evento_id
        GROUP BY 
            j.id
    )
    SELECT * FROM PlayerPerformance;
END;
$$ LANGUAGE plpgsql;
