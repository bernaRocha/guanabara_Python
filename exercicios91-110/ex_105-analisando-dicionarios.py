'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
from os import system
system('clear')

def notas(*n, situacao=False):
    '''
    Função para analisar notas e situações dos alunos.
    :param n: uma ou mais notas
    :param situacao: opcional se indica ounão a situação do aluno
    :return: dicionário com as informações geradas
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)

    if situacao:
        if r['média'] >= 7:
            r['situação'] = 'Aprovado'
        elif r['média'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r


resposta = notas(6,7,8,4.5, situacao=True)
print((resposta))
## {'total': 4, 'maior': 8, 'menor': 4.5, 'média': 6.375, 'situação': 'Razoável'}
