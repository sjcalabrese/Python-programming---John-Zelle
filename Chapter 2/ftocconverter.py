def main():
    print("This program converts the temperature from Fehrenheit to Celsius")
    print("and prints is out in a table from 0 - 100 by 10 degree intervals")
    print()
    print("fahrenheit   celsius")
    print("____________________")    
    for i in range(0,110,10):
        fahrrenheit = i
        fahrenheit = (i - 32) * 9/5 
        print("{}            {}".format(i, fahrenheit))
    input("Press the <Enter> key to quit.")

main()