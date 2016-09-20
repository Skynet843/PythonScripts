# BMI calculator :)

def BMI_calculator(k,m):

    BMI = k / ( m * m )
    print 'Your BMI is ' ,BMI
    print '\n'

    # the under this comments upon your weight
    if BMI  <= 18.5:
        print "You are underweight you need to put on some weight"

    elif 18.5 < BMI <=25:

      print "you are normal"

    elif 25< BMI < 30 :
        print "You are over weighted person , you need to loose some weight"

    elif BMI >= 30:
        print "you are heavy Weighted person , you need to loose some weight"

 # Collects data from user , converts data into float and enters data into the function(BMI_calculator)

w= raw_input('Enter your weight in kg :')
h= raw_input('Enter your height in metres:')
weight= float(w)
height= float(h)

BMI_calculator(weight,height)

