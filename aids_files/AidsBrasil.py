import matplotlib.pyplot
import pandas as pd

arquivo = pd.read_csv('aids-brasil.csv', sep=';', encoding='latin-1')

print (arquivo[0])