def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero"

def resultados():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            break  # Sai do loop se a entrada for um número válido
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
    
    while True:
        try:
            numero2 = float(input("Digite o segundo número: "))
            break  # Sai do loop se a entrada for um número válido
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")
    
    print(f"Soma: {soma(numero1, numero2)}")
    print(f"Subtração: {subtracao(numero1, numero2)}")
    print(f"Multiplicação: {multiplicacao(numero1, numero2)}")
    print(f"Divisão: {divisao(numero1, numero2)}")

# Chama a função para executar o código
resultados()