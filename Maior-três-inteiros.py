'''
    Comentários de várias linhas com três aspas
    Faca um Programa que leia três números e mostre o maior deles.
'''
a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('terceiro: '))

if a >= b and a >= c:
    print ('O Primeiro é o maior: %d' %a)
elif b >= c:
    print ('O Segundo é o maior : %d' %b)
else:
    print ('O Terceiro é o maior : %d' %c)
    
