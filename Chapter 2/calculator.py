def main():
    print("This is a calculater, it will allow you to enter 100 expressions.")
    print("simply close the program to exit, or type an invaled mathematical expression such as dividing by 0.")
    for i in range(100):
        expression = eval(input("Please enter your mathematical expression: "))
        print(expression)
    
main()