number=int(input("Enter a number to find its factorial :"))


def fact(number):
   if number<=1:
    return 1

   else:
     return number*fact((number-1))

print("Factorial  is", fact(number))


