import math

print("Die Gleichung ax^2+bx+c=0 wird nach x gelöst, geben sie dafür die folgenden Parameter an: ")

a = float(input("Geben Sie den Wert für 'a' an: "))
b = float(input("Geben Sie den Wert für 'b' an: "))
c = float(input("Geben Sie den Wert für 'c' an: "))
print()
print("Die quadratische Funktion lautet: ",math.sqrt(a),"*x^2",b,"*x",c)
print()
print("Die Gleichung g(x)= m*x+n wird hergeleitet!")
print()
m = float(input("Geben Sie den Wert für 'm' ein: "))
n = float(input("Geben Sie von Wert für 'n' ein: "))
print()
print("Die lineare Funktion lautet: ",m,"*x+",n)
print()
print("Die Schnittstelle der quadratischen und linearen Funktion wird nun ermittelt!")
print("Nach Umstellen und Substitution der Gleichungen, lautut die Funktion zur Berechnung der Schnittstelle einer quadratischen und linearen Funktion nun ax^2+gx+d=0, webei d = c - n und g = b - m ")
d = c - n
g = b - m
print()
if a == 0 and g == 0 and d == 0:
    x = 0
    y = m * x + n
    print("Der Schnittpunkt von f(x) und g(x) liegt bei Schnittpunkt S", "(", x,"/", y, ")")

elif a == 0 and g == 0:
    x = d
    y = m * x + n
    print("Der Schnittpunkt von f(x) und g(x) liegt bei Schnittpunkt S", "(", x,"/", y, ")")

elif a == 0:
    x: float = - d / g
    y_1 = m * x + n
    print("Der Schnittpunkt von f(x) und g(x) liegt bei Schnittpunkt S", "(", x,"/", y_1, ")")

elif g == 0:
    print("Es gibt kein Ergebisse , da die keine negativen Wurzeln gezogen werden könnnen!")

elif d == 0:
    x_1: float = -g / a
    x_2 = 0
    y_1 = m * x_1 + n
    y_2 = n
    print("Der Schnittpunkt von f(x) und g(x) liegt bei Schnittpunkt S", "(", x_1, "/",y_1,")","und","(",x_2,"/",y_2,")")

else:
    alpha: float = g * g - 4.0 * a * d
    if alpha < 0:
        print("Wurzel kann nicht negativ werden, eingegebene Werte sind falsch!")
    else:
        x_ergebnis_1: float = (-g + math.sqrt(alpha)) / (2 * a)
        x_ergebnis_2: float = (-g - math.sqrt(alpha)) / (2 * a)
        print("x_1 =", x_ergebnis_1)
        print("x_2 =", x_ergebnis_2)

        y_1 = m * x_ergebnis_1 + n
        y_2 = m * x_ergebnis_2 + n
        print()
        print("Der Schnittpunkt von f(x) und g(x) liegt beim Schnittpunkt S_1", "(", x_ergebnis_1, "/",y_1, ")", "und s_2","(", x_ergebnis_2, "/", y_2,")")
