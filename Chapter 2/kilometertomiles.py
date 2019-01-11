def main():
    print("This program converts Kilometers into Miles")
    
    kilometers = eval(input("Please enter the distance in kilometers: "))
    miles = kilometers * .62
    
    print(kilometers, "kilometer equals", miles, "miles")
    input("Press the <Enter> key to quit.")

main()