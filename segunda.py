def fibonacci (numero):
    #Iniciado os dois primeiros valores da sequencia
    a, b= 0, 1
    while a <= numero:
        if a == numero:
            return True #Número pertence a sequencia
        a, b = b, a + b #Atualiza os valores
    return False #Numero não pertecen a sequencia


numero = int(input("Digite o número: ")) #Entrada para o numero

if fibonacci (numero):
    print(f"O numero {numero} pertence a sequencia de Fibonacci.")
else:
    print(f"O numero {numero} nao pertence a sequencia de Fibonacci")