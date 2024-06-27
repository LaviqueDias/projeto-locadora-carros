
from sistema import *

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

        foi_adicionado = adicionar_paciente(dados_paciente, cpf)

        if foi_adicionado == True:
            print('\nPaciente cadastrado com sucesso!')
    
        else:
            print('\nPaciente já cadastrado!')


    elif opcao == 2: # Adicionar novo médico
        
        nome = input('Digite o nome do médico: ')
        especialidade = input('Digite a especialidade do médico: ')
        crm = int(input('Digite o CRM do médico: '))
        telefone = input('Digite o telefone do médico: ')
        dados_medico = (nome, especialidade, crm, telefone)

        foi_adicionado = adicionar_medico(dados_medico, crm)

        if foi_adicionado == True:
            print('\nMédico cadastrado com sucesso!')
    
        else:
            print('\nMédico já cadastrado!')


    elif opcao == 3: # Pesquisar paciente pelo CPF
        cpf = int(input('\nDigite o CPF do paciente: '))

        paciente_pesquisado = pesquisar_paciente_cpf(cpf)

        if len(paciente_pesquisado) != 0:
            print('\nPaciente do CPF %d encontrado!' % (cpf))
            print('\nCPF: %s\nNome: %s\nIdade: %s\nEndereço: %s\nTelefone: %s\n' % (paciente_pesquisado[0][0], paciente_pesquisado[0][1], paciente_pesquisado[0][2], paciente_pesquisado[0][3], paciente_pesquisado[0][4]))
        
        else:
            print('\nPaciente não encontrado!')

    
    elif opcao == 4: # Pesquisar médico pelo CRM
        crm = int(input('\nDigite o CRM do médico: '))

        medico_pesquisado = pesquisar_medico_crm(crm)

        if len(medico_pesquisado) != 0:
            print('\nMédico do CRM %d encontrado!' % (crm))
            print('\nNome: %s\nEspecialidade: %s\nCRM: %s\nTelefone: %s\n' % (medico_pesquisado[0][0], medico_pesquisado[0][1], medico_pesquisado[0][2], medico_pesquisado[0][3]))
        
        else:
            print('\nMédico não encontrado!')

    
    elif opcao == 5: # Excluir paciente pelo CPF

        cpf = int(input('Digite o CPF do paciente a ser deletado: '))

        foi_excluido = excluir_paciente_cpf(cpf)
        

        if foi_excluido == True:
            print('Paciente do CPF %s removido com sucesso!' % (cpf))
        
        else:
            print('Não há paciente com o CPF informado!')


    elif opcao == 6: # Excluir médico pelo CRM

        crm = int(input('Digite o CRM do médico a ser deletado: '))

        foi_excluido = excluir_medico_crm(crm)

        if foi_excluido == True:
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

                agendar_consulta(dados_agendamento)

                print('Consulta agendada com sucesso!')

                                

            elif opcao == 2: # Visualizar todas as consultas

                consultas = listar_consultas()

                if len(consultas) != 0:
                    print('\nLista de Consultas agendadas:')
                    
                    for item in consultas:
                        print('\nID: %s\nData: %s\nMotivo: %s\nCPF paciente: %s\nCRM médico: %s\n' % (item[0], item[1], item[2], item[3], item[4]))
                
                else:
                    print('\nNão há consultas agendadas!')
            

            elif opcao == 3: # Cancelar o agendamento de uma consulta
                id = int(input('Digite o ID da consulta que deseja cancelar: '))

                foi_cancelada = cancelar_consulta_id(id)  

                if foi_cancelada == True:
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

