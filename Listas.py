#listas
frutas = ["maçã","manga","melancia", "banana" ]
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])

#Métodos de listas
frutas.append("pera")
print(frutas)  # Imprime ['maçã', 'manga', 'melancia', 'banana', 'pera']


frutas.insert(1, "uva")
print(frutas)  # Imprime ['maçã', 'uva', 'manga', 'melancia', 'banana', 'pera']


frutas.remove("banana")
print(frutas)  # Imprime ['maçã', 'uva', 'manga', 'melancia', 'pera']


fruta_removida = frutas.pop(2)
print(frutas)  # Imprime ['maçã', 'uva', 'melancia', 'pera']
print(fruta_removida)  # Imprime "manga"


frutas.sort()
print(frutas)  # Imprime ['maçã', 'melancia', 'pera', 'uva']


frutas.reverse()
print(frutas)  # Imprime ['uva', 'pera', 'melancia', 'maçã']
#Listas de compreensão
números = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in números if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]