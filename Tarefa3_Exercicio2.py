def verificar_tipo_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Triângulo Equilátero"
        elif a == b or a == c or b == c:
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"
    else:
        return "Não é um triângulo válido"

# Solicitar ao usuário os comprimentos dos lados
a = float(input("Digite o comprimento do primeiro lado: "))
b = float(input("Digite o comprimento do segundo lado: "))
c = float(input("Digite o comprimento do terceiro lado: "))

# Chamar a função para verificar o tipo de triângulo e imprimir o resultado
tipo_triangulo = verificar_tipo_triangulo(a, b, c)
print("O triângulo é:", tipo_triangulo)
