#print("This program illstratea a chaotic function")
#x = eval(input("Enter a number between 0 and 1: "))
#for i in range(10):
#    x = 3.9 * x * (1 - x)
#    print(x)

#Modify the expression (removed 3.9 and added 2.0)
#print("This program illstratea a chaotic function")
#x = eval(input("Enter a number between 0 and 1: "))
#for i in range(10):
#    x = 2.0 * x * (1 - x)
#    print(x)

#Modify program to print 20 lines instead of 10
#print("This program illstratea a chaotic function")
#x = eval(input("Enter a number between 0 and 1: "))
#for i in range(20):
#    x = 2.0 * x * (1 - x)
#    print(x)

#Modify program to get the number of repetitions from the user
print("This program illstratea a chaotic function")
x = eval(input("Enter a number between 0 and 1: "))
n = eval(input("Enter the number of times I should repeat: "))
for i in range(n):
    x = 2.0 * x * (1 - x)
    print(x)    