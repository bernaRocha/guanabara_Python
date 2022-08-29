from os import system

system('clear')

for n in range(2, 51, 2): # De 2 até 51 pulando de dois em dois
    if n % 2 == 0: 
        print(n, end=" ")
print('Fim')