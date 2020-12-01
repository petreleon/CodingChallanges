file_opened = open("input", 'r')
lines = file_opened.readlines()
lista = []
for line in lines:
    var = int(line)
    lista.append(var)

for a in range(len(lista)):
    for b in range(a+1,len(lista)):
        if lista[a]+lista[b]<2020:
            for c in range(b+1,len(lista)):
                if(lista[a]+lista[b]+lista[c]==2020):
                    print(lista[a]*lista[b]*lista[c])
                    break
