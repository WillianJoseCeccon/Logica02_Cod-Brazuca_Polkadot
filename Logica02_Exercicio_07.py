#Atividade 7: Trabalhando com Listas


def lista_de_compras():
    lista = []  # Inicializa a lista vazia
    
    while True:
        item = input("Digite um item para adicionar à lista de compras (ou 0 (zero) para encerrar): ")
        if item == '0':
            break  # Sai do loop se o usuário digitar 'sair'
        lista.append(item)  # Adiciona o item à lista
    
    print("\nLista de Compras:")
    for i, item in enumerate(lista, start=1):
        print(f"{i}. {item}")

# Chama a função para executar o código
lista_de_compras()