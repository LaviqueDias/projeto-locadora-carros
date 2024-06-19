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
        "crm int"
    ]

# Criar tabela 'agendamentos'
criarTabela(conexao, 'agendamentos', campos_agendamentos, "hospital")

campos_procedimentos = [
        "id int auto_increment primary key",
        "data varchar(10)", 
        "receita varchar(100)",
        "cpf int",
        "crm int"
    ]

# Criar tabela 'procedimentos'
criarTabela(conexao, 'procedimentos', campos_procedimentos, "hospital")


opcao = 1

while opcao != 9:
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
        
        sql_select = 'select * from pacientes where cpf = %s' % (cpf)
        paciente_pesquisado = listarBancoDados(conexao, sql_select)

        if len(paciente_pesquisado) == 0:
            sql_insert = 'insert into pacientes (cpf, nome, idade, endereco, telefone) values (%s, %s, %s, %s, %s)'
            insertNoBancoDados(conexao, sql_insert, dados_paciente)
            print('\nPaciente cadastrado com sucesso!')
    
        else:
            print('\nPaciente já cadastrado!')


    elif opcao == 2: # Adicionar novo médico
        
        nome = input('Digite o nome do médico: ')
        especialidade = input('Digite a especialidade do médico: ')
        crm = int(input('Digite o CRM do médico: '))
        telefone = input('Digite o telefone do médico: ')
        dados_medico = (nome, especialidade, crm, telefone)

        sql_select = 'select * from medicos where crm = %s' % (crm)
        medico_pesquisado = listarBancoDados(conexao, sql_select)

        if len(medico_pesquisado) == 0:
            sql_insert = 'insert into medicos (nome, especialidade, crm, telefone) values (%s, %s, %s, %s)'
            insertNoBancoDados(conexao, sql_insert, dados_medico)
            print('\nMédico cadastrado com sucesso!')
    
        else:
            print('\nMédico já cadastrado!')


    elif opcao == 3: # Pesquisar paciente pelo CPF
        cpf = int(input('\nDigite o CPF do paciente: '))

        sql_select = 'select * from pacientes where cpf = %s' % (cpf)

        paciente_pesquisado = listarBancoDados(conexao, sql_select)

        if len(paciente_pesquisado) != 0:
            print('\nPaciente do CPF %d encontrado!' % (cpf))
            print('\nCPF: %s\nNome: %s\nIdade: %s\nEndereço: %s\nTelefone: %s\n' % (paciente_pesquisado[0][0], paciente_pesquisado[0][1], paciente_pesquisado[0][2], paciente_pesquisado[0][3], paciente_pesquisado[0][4]))
        
        else:
            print('\nPaciente não encontrado!')
    
    elif opcao == 4: # Pesquisar médico pelo CRM
        crm = int(input('\nDigite o CRM do médico: '))

        sql_select = 'select * from medicos where crm = %s' % (crm)

        medico_pesquisado = listarBancoDados(conexao, sql_select)

        if len(medico_pesquisado) != 0:
            print('\nMédico do CRM %d encontrado!' % (crm))
            print('\nNome: %s\nEspecialidade: %s\nCRM: %s\nTelefone: %s\n' % (medico_pesquisado[0][0], medico_pesquisado[0][1], medico_pesquisado[0][2], medico_pesquisado[0][3]))
        
        else:
            print('\nMédico não encontrado!')
    
    elif opcao == 5: # Excluir paciente pelo CPF
        cpf = int(input('Digite o CPF do paciente a ser deletado: '))

        sql_delete = 'delete from pacientes where cpf = %s'
        dados_delete = (cpf,)
        linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)

        if linhas_afetadas != 0:
            print('Paciente do CPF %s removido com sucesso!' % (cpf))
        
        else:
            print('Não há paciente com o CPF informado!')


    elif opcao == 6: # Excluir médico pelo CRM
        crm = int(input('Digite o CRM do médico a ser deletado: '))

        sql_delete = 'delete from medicos where crm = %s'
        dados_delete = (crm,)
        linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)
        print("%s linhas foram excluídas." % (linhas_afetadas))

        if linhas_afetadas != 0:
            print('Médico do CRM %s removido com sucesso!' % (crm))
        
        else:
            print('Não há médico com o CRM informado!')


    elif opcao == 7: # Agendar consulta
        opcao = 1

        while opcao != 4:
            print('\n=====AGENDAMENTO DE CONSULTAS=====')
            print("1. Agendar uma nova consulta")
            print("2. Visualizar todas as consultas")
            print("3. Cancelar o agendamento de uma consulta")
            print('4. Sair')

            opcao = int(input('\nDigite uma opção: '))

            if opcao == 1: # Agendar uma nova consulta
                data = input('\nDigite a data da consulta: ')
                motivo = input('Digite o motivo da consulta: ')
                cpf = int(input('Digite o CPF do paciente: '))
                crm = int(input('Digite o CRM do médico: '))
                dados_agendamento = (data, motivo, cpf, crm)

                sql_insert = 'insert into agendamentos (data, motivo, cpf, crm) values (%s, %s, %s, %s)'
                insertNoBancoDados(conexao, sql_insert, dados_agendamento)                

            elif opcao == 2: # Visualizar todas as consultas
                sql_select = 'select * from agendamentos'

                consultas = listarBancoDados(conexao, sql_select)

                if len(consultas) != 0:
                    print('\nLista de Consultas agendadas:')
                    
                    for item in consultas:
                        print('\nID: %s\nData: %s\nMotivo: %s\nCPF paciente: %s\nCRM médico: %s\n' % (item[0], item[1], item[2], item[3], item[4]))
                
                else:
                    print('\nNão há consultas agendadas!')
            

            elif opcao == 3: # Cancelar o agendamento de uma consulta
                id = int(input('Digite o ID da consulta que deseja cancelar: '))

                sql_delete = 'delete from agendamentos where id = %s'
                dados_delete = (id,)

                linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)
                print("%s linhas foram excluídas." % (linhas_afetadas))  

                if linhas_afetadas != 0:
                    print('Consulta do ID %s removida com sucesso!' % (id))
                
                else:
                    print('Não há consulta com o ID informado!')
              

            elif opcao != 4:
                print('Digite uma opção válida!')

    elif opcao == 8: # Registrar procedimento médico
        opcao = 1

        while opcao != 3:
            print('\n=====REGISTRO DE PROCEDIMENTOS=====')
            print("1. Adicionar um procedimento médico")
            print("2. Visualizar todos os procedimentos médicos")
            print('3. Sair')

            opcao = int(input('\nDigite uma opção: '))

            if opcao == 1: # Adicionar um procedimento médico
                data = input('\nDigite a data da consulta: ')
                receita = input('Digite a receita pro paciente: ')
                cpf = int(input('Digite o CPF do paciente: '))
                crm = int(input('Digite o CRM do médico: '))
                dados_procedimento = (data, receita, cpf, crm)

                sql_insert = 'insert into procedimentos (data, receita, cpf, crm) values (%s, %s, %s, %s)'
                insertNoBancoDados(conexao, sql_insert, dados_procedimento)                

            elif opcao == 2: # Visualizar todos os procedimentos médicos
                sql_select = 'select * from procedimentos'

                procedimentos = listarBancoDados(conexao, sql_select)

                if len(procedimentos) != 0:
                    print('\nLista de Procedimentos médicos:')
                    
                    for item in procedimentos:
                        print('\nID: %s\nData: %s\nReceita: %s\nCPF paciente: %s\nCRM médico: %s\n' % (item[0], item[1], item[2], item[3], item[4]))
                
                else:
                    print('\nNão há procedimentos cadastrados!')
                
            elif opcao != 3:
                print('Digite uma opção válida!')


    elif opcao != 9:
        print('\nOpção Inválida')



print('\nObrigado por usar o sistema do nosso hospital!')
encerrarBancoDados(conexao)

