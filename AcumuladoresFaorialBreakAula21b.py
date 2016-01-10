'''
      Acumuladores
 Calcule a soma de números inteiros até ser
 digitado zero
'''
soma = 0
while True:
    x = int(input("Digite o número (0 sai): "))
    if x == 0:
        break
    soma = soma + x
print ("Soma: %d" %soma)    
