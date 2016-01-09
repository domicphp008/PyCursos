
'''
          elif
A cláusula elif subistitui
um par else if

'''
minutos = int(input("Minutos utilizados: "))
if  minutos < 200:
        preço = 0.20
elif minutos <= 400:
        preço = 0.18
elif minutos <=800:
        preço = 0.15
else:
        preço = 0.08
print("Conta telefonica: R$%6.2f" % (minutos *preço))
