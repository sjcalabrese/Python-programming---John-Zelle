def main():
    print("This is a program to conver the temperature from Celsius to Fehrenheit")
    print()
    print("celsius   fahrenheit")
    print("____________________")    
    for i in range(0,110,10):
        celsius = i
        fahrenheit = 9/5 * i + 32
        print("{}            {}".format(i, fahrenheit))
    input("Press the <Enter> key to quit.")

main()