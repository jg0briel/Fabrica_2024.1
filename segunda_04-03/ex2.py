#ex2
#Faça a média aritmetica de 5 alunos 

nota = 0
alunos = 0
while(alunos < 5):

    aluno = int(input("Digite seu média: "))
    nota = nota + aluno
    alunos = alunos + 1

media = nota/5
print(f"A média aritmetica é: {media}")
