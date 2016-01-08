Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ('Alô') # isto é o meu primeiro programa
Alô
>>> #calcular quantos dígitos tem 2 ** 1000000
>>> 2 ** 10
1024
>>> 2 ** 100
1267650600228229401496703205376
>>> a - str ('1267650600228229401496703205376')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a - str ('1267650600228229401496703205376')
NameError: name 'a' is not defined
>>> a = str ('1267650600228229401496703205376')
>>> len(a)
31
>>> a = str(2 ** 1000000)
>>> len(a)
301030
>>> 
