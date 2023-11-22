frase = 'Olá bem vindo a esse treinamento'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'jonatan, rafael, carol, amanda,jefferson'
print(nomes.split())
print(nomes.split(','))
hashtags = 'music #guitar #gamer #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
# separa por # ate o terceira ocorrencia
print(hashtags.split('#', 3))
# Como concatenar(combinar) strings
hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))



#Desafio1
##Transforme a frase1 em uma lista de palavras e guarde o resultado em uma variável chamada palavras1
# #Desafio2
# ##Transforme a frase2 em uma lista de palavras e guarde o resultado em uma variável chamada palavras2
# #Desafio3
##Pegue o palavra1 e transforme elas no seguinte string: "desafio, manipulação, de strings". imprima o resultado no sonsole.
# #Desafio4
# ##Pegue o palavra2 e transforme elas no seguinte string: frase2 = "jonatan & rafael & carol & camilla". imprima o resultado no console.

frase1 = 'Desafio manipulaçâo de string'
palavras1 = frase1.split()
print(palavras1)
palavras1 = frase1.split(' ')
print(','.join(palavras1))


frase2 = 'jonatan,rafael,carol,camilla'
palavras2 = frase2.split(',')
print(palavras2)
palavras_separadas = ' & '.join(palavras2)
print(palavras_separadas)




