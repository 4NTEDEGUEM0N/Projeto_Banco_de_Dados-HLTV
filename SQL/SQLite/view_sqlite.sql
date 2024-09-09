CREATE VIEW jogador_detalhes_view AS
SELECT 
    j.id AS jogador_id,
    j.name AS nome_jogador,
    j.apelido,
    j.nacionalidade,
    j.data_nascimento,
    j.genero,
    GROUP_CONCAT(DISTINCT t.name) AS time_atual,
    e.nome AS evento_trofeu,
    e.id AS evento_id,
    trof.foto_id as trofeu_foto_id,
    f.nome_foto AS nome_foto,
    f.id AS foto_id
FROM jogador j
LEFT JOIN escalacao_jogador ej ON j.id = ej.jogador_id
LEFT JOIN escalacao ecal ON ej.escalacao_id = ecal.id AND ecal.ativo = TRUE
LEFT JOIN time t ON ecal.time_id = t.id
LEFT JOIN jogador_trofeu jt ON j.id = jt.jogador_id
LEFT JOIN trofeu trof ON jt.evento_id = trof.evento_id
LEFT JOIN evento e ON jt.evento_id = e.id
LEFT JOIN foto f ON j.foto_id = f.id
GROUP BY j.id, j.name, j.apelido, j.nacionalidade, j.data_nascimento, j.genero, e.nome, e.id, trof.foto_id, f.nome_foto, f.dados;
