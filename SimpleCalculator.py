while True:
    print("> This is a simple calculator")
    print("")
    print("> Choose 1 to make calculation")
    print("> Choose 2 to read the file")
    print("> Choose 3 to exit the calculator")
    print("")

    user_option = input("Enter your choice from 1, 2, 3:\n> ")

    if user_option == "1":
        number1 = input("Enter the first number:\n> ")
        operator = input("Enter an operator + - / *:\n> ")
        number2 = input("Enter the second number:\n> ")       

        try:
            x = float(number1)
            y = float(number2)

            if operator == "+":
                equ1 = x + y
                print(f"{x} + {y} = {equ1}") #this will print the result to the equation
                print("")
                equation1 = "x + y"  #writing the equation string to the to the txt file individually
                with open('equation1.txt', 'w') as f:
                    f.write(equation1)   

            elif operator == "*":
                equ2 = x * y
                print(f"{x} * {y} = {equ2}")
                print("")
                equation2 = "x * y"
                with open('equation2.txt', 'w') as f:
                    f.write(equation2)  

            elif operator =="/":
                try:                             #defensive programming to detect zero divison error
                    equ3 = x / y
                    print(f"{x} / {y} = {equ3}")
                    print("")
                    equation3 = "x / y"
                    with open('equation3.txt', 'w') as f:
                        f.write(equation3)

                except ZeroDivisionError:
                    print("Numbers cannot be divided by zero") 

            elif operator == "-":
                equ4 = x - y
                print(f"{x} - {y} = {equ4}")
                print("")
                equation4 = " x - y"
                with open('equation4.txt', 'w') as f:
                    f.write(equation4)
                        
            else:
                print("You have entered a wrong operator, try again")
                print("")
        
        except ValueError:
            print("Value Error, please enter a valid number")
            print("")

    elif user_option == "2":
        while True:

            text_file_name = input("Enter the text file name you wish to access:\n> ")
            try:
                number1 = int(input("Enter the first number:\n> "))
                number2 = int(input("Enter the second number:\n> ")) 
                x = number1
                y = number2   

                equation1 = x + y
                equation2 = x * y
                equation3 = x / y
                equation4 = x - y 

                with open(text_file_name, 'w') as f:  #writing multiple equations in the same line
                    f.write("x + y\n")
                    f.write("x * y \n")
                    f.write("x / y \n")
                    f.write("x - y \n")    
                                          #note that i have written the equation in strings to avoid a synthax error while evaluating
                f.close() 

                try:                  
                    with open(text_file_name, 'r') as f:
                        equations = f.readlines() 
                        for equation in equations:     #the for function reads each equation in each line and then evaluate
                            result = eval(equation)
                            print(f"{equation} = {result}") 
                    break

                except FileNotFoundError:
                    print(f"{text_file_name} file not found")
                    continue
        
                    
            except ZeroDivisionError:
                print("Numbers cannot be divided by zero")
                print("")

    elif user_option == "3":
        exit()

    else:
        print("Invalid option try again")
        print("")



