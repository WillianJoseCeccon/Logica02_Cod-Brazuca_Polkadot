#Atividade 10: Números Primos
#Atividade Prática:
#Crie um programa que encontre e imprima todos os números primos em um intervalo definido pelo usuário.

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):
        if eh_primo(num):
            primos.append(num)
    return primos

# Exemplo de uso do programa
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

primos = encontrar_primos(inicio, fim)

if primos:
    print(f"Números primos entre {inicio} e {fim}: {primos}")
else:
    print(f"Não há números primos no intervalo de {inicio} a {fim}.")