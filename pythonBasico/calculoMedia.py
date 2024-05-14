nota = int(input("Digite a nota do aluno: "))

if nota < 5:
    print("O aluno foi reprovado!")
elif nota < 7:
    print("O aluno está de recuperação!")
else:
    print("O aluno foi aprovado!")