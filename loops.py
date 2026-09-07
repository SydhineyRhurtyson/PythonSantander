#loops
# For
alunos = ["Victor","Maria","Eduarda","Danieli"]

for anulo in alunos:
    print(anulo)


print(40*"=")
# while
from time import sleep
contador = 10
while contador > 0:
    print(contador)
    contador -=1
    sleep(0.5)
print(40*"=")

#controles de loops
#break
contador = 10
while contador > 0:
    print(contador)
    contador -=1
    if contador == 5:
        break
    sleep(0.5)
print(40*"=")
#Continue
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)
    sleep(0.5)
print(40*"=")
#Pass

for anulo in alunos:
    pass

