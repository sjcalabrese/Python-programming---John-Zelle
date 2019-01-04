def main():
    print("This is a program to conver the temperature from Celsius to Fehrenheit")
    celsius = eval(input("What is the Cellsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")

main()