# sistema-geren-hosp
Projeto de um Sistema de Gerenciamento Hospitalar feito em Python e MySQL. 

Caso queira testar:

- Instale a biblioteca do mysql connector na sua máquina
- Crie uma pasta env; Dentro dela crie um arquivo env.py; 

Dentro do arquivo env.py coloque:

import operacoesbd

def conexaoInicial():
    conexao = operacoesbd.criarConexaoInicial(seu_endereco, seu_host, sua_senha)
    return conexao

Trocando os parâmetros "seu_endereco", "seu_host" e "sua_senha" por suas respectivas credenciais.
