Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = '42'
>>> type(x)
<class 'str'>
>>> y = 3
>>> type(y)
<class 'int'>
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(x+y)
TypeError: Can't convert 'int' object to str implicitly
>>> 
>>> int(x) +y
45
>>> x + str(y)
'423'
>>> 
