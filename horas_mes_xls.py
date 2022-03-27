import sys
import csv
# from IPython.display import display
import pandas as pd
from datetime import datetime, timedelta, date
import calendar
import io
from openpyxl import Workbook, load_workbook
import os

FMT = '%H:%M:%S'
# tam = 5
# col = 1
# pasta = '/home/alipio/00.planilha_horas_odoo/'
pasta = os.getcwd() + '/planilha_horas/'
print(pasta)

mod_xls = pasta + "modelo_openpyxl.xlsx"

DIAS = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']

FMT = '%H:%M:%S'

# pasta = '/home/alipio/00.planilha_horas_odoo/'
# lista = ''
# colaborador = ''

# arquivo = pasta + "lista_horas_janeiro_2022.xlsx"
arquivo = pasta + "lista_horas.xlsx"
df = pd.read_excel(arquivo, sheet_name=0)
lin_col = df.shape
nr_linhas = lin_col[0]
colaborador = ''
colab_old = ''
# arqxx = ''
passai = pasta + 'saida/'
y = 0
tam = 0
# dias = 31

dias = int(input('Quantidade de Dias: '))
dias += 1

# FUNTIONS GERAIS
# +++++++++++++++

def Dia_sem(x, mes):
    # data = date(year=2022, month=1, day=x)
    data = date(year=2022, month=mes, day=x)
    dia_semana = DIAS[data.weekday()]
    return(dia_semana)

def Util(tam):
    d_util = str(df['entrada'][tam][8:10])
    return (d_util)

def Cria_arquivo(val, colab):
    mod_arq = load_workbook(mod_xls)
    aba_ativa = mod_arq.active
    aba_ativa[f"A6"] = 'Colaborador: ' + colaborador
    return (mod_arq)

def Ler_dia(val):
    dtpri = str(df['entrada'][val][8:10])
    dtseg = str(df['entrada'][val+1][8:10])
    if dtpri == dtseg:
        return('I')
    else:
        return('D')

# Acerto fuso horario
def Acerto_fuso(hhmm):
    hrxx = int(hhmm[11:13]) - 3
    if len(str(hrxx)) == 1:
        hra = '0' + str(hrxx)
    else:
        hra = str(hrxx)
    hora = hra + hhmm[13:19]
    return(hora)


def Grava_1dia(val_tam, val_x, lin, aba, mes):
    # data = date(year=2022, month=1, day=val_x)
    data = date(year=2022, month=mes, day=val_x)
    dia_semana = DIAS[data.weekday()]
    # print(str(val_tam) + ' ..... x: ' + str(val_x) + ' .... S: ' + dia_semana)
    dthrin = str(df['entrada'][val_tam])
    dt01 = dthrin[8:10] + dthrin[4:8] + dthrin[0:4]
    dia_util = dthrin[8:10]
    hr01 = Acerto_fuso(dthrin)
    dthrfi = str(df['saida'][val_tam])
    if dthrfi == '0':
        hr02 = '00:00:00'
    else:
        hr02 = Acerto_fuso(dthrfi)

    td01 = datetime.strptime(hr02, FMT) - datetime.strptime(hr01, FMT)

    cel_a = "A" + str(lin)
    cel_b = "B" + str(lin)
    cel_c = "C" + str(lin)
    cel_d = "D" + str(lin)
    cel_e = "E" + str(lin)
    cel_f = "F" + str(lin)
    cel_g = "G" + str(lin)

    aba[cel_a] = dt01
    aba[cel_b] = dia_semana
    aba[cel_c] = hr01
    aba[cel_d] = hr02
    aba[cel_e] = ''
    aba[cel_f] = ''
    aba[cel_g] = str(td01)

def Grava_2dia(val_tam, val_x, lin, aba, mes):
        # data = date(year=2022, month=1, day=val_x)
        data = date(year=2022, month=mes, day=val_x)
        dia_semana = DIAS[data.weekday()]
        dthrin = str(df['entrada'][val_tam])
        dt01 = dthrin[8:10] + dthrin[4:8] + dthrin[0:4]
        dia_util = dthrin[8:10]
        hr01 = Acerto_fuso(dthrin)
        dthrfi = str(df['saida'][val_tam])

        if dthrfi == '':
            hr02 = '00:00:00'
        else:
            hr02 = Acerto_fuso(dthrfi)
        td01 = datetime.strptime(hr02, FMT) - datetime.strptime(hr01, FMT)


        dthrin = str(df['entrada'][val_tam+1])
        hr03 = Acerto_fuso(dthrin)
        dthrfi = str(df['saida'][val_tam+1])

        if dthrfi == '':
            hr04 = '00:00:00'
        else:
            hr04 = Acerto_fuso(dthrfi)
        td02 = datetime.strptime(hr04, FMT) - datetime.strptime(hr03, FMT)
        tdfin = td01 + td02

        cel_a = "A" + str(lin)
        cel_b = "B" + str(lin)
        cel_c = "C" + str(lin)
        cel_d = "D" + str(lin)
        cel_e = "E" + str(lin)
        cel_f = "F" + str(lin)
        cel_g = "G" + str(lin)

        aba[cel_a] = dt01
        aba[cel_b] = dia_semana
        aba[cel_c] = hr01
        aba[cel_d] = hr02
        aba[cel_e] = hr03
        aba[cel_f] = hr04
        aba[cel_g] = str(tdfin)

    # print(lin)
    # print(dt01)
    # print(hr01)
    # print(hr02)
    # exit()


def Grava_falta(val_tam, val_x, lin, aba, mes):
    if len(str(val_x)) == 1:
        zz = '0' + str(val_x)
    else:
        zz = str(val_x)

    # data = date(year=2022, month=1, day=val_x)
    data = date(year=2022, month=mes, day=val_x)
    dia_semana = DIAS[data.weekday()]
    dt01 = data.strftime('%d-%m-%Y')

    cel_a = "A" + str(lin)
    cel_b = "B" + str(lin)
    cel_c = "C" + str(lin)

    aba[cel_a] = dt01
    aba[cel_b] = dia_semana
    aba[cel_c] = 'FALTA'

x = 1
y = 0

# data = str(df['entrada'][tam])
mes_plan = int(str(df['entrada'][tam][5:7]))
print(mes_plan)
print(pasta)
# exit()


while tam < nr_linhas:
    colaborador = str(df['colaborador'][tam])
    if tam == 0 and y == 0:
        arq_sai = passai + colaborador + '.xlsx'
        colab_old = colaborador
        linha = 9
        modelo = Cria_arquivo(tam, colaborador)
        print(colaborador)
        y = 1

    if x == dias:
       x = 1

    dia_semana = Dia_sem(x, mes_plan)
    dia_util = Util(tam)
    print(dia_util)

    if dia_semana == 'Sábado' or dia_semana == 'Domingo':
       x += 1
    else:
        # d_util = str(df['entrada'][tam][8:10])

        if colaborador == 'xxx':
            modelo.save(arq_sai)
            exit()
        elif colab_old != colaborador:
            modelo.save(arq_sai)
            arq_sai = passai + colaborador + '.xlsx'
            colab_old = colaborador
            linha = 9
            modelo = Cria_arquivo(tam, colaborador)
            print(colaborador)
            x = 0
        else:
            if len(str(x)) == 1:
                kx = '0' + str(x)
            else:
                kx = str(x)

            aba_ativa = modelo.active
            if dia_util == kx:
                try:
                    compara = Ler_dia(tam)
                except:
                    print(tam)
                    dtpri = str(df['entrada'][tam][8:10])
                    dtseg = str(df['entrada'][tam + 1][8:10])
                    print(dtpri)
                    print(dtseg)
                    exit()

                if compara == 'D':
                    Grava_1dia(tam, x, linha, aba_ativa, mes_plan)
                else:
                    Grava_2dia(tam, x, linha, aba_ativa, mes_plan)
                    tam += 1
                linha += 1
                tam += 1
            else:
                # print(dia_util)
                print(colaborador + ' antes    x: ' + str(x) + '    antes tam: ' + str(tam))
                Grava_falta(tam, x, linha, aba_ativa, mes_plan)
                # modelo.save(arq_sai)
                # exit()
                # tam -= 1
                # exit()
                # x += 1
                linha += 1
        x += 1


print('Final gravação')

