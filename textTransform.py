fileR = open('nome_base.txt', 'r')
fileW = open('novo-arquivo.txt', 'w')
lines = fileR.readlines()

count = 1

for i in lines:
    line = i.split()
    lineTransform =  line[0] + ' &  ' + line[1]
    teste = lineTransform.replace("_", "\_")
    if (count % 4 == 0):
        fileW.write(teste + ' \\' + '\\' + '\n')
    else:
        fileW.write(teste + ' & ')
    count = count + 1

fileR.close()
fileW.close()
