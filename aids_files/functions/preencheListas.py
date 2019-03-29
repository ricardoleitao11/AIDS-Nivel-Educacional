# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 18:35:21 2019
@author: ricardo.leitao
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
    return lista_