file_opened = open("input", 'r')
lines = file_opened.readlines()
lista = []
for line in lines:
    var = int(line)
    for element in lista:
        if var + element == 2020:
            print(var*element)
            break
    lista.append(var)

    