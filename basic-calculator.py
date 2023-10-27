# FUNCTIONS
def add(x,y):
    result =  x + y
    print("The Answer is : ", result)
def sub(x,y):
    result = x - y
    print("The Answer is : ", result)

def mul(x,y):
    result =  x * y
    print("The Answer is : ", result)

def div(x,y):
    result = x / y
    print("The Answer is : ", result)



# keep running code until exit
while(True):
    print("========================================================")
    # Choices
    print("What Operation do you want to do?")
    print("1. Addtion")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = int(input("Please Select your choice : "))


    if choice == 1:
        print("========================================================")

        first_number = int(input("Please enter your first number : "))
        second_number = int(input("Please enter your second number : "))

        print("========================================================")
        add(first_number, second_number) 

    elif choice == 2:
        print("========================================================")

        first_number = int(input("Please enter your first number : "))
        second_number = int(input("Please enter your second number : "))

        print("========================================================")
        sub(first_number, second_number)
        
    elif choice == 3:
        print("========================================================")

        first_number = int(input("Please enter your first number : "))
        second_number = int(input("Please enter your second number : "))

        print("========================================================")
        mul(first_number, second_number)
        
    elif choice == 4:
        print("========================================================")

        first_number = int(input("Please enter your first number : "))
        second_number = int(input("Please enter your second number : "))

        print("========================================================")
        div(first_number, second_number)
        
    elif choice == 5:
        print("You quit the Program!!!")
        quit()
