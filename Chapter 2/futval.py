# A program to compute the value of an investement
# carrie 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment.")
    
    numberOfYears = eval(input("Enter the number of years for your investment: "))
    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as a decimal value: "))
    
    for i in range(numberOfYears):
        principal = principal * (1 + apr)
        
    print("The value in", numberOfYears, "years is:", round(principal, 2))
    
main()
    