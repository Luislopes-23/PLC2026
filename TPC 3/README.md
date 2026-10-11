## TPC3 : Analisador Léxico

Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:

```
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
?s a dbo:MusicalArtist.
?s foaf:name "Chuck Berry"@en .
?w dbo:artist ?s.
?w foaf:name ?nome.
?w dbo:abstract ?desc
} LIMIT 1000

```

## EXEMPLO

Se colocarmos o texto mostrado em cima no analisador, o resultado obtido deve ser, por exemplo:

```
('SELECT', 'select', 2, (32, 38))
('VARIAVEL', '?nome', 2, (39, 44))
('VARIAVEL', '?desc', 2, (45, 50))
('WHERE', 'where', 2, (51, 56))
('DELIMITADOR', '{', 2, (57, 58))
('VARIAVEL', '?s', 3, (59, 61))
('CONCEITO', 'a', 3, (62, 63))
('CONCEITO', 'dbo:MusicalArtist', 3, (64, 81))
('DELIMITADOR', '.', 3, (81, 82))
('VARIAVEL', '?s', 4, (83, 85))
('CONCEITO', 'foaf:name', 4, (86, 95))
('STRING', '"Chuck Berry"', 4, (96, 109))
('LINGUA', '@en', 4, (109, 112))
('VARIAVEL', '?w', 5, (113, 115))
('CONCEITO', 'dbo:artist', 5, (116, 126))
('VARIAVEL', '?s', 5, (127, 129))
('DELIMITADOR', '.', 5, (129, 130))
('VARIAVEL', '?w', 6, (131, 133))
('CONCEITO', 'foaf:name', 6, (134, 143))
('VARIAVEL', '?nome', 6, (144, 149))
('DELIMITADOR', '.', 6, (149, 150))
('VARIAVEL', '?w', 7, (151, 153))
('CONCEITO', 'dbo:abstract', 7, (154, 166))
('VARIAVEL', '?desc', 7, (167, 172))
('DELIMITADOR', '}', 8, (173, 174))
('LIMIT', 'LIMIT', 8, (175, 180))
('NUMERO', '1000', 8, (181, 185))
```

## EXPLICAÇÃO

O analisador usa as expressões regulares para identificar cada tipo de token na query, e depois cria um tuplo para cada correspondência encontrada, no formato (TIPO, VALOR, LINHA, POSIÇÕES).
