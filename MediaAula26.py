'''
          Listas
    Prof: Fernando masanori
     e-mail: fmasanori@gmail.com
    Aluno: Domício
     e-mail:domiciopro@gmail.com
     . Calcule a média de 5 notas
     Obs.: x += 1 é o mesmo que x = x +1
'''
notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas[x]
    x += 1
print ("Média: %5.2f" %(soma/x))    
