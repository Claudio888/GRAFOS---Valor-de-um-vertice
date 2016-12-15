#coding: utf-8
import networkx as nx  #Importa networkx X responsavel por trabalhar com grafos
import numpy as np   # Numpy, trabalha com vetores 
import matplotlib.pyplot as plt 
import collections #biblioteca utilizada para ordenar um dicionario 



G = nx.read_gml('C:/Users/Claudio/Desktop/trabalhografo/dolphins.gml') # Importando o grafo enviado pelo professor

prob=np.empty([]) #Criando vetor vazio chamado prob com numpy e sua propriedade empty 

Narestas2=(G.number_of_edges())*2 #Multiplica o numero de aresta por 2, necessario para encontrar a probabilidade desejada

graus=G.degree() # jogo na variavel graus, o dicionario com o nome do vertice e seus graus. 

#print(graus)

print("----------------------------------------")
print(" ")
print('Vertices e seus respectivos graus')
print(" ")
print(collections.OrderedDict(sorted(graus.items())))


def distribuicao(G): # Função que executa o calculo da probabilidade 
    graus.update((x, y / (Narestas2)*100) for x, y in graus.items()) #Utilizo a função update, que seve para editar dicionarios, onde X é o nome do vertice e Y o grau do mesmo, 
    																 #o for logo em seguida serve para iterar ou seja fazer a conta em todos os itens do dicionario(.item()) 
    prob=graus #atribuo o dicionario acima calculado ao vetor vazio prob 

    return prob # retorne o vetor

result=distribuicao(G) #variavel resultado recebe a função com sua propriedade G 
#print(result) #Escreva a variavel result. 


print("----------------------------------------")
print(" ")
print('Vertices e sua porcentagem') 
print(" ")
print(collections.OrderedDict(sorted(result.items())))#impressão do dicionario result ordenado alfabeticamente


print("----------------------------------------")
print(" ")
print('Soma da porcentagem de todos os vertices')
print(sum(graus.values()))#soma todos os valores para conferir se chegam a 100 % 

print("----------------------------------------")
print(" ")
print('Vertice com a maior porcentagem')
print(max(result, key=result.get))#Retira do dicionario o maior valor 


# Parte da plotagem do grafico. 


y_axis =graus.values()#define valores para Y do grafico, os valores de cada vertice
x_axis = range(len(y_axis))#tamanho do eixo X , range dos valores 
width_n=0.5 # tamanho das barras
bar_color='yellow'#cor das barras 

legenda=graus.keys() # legenda de cada barra, sua correspondente chave 

ax=plt.axes() #ax para eixos, facilitar programçaão 

grafico = plt.bar(x_axis,y_axis, width=width_n,color=bar_color) #define o grafico(eixox,eixoy,tamanho,cor)


ax.set_xticks(x_axis)#define que para cada barra havera uma legenda, define o espaçamento delas. 

ax.set_xticklabels(legenda,rotation='vertical') #atribui a legenda os nomes dos vertices rotacionando para vertical 

plt.xlabel('Vertices') #label x = vertice 
plt.ylabel('Valores') # label y = valores 
plt.title('Relacao de vertice de um grafo e seu valor dentro da estrutura') #titulo 

plt.grid(True) #coloque grid = sim 

plt.show() #mostre o grafico. 


