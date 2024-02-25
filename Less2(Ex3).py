a = int(input("Для розв'язання рівняння введіть наступне значення: \n значення 'a': "))
b = int(input(" значення 'b' "))
c = int(input(" значення: 'c' "))
discr = b**2 - 4*a*c
x1 = (-b + discr ** 0.5)/2*a
x2 = (-b - discr ** 0.5)/2*a
print(discr)
print(x1, x2)