def criar_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Solicitar ao usuário o número para a tabuada
numero_tabuada = int(input("Digite um número para ver a tabuada: "))

# Chamar a função para criar a tabuada
criar_tabuada(numero_tabuada)
