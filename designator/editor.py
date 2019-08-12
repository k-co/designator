'''
Created on 11 de ago de 2019

@author: k_co
'''

import datetime
import calendar
import json

LISTA = {}
DATAS = {}

def adicionar_participante(nome,partes):
    '''
    @nome completo do participante
    @partes que está apto a realizar, pode ser um sistema binário
    retorna boolean de sucesso, erro se já houver participante com esse nome
    ou simplesmente pergunta se deseja atualizar o registro.
    '''
    LISTA[nome]=partes
    
def remover_participante(nome):
    '''
    @nome remove participante se estiver na lista
    '''
    if nome in LISTA: LISTA.pop(nome)

def salvar_dados_json(arquivo,dados):
    '''
    @arquivo onde salvar, retorna booleano de sucesso, erro se o arquivo
    já existir ou simplesmente pergunta se deseja atualizar o registro, ou o
    arquivo não pode ser salvo por falta de permissão.
    https://realpython.com/python-json/
    '''
    with open (arquivo,'w') as doc:
        json.dump(dados,doc)

def carregar_dados_json(arquivo):
    '''
    @arquivo carrega lista previamente salva em um arquivo
    retorna dicionario de nome e partes que está apto.
    '''
    with open(arquivo,'r') as doc:
        return json.load(doc)

def adicionar_evento(data):
    '''
    @data dia do evento
    '''
    pass

def mover_evento(data_antiga, data_nova):
    '''
    @data_antiga
    @data_nova
    Move o evento para outra data
    '''
    pass

def gerar_eventos_do_mes(ano,mes,diadasemana):
    '''
    Retorna lista contendo todos os dias do mês que correspondem ao dia 
    da semana selecionado.       
    @data_inicio ? 
    @diadasemana inteiro 0 - 6 = segunda - domingo
    '''
    l=[]
    for i in calendar.Calendar().itermonthdays2(ano,mes):
        if i[1] == diadasemana and i[0]:
            l.append(i[0])
    return l
            

def dds(dia,mes,ano):
    '''
    Retorna o inteiro que corresponde ao dia da semana
    '''
    return datetime.date(ano,mes,dia).weekday()
    
def dds_nome(inteiro):
    '''
    @inteiro 0-6 retorna o nome do dia da semana
    '''
    l='Segunda Terça-Feira Quarta-Feira Quita-Feira Sexta-Feira Sábado Domingo'.split(' ')
    return l[inteiro]

def a():
    '''
    
    '''
    pass

''' PARTES DEFINIDAS EM BINARIO

b'0000 0000'
  |||| |||L-Parte publicador
  |||| ||L--Parte leitura
  |||| |L---Oração
  |||| L----Servo
  |||L -----Ancião
  ||L- -----Interpretação
  XX
ex.: gabriel b'00101111' = 32+15 = 47 
'''

def teste1():
    limpar = lambda: print('\n'*200)
    
    limpar()
    print('''0-Sair\n1-adicionar participante\n2-salvar dados\
\n3-carregar dados\n4-gerar eventos\n''')
    opcao = input('Escolha uma opção: ')
    if opcao == '1':
        limpar()
        nome = input('Digite o Nome: ')
        limpar()
        partes = input('Digite um valor para Partes: ')
        limpar()
        print('Está correto?\t%s,%s\n1-Sim\n2-Não\n' % (nome,partes))
        opcao = input()
        if opcao == '1':
            adicionar_participante(nome, partes)
            
    elif opcao == '2':
        limpar()
        salvar_dados_json('lista.json', LISTA)
        print('salvo')
        input('(Enter)')
        
    elif opcao == '3':
        limpar()
        _LISTA = carregar_dados_json('lista.json')
        print('Dados carregados: \n%s' % str(_LISTA))
        input('(Enter)')
        
    elif opcao == '4':
        limpar()
        print('''Escolha o dia Reunião (1-Dom a 7-Sáb): \n''')
        diadasemana = int(input())-2
        if diadasemana == -1:
            diadasemana = 6
        limpar()
        print('''Dia: %s\nEscolha o mês (1-Jan a 12-Dez): \n''' % dds_nome(diadasemana))
        mes = int(input())
        limpar()
        print('''Dia: %s-%d\nEscolha o ano: \n''' %(dds_nome(diadasemana),mes))
        ano = int(input())        
        limpar()
        print('''Dia: %s-%d/%d\nData correta?(1-Sim/2-Não): \n''' % (dds_nome(diadasemana),mes,ano))
        opcao = input()
        if opcao == '1':
            DATAS = gerar_eventos_do_mes(ano,mes,diadasemana)
            limpar()
            print(DATAS)
            input('\n(Enter)')

            
    else: # == 0
        #limpar()
        exit()
        
        
    

if __name__ == '__main__':
    while(1):
        teste1()