 def avalia_temperatura(a):
  if a > 30:
    return "Quente"
  elif a < 15:
    return "Frio"
  else:
    return "Agradável"


 def temperatura():
    while True:
        try:
            temp = float(input("Informe a temperatura atual: "))
            break  # Sai do loop se a entrada for um número válido
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números e quando necessário utilize ponto (.) para indicar números decimais.")
    
        ava
    
    print(f"O clima está {avalia_temperatura(temp)}")
    
# Chama a função para executar o código
temperatura()