try:
    n1 = int(input("enter first number : "))
    n2 = int(input("enter second number : "))    
    print(n1/n2)

except (ValueError, ZeroDivisionError) as err:
    print("invalid input")
    print(err)

