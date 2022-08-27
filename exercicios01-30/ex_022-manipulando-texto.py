frase = "Revendo o Curso em vídeo do Guanabara"
print(frase[19])
print(frase[28:37])
print(frase[30:50]) # anabara
print(frase[2:16:3]) # vdouo
print(frase[:3]) # Rev
print(frase[3:]) # endo o Curso em vídeo do Guanabara

print(frase[12::2]) # roe íe oGaaaa > a partir do 12, pula 1 e imprime

print(f'O tamanho da frase é : {len(frase)}') # O tamanho da frase é : 37
print(frase.count('a')) # 4
print(frase.find('deo')) # 21
print(frase.find("não existe")) # -1

print('Guanabara' in frase) # True

print(frase.upper()) # REVENDO O CURSO EM VÍDEO DO GUANABARA
print(frase.lower())
print(frase.capitalize())
print(frase.title())

frase2 = "    Aprendendo python   "
print(frase2.strip()) # Aprendendo python
print(frase2.split()) # ['Aprendendo', 'python']
print('-'.join(frase2)) #  - - - -A-p-r-e-n-d-e-n-d-o- -p-y-t-h-o-n- - - 

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sed justo justo. 
In justo neque, maximus bibendum pulvinar ut, eleifend a enim. Sed ut facilisis nisi. 
Mauris laoreet lorem eget orci congue, malesuada porta sapien dictum. 
Aliquam eros nunc, dictum vel massa finibus, sollicitudin viverra enim. 
Cras vel sem eu eros malesuada imperdiet. Aliquam erat volutpat. In id fringilla tellus. 
Quisque ullamcorper, neque ac congue dictum, enim nisi convallis est, a consequat est leo nec lorem. 
Suspendisse auctor, metus efficitur mollis tincidunt, ante ligula auctor augue, 
sit amet placerat dolor dolor vel velit. Mauris eget tortor sed lectus accumsan consectetur. 
Nulla arcu lacus, mollis sed dapibus id, convallis at nunc. 
Vivamus ligula libero, egestas ut varius in, venenatis id quam. 
Sed non ultricies urna, a lobortis purus. """)

lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sed justo justo. "

print(lorem.count('a')) # 3
