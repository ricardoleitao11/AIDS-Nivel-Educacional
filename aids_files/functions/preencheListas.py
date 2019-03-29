# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:35:21 2019
@author: ricardo.leitao

Função que preenche as listas de casos de Aids por nível de escolaridade.
** A coluna TOTAL, presente no arquivo, não foi incluida pois afetaria os gráficos

"""
import pandas as pd

def preencheListas(x):

    filename = 'C:\\AIDS-Nivel-Educacional\\aids_files\\aids-brasil.csv'
    arquivo = pd.read_csv(filename, encoding='latin-1', sep=',')

    lista_ = []
    for i in range(len(arquivo)):
        linha = arquivo.values[i][0].split(',')
        lista_.append(linha[x])
        
    lista_.remove(lista_[-1])
    lista_ = [int(x) for x in lista_]
    return lista_