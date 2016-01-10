'''
    A seguencia de Fibonacci é a seguinte:
         1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
    Sua regra de formação é simples: os dois primeiros elementos são 1;
    a partir de então, cada elemento é a soma dos dois anteriores.
    Faç um algoritmo que leia um número inteiro calcule o seu número
    de Fibonacci. F(1) = 1, F(2) = 1, F(3) = 2, F(4) = 3, etc.
    Youtube -> Nature by Numbers
'''
n = int(input('N: '))
a, b = 1,1
k = 1
while k <= n - 2:
    a, b = b, a + b
    k = k + 1
print ('Fib(%d) = %d' %(n, b))    
