<h1 align="center">
  Sistema de Gerenciamento Hospitalar (Python + MySQL)
</h1>
Este projeto é um Sistema de Gerenciamento Hospitalar desenvolvido em Python com banco de dados MySQL. 

## Pré-requisitos

Antes de testar o sistema, certifique-se de que os seguintes itens estão instalados:

- Python (versão 3.7 ou superior).
- MySQL (servidor configurado e funcionando).
- Biblioteca mysql-connector instalada no Python:
```
pip install mysql-connector-python
```

## Configuração do Ambiente

- Crie uma pasta chamada env no diretório do projeto.

- Dentro da pasta env, crie um arquivo env.py com o seguinte conteúdo:
```
import operacoesbd

def conexaoInicial():
    conexao = operacoesbd.criarConexaoInicial(
        "seu_endereco", 
        "seu_host", 
        "sua_senha"
    )
    return conexao
```
- Substitua os parâmetros "seu_endereco", "seu_host", e "sua_senha" pelas suas credenciais do banco de dados.
    - seu_endereco: Endereço ou IP do servidor MySQL (por exemplo, "localhost").
    - seu_host: Nome de usuário do MySQL (por exemplo, "root").
    - sua_senha: Senha do usuário MySQL.

## Execução do Sistema

- Certifique-se de que o MySQL está rodando e execute o sistema conforme as instruções do arquivo principal do projeto.
