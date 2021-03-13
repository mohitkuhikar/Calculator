def intro ():

    print ("\nHelp:-")

    print ("Type '+' for addition")

    print ("Type '-' for subtraction")

    print ("Type '*' for multiplication")

    print ("Type '/' for division")

    return

    

    

def calculate ():

    operation = str(input ("Type Operation method:- "))

    value1 = int(input ("Value 1 > "))

    value2 = int(input ("Value 2 > "))

    

    if operation == "+":

        solution = value1 + value2

        print (solution)

        

    if operation == "-":

        solution = value1 - value2

        print (solution)

        

    if operation == "*":

        solution = value1 * value2

        print (solution)

        

    if operation == "/":

        solution = value1 / value2

        print (solution)

   

   

intro ()

calculate ()
