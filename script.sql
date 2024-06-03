CREATE TABLE cotacao_dolar (
    id SERIAL PRIMARY KEY,
    data DATE,
    hora TIME,
    cotacao DECIMAL (10, 2)
);

CREATE OR REPLACE PROCEDURE inserir_tabela(data DATE, hora VARCHAR, cotacao DECIMAL)
AS
$$
    BEGIN
        INSERT INTO cotacao_dolar(data, hora, cotacao) VALUES (data, hora::TIME, cotacao);
    END;
$$
LANGUAGE plpgsql;