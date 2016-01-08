v = int(input("velocidade: "))
if v > 110:
    print ("Você foi multado!")
    multa = (v-110) *5
    print ("Valor da multa: R$ %5.2f" %multa)
