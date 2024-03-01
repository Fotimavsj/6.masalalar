# ## 6.1
# X = float(input("X="))
# Y = float(input("Y="))
# if X > Y:
#     print("X:",X)
# else:
#     print("Y:", Y)


# ## 6.1
# X = float(input("X="))
# Y = float(input("Y="))
# if X < Y:
#     print("X:",X)
# else:
#     print("Y:",Y)


# ## 6.2
# X = float(input("X="))
# Y = float(input("Y="))
# Z = float(input("Z="))
# if X > Y and X > Z:
#     print("X:",X)
# else:
#     print("Max qiymat toplmadi")
# if Y > Z and Y > X:
#     print("Y:",Y)
# else:
#     print("Max qiymat toplmadi")
# if Z > X and Z > Y:
#     print(Z,"Z:")
# else:
#     print("Max qiymat toplmadi")


# ## 6.3
# X = float(input("X="))
# Y = float(input("Y="))
# Z = float(input("Z="))
# a = X + Y + Z
# b = X * Y * Z
# if a > b:
#     print("A:",a)
# else:
#     print("B:",b)


# ## 6.3
# X = float(input("X="))
# Y = float(input("Y="))
# Z = float(input("Z="))
# a = (X + Y + Z)/2
# b = X * Y * Z
# if a < b:
#     print("A:",a  2 + 1)
# elif b < a:
#     print("B:",b  2 + 1)


# ## 6.4
# a = float(input("A:"))
# b = float(input("B:"))
# c = float(input("C:"))
# if a > b and b > c:
#     print("Qanoatlantiradi")
# else:
#     print("Qanoatlantirmaydi")


# ## 6.5
# a = float(input("A:"))
# b = float(input("B:"))
# c = float(input("C:"))
# if a >= b >= c:
#     print(a * 2,b * 2,c * 2)
# else:
#     print(a * -1,b * -1,c * -1)


# ## 6.6
# x = float(input("x="))
# y = float(input("y="))
# if x > y:
#     print("z:",x - y)
# else:
#     print("z:",y - x + 1)


# ## 6.7

# a = float(input("a="))
# b = float(input("b="))
# if a > b:
#     print("a=",a)
# else:
#     print("a=", a , "b=",b)


# ##6.8
# a = float(input("a="))
# b = float(input("b="))
# if a <= b:
#     print("a:",a*0)
# else:
#     print("a=",a,"b=",b)


# ## 6.9
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# if 1 < a and  b and c < 3:
#     print("True")
# else:
#     print("False")


# ##6.10
# x = float(input("x="))
# y = float(input("y="))
# if x < y:
#     x = (x + y)/2
#     print("x:",x)
# else:
#     y = (x * y)*2
#     print("y:",y)



# ## 6.11
# x = float(input("x:"))
# y = float(input("y:"))
# z = float(input("z:"))
# if x > 0:
#     print(x  2)
# elif x == 0:
#     print("Nolga teng")
# else:
#     print("Manfiy qiymat")
# if y > 0:
#     print(y  2)
# elif y == 0:
#     print("Nolga teng")
# else:
#     print("Manfiy qiymat")
# if z > 0:
#     print(z  2)
# elif z == 0:
#     print("Nolga teng")
# else:
#     print("Manfiy qiymat")





# ## 6.12
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# d = float(input("d="))
# if d >= c >= b >= a:
#     print("d:",d,"c:",d,"b:",d,"a:",d)
# elif a > b > c > d:
#     print("a:",a,"b:",b,"c:",c,"d:",d)
# else:
#     print((a  2),(b  2),(c  2),(d  2))





# ## 6.13
# from math import *
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# D = (b  2) - 4 * a * c
# if a == 0:
#     print("Chiziqli algaritm")
# if D < 0 :
#     print("Yechimga ega emmas")
# elif D == 0:
#     x1 = (-b)/(2 * a)
#     x2 = x1
#     print("x1:",x1,"x2:",x2)
# else:
#     x1 = ((-b + sqrt(D))/(2 * a))
#     x2 = ((-b - sqrt(D))/(2 * a))
#     print("x:",x1,"x2",x2)


# ## 6.14
# x=int(input("x="))
# y=int(input("y="))

# a=int(input("a ni kiriting:"))
# b=int(input("b ni kiriting:"))
# c=int(input("c ni kiriting:"))

# if (x>=a or x>=b or x>=c) and( y>=a or y>=b or y>=c):
#     print(" sigadi")

# else:
#     print("sigmaydi")