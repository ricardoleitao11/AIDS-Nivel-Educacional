# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:55:50 2019
@author: ricardo.leitao

Função que preenche a lista de anos, de 1980 a 2017
** Na coluna de anos, existem aspas ("") que são desagradáveis ao resultado. Por isso, foi
    feita a tratativa que remove as aspas
"""
import pandas as pd

def preencheAnos():

    filename = 'C:\\AIDS-Nivel-Educacional\\aids_files\\aids-brasil.csv'
    arquivo = pd.read_csv(filename, encoding='latin-1', sep=',')

    lista_ = []
    for i in range(len(arquivo)):
        linha = arquivo.values[i][0].split(',')
        lista_.append(linha[0])

    lista_ = [x.replace('"', '') for x in lista_]
    lista_.remove(lista_[-1])
    lista_ = [int(x) for x in lista_]
    return lista_
