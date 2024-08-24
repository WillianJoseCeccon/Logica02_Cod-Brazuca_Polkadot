#Atividade 8: Criando Funções
#Atividade Prática: Escreva uma função que receba um número e retorne se ele é par ou ímpar

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

def obter_numero_inteiro():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero  # Retorna o número se a conversão for bem-sucedida
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")

# Exemplo de uso da função
numero = obter_numero_inteiro()
resultado = par_ou_impar(numero)
print(f"O número {numero} é {resultado}.")