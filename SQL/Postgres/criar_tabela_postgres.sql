BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

CREATE TABLE evento (
    id SERIAL NOT NULL, 
    nome VARCHAR(100) NOT NULL, 
    data_inicio DATE NOT NULL, 
    data_fim DATE NOT NULL, 
    pais VARCHAR(100) NOT NULL, 
    presencial BOOLEAN NOT NULL, 
    premiacao NUMERIC NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (nome)
);

CREATE TABLE foto (
    id SERIAL NOT NULL, 
    nome VARCHAR(255) NOT NULL, 
    nome_foto VARCHAR NOT NULL, 
    dados BYTEA NOT NULL, 
    PRIMARY KEY (id)
);

CREATE TABLE mapa (
    id SERIAL NOT NULL, 
    nome VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (nome)
);

CREATE TABLE noticia (
    id SERIAL NOT NULL, 
    cabecalho VARCHAR(100) NOT NULL, 
    corpo TEXT NOT NULL, 
    autor VARCHAR(100) NOT NULL, 
    regiao VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id)
);

CREATE TABLE ranking (
    id SERIAL NOT NULL, 
    regiao VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (regiao)
);

CREATE TABLE time (
    id SERIAL NOT NULL, 
    name VARCHAR(100) NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (name)
);

CREATE TABLE escalacao (
    id SERIAL NOT NULL, 
    ativo BOOLEAN, 
    data_inicio DATE NOT NULL, 
    data_fim DATE NOT NULL, 
    time_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(time_id) REFERENCES time (id)
);

CREATE TABLE jogador (
    id SERIAL NOT NULL, 
    name VARCHAR(100) NOT NULL, 
    apelido VARCHAR(100) NOT NULL, 
    nacionalidade VARCHAR(255) NOT NULL, 
    data_nascimento DATE NOT NULL, 
    genero VARCHAR(50) NOT NULL, 
    foto_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(foto_id) REFERENCES foto (id)
);

CREATE TABLE partida (
    id SERIAL NOT NULL, 
    data DATE NOT NULL, 
    evento_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(evento_id) REFERENCES evento (id)
);

CREATE TABLE time_evento (
    evento_id INTEGER NOT NULL, 
    time_id INTEGER NOT NULL, 
    PRIMARY KEY (evento_id, time_id), 
    FOREIGN KEY(evento_id) REFERENCES evento (id), 
    FOREIGN KEY(time_id) REFERENCES time (id)
);

CREATE TABLE time_ranking (
    time_id INTEGER NOT NULL, 
    ranking_id INTEGER NOT NULL, 
    posicao INTEGER NOT NULL, 
    PRIMARY KEY (time_id, ranking_id), 
    FOREIGN KEY(ranking_id) REFERENCES ranking (id), 
    FOREIGN KEY(time_id) REFERENCES time (id), 
    CONSTRAINT time_posicao_ranking UNIQUE (time_id, ranking_id, posicao)
);

CREATE TABLE trofeu (
    evento_id INTEGER NOT NULL, 
    foto_id INTEGER, 
    PRIMARY KEY (evento_id), 
    FOREIGN KEY(evento_id) REFERENCES evento (id), 
    FOREIGN KEY(foto_id) REFERENCES foto (id)
);

CREATE TABLE escalacao_jogador (
    escalacao_id INTEGER NOT NULL, 
    jogador_id INTEGER NOT NULL, 
    treinador BOOLEAN, 
    PRIMARY KEY (escalacao_id, jogador_id), 
    FOREIGN KEY(escalacao_id) REFERENCES escalacao (id), 
    FOREIGN KEY(jogador_id) REFERENCES jogador (id)
);

CREATE TABLE jogador_trofeu (
    evento_id INTEGER NOT NULL, 
    jogador_id INTEGER NOT NULL, 
    PRIMARY KEY (evento_id, jogador_id), 
    FOREIGN KEY(evento_id) REFERENCES trofeu (evento_id), 
    FOREIGN KEY(jogador_id) REFERENCES jogador (id)
);

CREATE TABLE mapa_partida (
    partida_id INTEGER NOT NULL, 
    mapa_id INTEGER NOT NULL, 
    PRIMARY KEY (partida_id, mapa_id), 
    FOREIGN KEY(mapa_id) REFERENCES mapa (id), 
    FOREIGN KEY(partida_id) REFERENCES partida (id)
);

CREATE TABLE time_partida (
    partida_id INTEGER NOT NULL, 
    time_id INTEGER NOT NULL, 
    PRIMARY KEY (partida_id, time_id), 
    FOREIGN KEY(partida_id) REFERENCES partida (id), 
    FOREIGN KEY(time_id) REFERENCES time (id)
);

COMMIT;
