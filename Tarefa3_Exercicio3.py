def calcular_media_final(p1, p2, atv):
    mf = ((p1 + p2) / 2) * (0.8 + 0.04 * atv)
    return mf

def verificar_status_aluno(media_final):
    if media_final >= 7:
        return "Aprovado"
    elif 5 <= media_final < 7:
        return "Recuperação"
    else:
        return "Reprovado"

# Solicitar ao usuário o nome do aluno e as notas
nome_aluno = input("Digite o nome do aluno: ")
p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))
atv = float(input("Digite a nota da ATIV: "))

# Chamar a função para calcular a média final
media_final = calcular_media_final(p1, p2, atv)

# Chamar a função para verificar o status do aluno com base na média final
status_aluno = verificar_status_aluno(media_final)

# Imprimir o resultado
print(f"O aluno {nome_aluno} obteve média final {media_final:.2f} e está {status_aluno}.")

