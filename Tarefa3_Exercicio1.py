import math

def calcular_raiz(numero):
    if numero >= 0:
        raiz = math.sqrt(numero)
        return raiz
    else:
        return "Não é possível calcular a raiz de um número negativo."

# Solicitar ao usuário um número para calcular a raiz
numero_input = float(input("Digite um número para calcular a raiz: "))

# Chamar a função para calcular a raiz e imprimir o resultado
resultado = calcular_raiz(numero_input)
print("A raiz quadrada de", numero_input, "é", resultado)
