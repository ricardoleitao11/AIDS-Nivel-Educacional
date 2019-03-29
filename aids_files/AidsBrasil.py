# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 15:43:50 2019
@author: ricardo.leitao
Main()
"""


import matplotlib.pyplot as plt
#import pandas as pd
import functions

#### preenche a lista com os anos
anos = functions.preencheAnos()

#### preenche as demais listas
analfabeto = functions.preencheListas(1)
primeiraaquartainc = functions.preencheListas(2)
quartacompleta = functions.preencheListas(3)
quintaaoitavainc = functions.preencheListas(4)
fundamentalcomp = functions.preencheListas(5)
medioincompl = functions.preencheListas(6)
mediocompl = functions.preencheListas(7)
superiorimcompl = functions.preencheListas(8)
superiorcompl = functions.preencheListas(9)
naoseaplica = functions.preencheListas(10)

fig = plt.figure(figsize=(10,5))
plt.xticks(range(1980,2020, 5))
plt.yticks(range(0,10000, 500))
plt.xlabel('Anos 1980-2017')
plt.ylabel('Quantidade de casos')
plt.plot(anos, analfabeto, color='#ff6666', label='Analfabeto')
plt.plot(anos, primeiraaquartainc, color='#668cff', label='1ª a 4ª serie incompleta')
plt.plot(anos, quartacompleta, color='#66ff33', label='4ª serie completa')
plt.plot(anos, quintaaoitavainc, color='#ff33cc', label='5ª a 8ª serie incompleta')
plt.plot(anos, fundamentalcomp, color='#3333ff', label='fundamental completo')
plt.plot(anos, medioincompl, color='#cc6600', label='medio incompleto')
plt.plot(anos, mediocompl, color='k', label='medio completo')
plt.plot(anos, superiorimcompl, color='#ffff00', label='superior incompleto')
plt.plot(anos, superiorcompl, color='#990099', label='superior completo')
plt.plot(anos, naoseaplica, color='#ff6600', label='NA')
plt.legend(bbox_to_anchor=(1.02,1), borderaxespad=0)
plt.subplots_adjust(right=0.7, left=0.125)
plt.savefig('Relacao_Aids.png', dpi=1000, orientation='portrait')





