# Liczby są niezmienne - immutable
digit = 50
print(float(digit))
print(type(digit))
digit = float(digit)
# Strings sa niezmienne - immutable
name = "John"
print(name + " Doe")
print(name)
name = name + "Doe"
print(name)
# String można wycinac
print(len(name))
# od 1 do 7 
print(name[0:7]) # ohnDoe
# JohnDoe
# 0123456
# Wycinanie dziala w taki sposob 0 poczatek - ostatni index + 1 
print(name[0:4]) # John
print(name[0:7:2]) # wycinanie za pomoca okreslonego kroku 
print(name[3:-1]) # -1 weź ostatni element 
print(name[0])
print(name[-1])
# print(name[1000])

error_text = "ERROR: TEST1"
new_text = error_text[7:]
print(new_text)
