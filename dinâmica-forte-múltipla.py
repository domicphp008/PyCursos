Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 42
>>> b = 13
>>> a > b
True
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> a < b
False
>>> a == 42
True
>>> b == 42
False
>>> b
13
>>> b = 42
>>> b
42
>>> a!= 13
True
>>> a
42
>>> nota = 7
>>> faltas = 30
>>> nota >= 6 and faltas <= 20
False
>>> a
42
>>> b
42
>>> a == 42 or b == 42
True
>>> a = 13
>>> a == 42 or b == 42
True
>>> b =13
>>> a == 42 or b == 42
False
>>> print ( ' O número é  42 )
	
SyntaxError: EOL while scanning string literal
>>> print ( ' O número é  42 ')
 O número é  42 
>>> # Obs: um erro acima e foi corrigido !
>>> print (' O número' , a, 'é muito legal')
 O número 13 é muito legal
>>> # Usando marcador
>>> print (' O número %d é muito legal' %a)
 O número 13 é muito legal
>>> a = 'abacate'
>>> print ('Uma fruta muito gostosa é o %s. Na opinião do Massa' %a)
Uma fruta muito gostosa é o abacate. Na opinião do Massa
>>> a = 3.1415
>>> print ('Pi é %f' %a)
Pi é 3.141500
>>> print ('Pi com duas casas %.2f' %a)
Pi com duas casas 3.14
>>> 

>>> a = 'abacate'
>>> a = 42
>>> a
42
>>> str(42) + 'mamão'
'42mamão'
>>> a
42
>>> b
13
>>> a, b = b, a
>>> a
13
>>> b
42
>>> a, , c = 1, 2, 3
SyntaxError: invalid syntax
>>> a, b, c = 1, 2, 3
>>> a
1
>>> b
2
>>> c
3
>>> a, b, c = 'OBA'
>>> a
'O'
>>> b
'B'
>>> c
'A'
>>> 
