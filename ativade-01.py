data = open(r"C:\Users\Lucas\Downloads\shootingsdata.csv", 'r')
info = data.readlines()
del info[0]
data.close()

idades = []
for linha in info:
    linhaE = linha.split(',')
    idade = linhaE[5]
    if idade[0] in '1234567890':
        idades.append(round(float(idade)))


'''distribuição de frequência'''

n_classes = 6
maior = max(idades)
menor = min(idades)
amplitude = maior - menor

amplitude_classe = round(amplitude/n_classes)

limites = []
limites.append(menor)

for x in range(n_classes):
    limites.append(limites[x] + amplitude_classe)

'''após os cálculos acima definimos que nossas classes estão delimitadas nas seguintes idades:
6 -- 19
20 -- 33
34 -- 47
48 -- 61
62 -- 76
77 -- 90
'''
###ocorrências nas classes

ocorrencias = {'6 a 19': 0, '20 a 33': 0, '34 a 47': 0, '48 a 61': 0, '62 a 76': 0, '77 a 90': 0 }

for idade in idades:
    if idade < limites[1]: ocorrencias['6 a 19'] += 1
    elif idade < limites[2]: ocorrencias['20 a 33'] += 1
    elif idade < limites[3]: ocorrencias['34 a 47'] += 1
    elif idade < limites[4]: ocorrencias['48 a 61'] += 1
    elif idade < limites[5]: ocorrencias['62 a 76'] += 1
    else:
        ocorrencias['77 a 90'] += 1

'''
Num total de 4887 casos obtivemos a seguinte distribuição:

6 a 19 = 271 ~ 5,54%
20 a 33 = 2009 ~ 41,1%
34 a 47 = 1638 ~ 33,51%
48 a 61 = 764 ~ 15,63%
62 a 76 = 180 ~ 3,68%
77 a 90 = 25 ~ 0,51%
'''

''''medidas de tendência central'''
media = sum(idades)/len(idades)
#print(media)

mediana_lista = sorted(idades)
mediana = mediana_lista[int(len(idades)/2-1)]
#print(mediana)

moda = None
cont = [0] * len(idades)
for x in range(len(idades)):
    cont[x] += idades.count(idades[x])

maiorpos = 0
maiorcont = cont[0]
for y in range(1, len(cont)):
    if cont[y] > maiorcont:
        maiorpos = y

moda = idades[maiorpos]
'''
print(maiorcont)
print(moda)
'''

#assim obtivemos 36.5 anos de média e 35 anos como mediana, nossa moda foi de 31 anos, a idade mais comum entre as mortes 



''''medidas de variação'''


###variância

variancia= 0
for numero in idades:
  variancia += (numero - media) ** 2
variancia = variancia/len(idades)

#print(variancia)

###desvio padrão
desvio = variancia ** (1/2)
#print(desvio)

'''e assim obtemos 161.10 de variância e 12.70 de desvio padrão'''



'''medidas de posição'''
q2 = mediana

idades1 = mediana_lista[0:int(len(idades)/2-1)]
q1 = idades1[int(len(idades1)/2-1)]

idades2 = mediana_lista[int(len(idades)/2):]
q3 = idades2[int(len(idades2)/2-1)]

'''print(q1)
print(q2)
print(q3)'''

'''
Aproximadamente 1/4 dos mortos tinham 27 anos ou menos
Aproximadamente metade dos mortos tinham 35 ou menos
Aproximadamente 3/4 dos mortos tinham 45 anos ou menos
'''


