import json

def calcular_faturamento (dados_faturamento):
    #armazenando apenas oa valoresmaiores que 0
    faturamento = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]

    #calculando maior e menor faturamento
    maior_faturamento = max (faturamento)
    menor_faturamento = min (faturamento)

    media = sum (faturamento) / len (faturamento)

    #Verifica os dias acima da media
    dias = 0
    for valor in faturamento:
        if valor > media:
            dias += 1

    return maior_faturamento, menor_faturamento, dias

#Ler o arquivo
with open('faturamento.json', 'r') as file:
    dados_faturamento = json.load(file)


#Calculos
maior, menor, dias = calcular_faturamento(dados_faturamento)


#Resultados
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias}")