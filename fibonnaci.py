
number=int(input("Enter no of digits in series:"))

def fibonnaci(number):

        a = 0
        b = 1
        print(a)
        print(b)
        while(number-3>=0):
            c=a+b
            print(c)
            a=b
            b=c
            number-=1


fibonnaci(number)

