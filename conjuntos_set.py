#conjuntos(set)
frutas ={"maçã","banana","laranja","maçã"}
numeros = set([1,2,3,4,5])
print(numeros)
print(frutas)# saida {'banana', 'laranja', 'maçã'}

print("=" *40 )

conjunto1 ={1,2,3}
conjunto2 ={5,3,4}

#união
uniao = conjunto1 | conjunto2
print(uniao)# saida {1, 2, 3, 4, 5}

#Intersecao
intersecao = conjunto1 & conjunto2
print(intersecao)# saida {3}

#Diferença
diferenca = conjunto1 - conjunto2
print(diferenca)# saida {1,2}

#Diferença Simetrica
diferenca_simetrica = conjunto1 ^ conjunto2
print(diferenca_simetrica)# saida {1,2,4,5}
print("=" *40)
#Métodos de conjuntos
#add
frutas.add("pera")
print(frutas)#Saida {'banana', 'maçã', 'laranja', 'pera'}

#remove
frutas.remove("banana")
print(frutas)#Saida {'maçã', 'laranja', 'pera'}

#discarda
frutas.discard("uva")
print(frutas)#Saida {'maçã', 'laranja', 'pera'}

frutas.clear()
print(frutas)#Saida set()