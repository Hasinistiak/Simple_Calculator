#Calculater

print('Welcome To My Calculater')
Choose_Calc_nums = int(input('Enter How many numbers you want to calculate: '))

#2 Number equation
if Choose_Calc_nums == 2:
    
    Num_1 = int(input('Enter first Number: '))
    Num_2 = int(input('Enter Second Number: '))


    Operators = ("+(plus) -(minus) *(multiplication) /(division")
    
    Choose_oprerator = input("Choose an operator: ")
    
    if Choose_oprerator == '+':
        print(Num_1 + Num_2)

    elif Choose_oprerator == '-':
        print(Num_1 - Num_2)

    elif Choose_oprerator == '.':
        print(Num_1 * Num_2)

    elif Choose_oprerator == '/':
        print(Num_1 / Num_2)

    else:
        print("Something Went Wrong!!!")


#3 Number equation
if Choose_Calc_nums == 3:
    Num_1 = int(input('Enter first Number: '))
    Num_2 = int(input('Enter Second Number: '))
    Num_3 = int(input('Enter Third Number: '))


    Operators = ("+(plus) -(minus) *(multiplication) /(division")
        
    Choose_oprerator = input("Choose an operator: ")
        
    if Choose_oprerator == '+':
        print(Num_1 + Num_2 + Num_3)

    elif Choose_oprerator == '-':
        print(Num_1 - Num_2 - Num_3)

    elif Choose_oprerator == '.':
        print(Num_1 * Num_2 * Num_3)

    elif Choose_oprerator == '/':
        print(Num_1 / Num_2 / Num_3)

    else:
        print("Something Went Wrong!!!")
print('Program Finished')