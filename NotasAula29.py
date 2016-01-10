'''
          Listas
    Prof: Fernando masanori
     e-mail: fmasanori@gmail.com
    Aluno: Domício
     e-mail:domiciopro@gmail.com
     .Faça um programa que leia quarto notas,
     mostre as notas e a média na tela
     
'''
notas = []
soma = 0
i = 1
while i <= 4:
    n = float(input("Nota: "))
    notas.append(n)
    soma += n
    i += 1
print ("Notas:", notas)
print ("Média: %4.2f" %(soma/4))
    
