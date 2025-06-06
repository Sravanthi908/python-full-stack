import fcalculator
num_1 = int(input())
while True:
    op = input()
    if op == "=":
        print ("end of calculation result =", num_1)
        break
    num_2 = int (input())
    if op =="+":
        num_1 = fcalculator.add (num_1 , num_2)
    elif op == "-":
        num_1 = fcalculator.sub (num_1 , num_2)
    elif op == "*":
        num_1 = fcalculator.mul (num_1 , num_2)
    elif op == "/":
        num_1 = fcalculator.div (num_1 , num_2)
    elif op == "**":
        num_1 = fcalculator.pow (num_1 , num_2)
    elif op == "%":
        num_1 = fcalculator.mod (num_1 , num_2)
    print (num_1)        

