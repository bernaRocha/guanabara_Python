from os import system

system('clear')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

if media < 3:
    print(f'Com a média {media:.1f} o aluno está reprovado.')
elif media <= 7:
    print(f'Com a média {media:.1f} o aluno está em recuperação.')
else:
    print(f'Com a média {media:.1f} o aluno está APROVADO.')
    