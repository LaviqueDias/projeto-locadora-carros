import mysql.connector
import env.env
from operacoesbd import *
from env import *

conexao = env.conexaoInicial()

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


def adicionar_paciente(dados_paciente, cpf):

    foi_adicionado = False

    paciente_pesquisado = pesquisar_paciente_cpf(cpf)

    if len(paciente_pesquisado) == 0:
        sql_insert = 'insert into pacientes (cpf, nome, idade, endereco, telefone) values (%s, %s, %s, %s, %s)'
        insertNoBancoDados(conexao, sql_insert, dados_paciente)
        foi_adicionado = True

    return foi_adicionado



def adicionar_medico(dados_medico, crm):

    foi_adicionado = False
    medico_pesquisado = pesquisar_medico_crm(crm)

    if len(medico_pesquisado) == 0:
        sql_insert = 'insert into medicos (nome, especialidade, crm, telefone) values (%s, %s, %s, %s)'
        insertNoBancoDados(conexao, sql_insert, dados_medico)
        foi_adicionado = True

    return foi_adicionado



def pesquisar_paciente_cpf(cpf):

    sql_select = 'select * from pacientes where cpf = %s' % (cpf)

    paciente_pesquisado = listarBancoDados(conexao, sql_select)

    return paciente_pesquisado

        

def pesquisar_medico_crm(crm):

    sql_select = 'select * from medicos where crm = %s' % (crm)

    medico_pesquisado = listarBancoDados(conexao, sql_select)

    return medico_pesquisado



def excluir_paciente_cpf(cpf):

    sql_delete = 'delete from pacientes where cpf = %s'
    dados_delete = (cpf,)

    linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)
    foi_excluido = False

    if linhas_afetadas != 0:
        foi_excluido = True

    return foi_excluido


def excluir_medico_crm(crm):

    sql_delete = 'delete from medicos where crm = %s'
    dados_delete = (crm,)

    linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)
    foi_excluido = False

    if linhas_afetadas != 0:
        foi_excluido = True

    return foi_excluido


def agendar_consulta(dados_agendamento):

    sql_insert = 'insert into agendamentos (data, motivo, cpf, crm) values (%s, %s, %s, %s)'
    insertNoBancoDados(conexao, sql_insert, dados_agendamento)



def listar_consultas():

    sql_select = 'select * from agendamentos'
    return listarBancoDados(conexao, sql_select)


def cancelar_consulta_id(id):

    sql_delete = 'delete from agendamentos where id = %s'
    dados_delete = (id,)

    foi_cancelada = False
    linhas_afetadas = excluirBancoDados(conexao, sql_delete, dados_delete)

    if linhas_afetadas != 0:
        foi_cancelada = True

    return foi_cancelada


def adicionar_procedimento_medico(dados_procedimento):

    sql_insert = 'insert into procedimentos (data, receita, cpf, crm) values (%s, %s, %s, %s)'
    insertNoBancoDados(conexao, sql_insert, dados_procedimento)                


def listar_procedimentos_medicos():

    sql_select = 'select * from procedimentos'
    return listarBancoDados(conexao, sql_select)


encerrarBancoDados(conexao)

