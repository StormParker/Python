Python 3.3.4 (v3.3.4:7ff62415e426, Feb 10 2014, 18:12:08) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def my_function(x="default text"):
	print(x)
>>> my_function("two")
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> def my_function(x="default text"):
	print(x)

	
>>> my_function("two")
two
>>> my_function("3")
3
>>> my_function()
default text
>>> 
