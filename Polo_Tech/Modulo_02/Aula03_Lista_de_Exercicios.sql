-- Base de dados - sales

-- Exercicio 1: Quantos itens distintos foram vendidos (item_id)?
SELECT 
	COUNT(DISTINCT item_id) AS itens_distintos
FROM 
	sales;

-- Exercicio 2: Quantas lojas existem na base (loja_id)?
SELECT 
	COUNT(DISTINCT loja_id) AS itens_distintos
FROM 
	sales;

-- Exercicio 3: Qual é a cidade que mais tem lojas (loja_id)?
SELECT 
	DISTINCT cidade,
	COUNT(DISTINCT loja_id) AS qtd_lojas
FROM
	sales
GROUP BY DISTINCT cidade
ORDER BY COUNT(DISTINCT loja_id) DESC
LIMIT 1;

-- Exercicio 4: Em qual municipio foi vendido mais itens?
SELECT 
	DISTINCT municipio,
	COUNT(item_id) AS itens_vendidos
FROM
	sales
GROUP BY DISTINCT municipio
ORDER BY COUNT(item_id) DESC
LIMIT 1;

-- Exercicio 5: Qual a cidade mais vendeu em dolares?
SELECT 
	DISTINCT cidade,
	SUM(total_venda) AS total_venda_cidade
FROM
	sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- Exercicio 6: Qual foi o dia que mais vendeu itens distintos?
SELECT 
	DISTINCT data_pedido,
	COUNT(DISTINCT item_id) AS total_itens_id
FROM
	sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 1;

-- Exercicio 7: Monte o top 5 bebidas (item_id) mais vendidas por valor?
SELECT 
	DISTINCT item_id,
	SUM(total_venda) AS total_venda_item_id
FROM
	sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;

-- Exercicio 8: Monte o top 5 bebidas (item_id) mais vendidas por volume em litros
SELECT 
	DISTINCT item_id,
	SUM(volume_litros_vendidos) AS total_venda_litros
FROM
	sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 5;

-- Exercicio 9: Quais são as 10 empresas (marca_id) que mais lucram com a venda de bebidas?
SELECT 
	DISTINCT marca_id,
	SUM(total_venda - custo_garrafa*garrafas_vendidas) AS lucro_marca
FROM 
	sales
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;

-- Exercicio 10: Monte uma tabela com a quantidade de vendas distintas por dia.
SELECT 
	DISTINCT data_pedido,
	COUNT(DISTINCT item_id) AS qtd_venda_distinta
FROM 
	sales
GROUP BY 1;