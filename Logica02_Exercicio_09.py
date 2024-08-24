#Atividade 9: Manipulação de Strings

#Atividade Prática:
#Escreva um programa que peça uma frase ao usuário e conte quantas vezes uma letra específica aparece.

def conta_letra(frase, letra):
    return frase.lower().count(letra.lower())


frase = input("Digite a frase desejada: ")
letra = input("Digite uma letra para contatabilizar a quantidade de vezes que ela aparece na frase: ")

quantidade = conta_letra(frase, letra)

print(f"A letra '{letra}' aparece {quantidade} vez(es) na frase.")