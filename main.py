# Bartosz Różycki
# numer indeksu: 255740

from Fraction import *

print("---Tworzenie ułamków---")
print("--a = Fraction(0,3)--")
a = Fraction(1,5)
print(a)
a.float_disallow()
try:
    print("--b = Fraction(2.5,7.5)--")
    b = Fraction(2.5,7.5)
except Exception:
    print("--Należy włączyć możliwość tworzenia ułamków z liczb zmiennoprzecinkowych.--")
    print("--a.float_allow()--")
    a.float_allow()
    print("--b = Fraction(2.5,7.5)--")
    b = Fraction(2.5,7.5)
print(b)
print("")

############################################
print("---Działania na ułamkach---")
a = Fraction(2,10)
b = Fraction(2.5, 7.5)
print(f"a = {a}, b = {b}")

print("--Dodawanie--")
print(a, "+", b)
print(a+b)
print(a, "+", 5)
print(a+5)
print(a, "+", 1.5)
print(a+1.5)
print(1.5, "+", b)
print(1.5+b)
print("")

print("--Odejmowanie--")
print(a, "-", b)
print(a-b)
print(a, "-", 5)
print(a-5)
print(a, "-", 1.5)
print(a-1.5)
print(1.5, "-", b)
print(1.5-b)
print("")

print("--Mnożenie--")
print(a, "*", b)
print(a*b)
print(a, "*", 5)
print(a*5)
print(a, "*", 1.5)
print(a*1.5)
print(1.5, "*", b)
print(1.5*b)
print("")

print("--Dzielenie--")
print(a, "/", b)
print(a/b)
print(a, "/", 5)
print(a/5)
print(a, "/", 1.5)
print(a/1.5)
print(1.5, "/", b)
print(1.5/b)
try:
    c = Fraction(0, 3)
    print(a, "/", c)
    print(a/c)
except ZeroDivisionError:
    print("Wyłapano i udaremniono próbę podzielenia przez 0.")
print("")

################################
print("---Porównywanie---")
a = Fraction(-2,10)
b = Fraction(2.5, 7.5)
print(f"a = {a}, b = {b}")
print("")

print(a, "<", b)
print(a<b)
print(a, "<", -1/5)
print(a<-1/5)
print("")

print(a, "<=", b)
print(a<=b)
print(a, "<=", -1/5)
print(a<=-1/5)
print("")

print(a, ">", b)
print(a>b)
print(a, ">", -0.19)
print(a>-0.19)
print("")

print(a, ">=", b)
print(a>=b)
print(1/3, ">=", b)
print(1/3>=b)
print("")

print(a, "==", a)
print(a==a)
print(a, "==", -0.2)
print(a==-0.2)
print(a, "==", -0.19)
print(a==-0.19)

print(b, "==", b)
print(b==b)
print(b, "==", 1/3)
print(b==1/3)
print(b, "==", 0.333333)
print(b==0.333333)
print("")

################################
print("---Inne działania---")
a = Fraction(-2,10)
print(f"a = {a}")
print("")

print("a.get_num()")
print(a.get_num())
print("a.get_denom()")
print(a.get_denom())
print("")

print(f"abs({a})")
print(abs(a))
print("")

print(f"int({a})")
print(int(a))
print("")

print(f"float({a})")
print(float(a))
print("")

#################################
print("---Widok liczby mieszanej---")
a = Fraction(15, 7)
b = Fraction(30, 14)
c = Fraction(7.5, 3.5)

print("Improper:")
print(f"a = Fraction(15, 7) = {a}")
print(f"b = Fraction(30, 14) = {b}")
print(f"a = Fraction(7.5, 3.5) = {c}")
print("")
a.display_mixed()
print("Mixed:")
print(f"a = Fraction(15, 7) = {a}")
print(f"b = Fraction(30, 14) = {b}")
print(f"a = Fraction(7.5, 3.5) = {c}")
print("")







