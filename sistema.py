import mysql.connector
from operacoesbd import *

conexao = criarConexaoInicial('localhost', 'root', 'admin')

criarBancoDados(conexao, 'hospital')

cursor = conexao.cursor()

cursor.close()

campos_pacientes = [
        "cpf int primary key",
        "nome varchar(100)",
        "idade int",
        "endereco varchar(100)",
        "telefone varchar(100)"
    ]

# Criar tabela 'pacientes'
criarTabela(conexao, 'pacientes', campos_pacientes, "hospital")

campos_medicos = [
        "nome varchar(100)",
        "especialidade varchar(100)",
        "crm int primary key",
        "telefone varchar(100)"
    ]

# Criar tabela 'medicos'
criarTabela(conexao, 'medicos', campos_medicos, "hospital")

campos_agendamentos = [
        "id int auto_increment primary key",
        "data varchar(10)", 
        "motivo varchar(100)",
        "cpf int",
        "crm int",
        "foreign key (cpf) references pacientes(cpf)",
        "foreign key (crm) references medicos(crm)"
    ]

# Criar tabela 'agendamentos'
criarTabela(conexao, 'agendamentos', campos_agendamentos, "hospital")

campos_procedimentos = [
        "id int auto_increment primary key",
        "data varchar(10)", 
        "receita varchar(100)",
        "cpf int",
        "crm int",
        "foreign key (cpf) references pacientes(cpf)",
        "foreign key (crm) references medicos(crm)"
    ]

# Criar tabela 'procedimentos'
criarTabela(conexao, 'procedimentos', campos_procedimentos, "hospital")


opcao = 1

while opcao != 6:
    print('\n=====HOSPITA ABC=====')
    print("1. Adicionar novo paciente")
    print("2. Adicionar novo médico")
    print("3. Pesquisar paciente pelo CPF")
    print("4. Pesquisar médico pelo CRM")
    print("5. Excluir paciente pelo CPF")
    print("6. Excluir médico pelo CRM")
    print("7. Agendar consulta")
    print("8. Registrar procedimento médico")
    print("9. Sair")

    opcao = int(input('\nDigite uma opção: '))

    if opcao == 1: # Adicionar novo paciente

        cpf = int(input('Digite o CPF do paciente: '))
        nome = input('Digite o nome do paciene: ')
        idade = int(input('Digite a idade do paciente: '))
        endereco = input('Digite o endereco do paciente: ')
        telefone = input('Digite o telefone do paciente: ')
        dados_paciente = (cpf, nome, idade, endereco, telefone)

        sql_insert = 'insert into pacientes (cpf, nome, idade, endereco, telefone)) values (%s, %s, %s, %s)'
        insertNoBancoDados(conexao, sql_insert, dados_paciente)


    elif opcao == 2: # Adicionar novo médico
        
        nome = input('Digite o nome do médico: ')
        especialidade = input('Digite a especialidade do médico: ')
        crm = int(input('Digite o CRM do médico: '))
        telefone = input('Digite o telefone do médico: ')
        dados_medico = (nome, especialidade, crm, telefone)

        sql_insert = 'insert into medicos (nome, especialidade, crm, telefone) values (%s, %s, %s, %s)'
        insertNoBancoDados(conexao, sql_insert, dados_medico)


    elif opcao == 3: # Pesquisar paciente pelo CPF
        cpf = int(input('\nDigite o CPF do paciente: '))

        sql_select = 'select * from pacientes where cpf = %s' % (cpf)

        paciente_pesquisado = listarBancoDados(conexao, sql_select)

        if len(paciente_pesquisado) != 0:
            print('\nPaciente do CPF %d encontrado!' % (cpf))
            print('\CPF: %s\nNome: %s\nIdade: %s\nEndereço: %s\nTelefone: %s\n' % (paciente_pesquisado[0][0], paciente_pesquisado[0][1], paciente_pesquisado[0][2], paciente_pesquisado[0][3], paciente_pesquisado[0][4]))
        
        else:
            print('\Paciente não encontrado!')
    
    elif opcao == 4: # Pesquisar médico pelo CRM
        crm = int(input('\nDigite o CRM do médico: '))

        sql_select = 'select * from medicos where crm = %s' % (crm)

        medico_pesquisado = listarBancoDados(conexao, sql_select)

        if len(medico_pesquisado) != 0:
            print('\nMédico do CRM %d encontrado!' % (crm))
            print('\Nome: %s\nEspecialidade: %s\nCRM: %s\nTelefone: %s\n' % (medico_pesquisado[0][0], medico_pesquisado[0][1], medico_pesquisado[0][2], medico_pesquisado[0][3]))
        
        else:
            print('\Médico não encontrado!')
    
    elif opcao == 5: # Excluir paciente pelo CPF
        codigo = int(input('Digite o código do filme a ser deletado: '))

        sql_delete = 'delete from filmes where codigo = %s'
        dados_delete = (codigo,)
        linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)
        print("%s linhas foram excluídas." % (linhas_afetadas))


    elif opcao == 6: # Excluir médico pelo CRM
        pass

    elif opcao == 7: # Agendar consulta
        pass

    elif opcao == 8: # Registrar procedimento médico
        pass

    elif opcao != 9:
        print('\nOpção Inválida')



print('\nObrigado por usar a locadora!')
encerrarBancoDados(conexao)

