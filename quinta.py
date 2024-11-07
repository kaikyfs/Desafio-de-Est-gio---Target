entrada = input("Digite a string que sera invertida: ")

invertida = ""

#Vamos percorrer a string de tras para frente
for i in range(len(entrada) -1, -1, -1):
    invertida += entrada[i]


print("String invertida: ", invertida )