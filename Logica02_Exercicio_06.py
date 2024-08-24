#Atividade 6: Somatório com While

def soma_numeros():
    soma = 0  # Variável para armazenar a soma dos números digitados
    
    while True:
        try:
            numero = float(input("Digite um número (ou 0 para encerrar): "))
            if numero == 0:
                break  # Sai do loop se o usuário digitar 0
            soma += numero  # Adiciona o número digitado à soma
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    
    print(f"A soma dos números digitados é: {soma}")

# Chama a função para executar o código
soma_numeros()

