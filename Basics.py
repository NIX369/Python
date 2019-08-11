# area of circle

# radius = int(input("Enter the radius "))
# area = 3.142*radius**2
# print("Area of circle is",area)
# format method
# print("Area of Circle is {0}".format(area))
# f-string method
# print(f"Area of circle is {area}")

# IF Statement

# age = int(input("Enter your age "))
# if age > 18:
#   print("You can vote ")
# else:
#   print("You cannot vote "
#        "Wait ",18-age," Years to vote")
# FOR Loop

# ninjas=["Micheal","leo","Raphael","Don"]
# for ninja in ninjas[1:3]:
#   print(ninja)

# WHILE Loop
# a=10
# b=0
# while(b<a):
#   print("Hello")
#   b+=1

# Ranges
# for n in range(5):
#    print(n)

# FUNCTIONS

def area(radius):
    ar = 3.14 * radius ** 2
    return ar


def vol(length, area):
    volume = area * length
    print(volume)


rad = int(input("ENter the radius of circle "))
len = int(input("Enter length "))
#calc = area(rad)
vol(area(rad), len)
