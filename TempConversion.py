def Cel_To_Fahren(num):
    return (num*9/5)+32
def Fahren_To_Cel(num):
    return (num-32)*5/9


print("\n*****Welcome To Temparature Converter Program****")
while True:
    print("\n1.Celsius To Fahrenheit\n2.Fahrenheit To Celsius\n3.Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        num = float(input("Enter the Temparature in Celsius: "))
        fahren = Cel_To_Fahren(num)
        print(f"{num}\u00B0C = {fahren:.2f}\u00B0F")
    elif choice == 2:
        num = float(input("Enter the Temparature in Fahrenheit: "))
        cels = Fahren_To_Cel(num)
        print(f"{num}\u00B0F = {cels:.2f}\u00B0C")
    elif choice == 3:
        exit(0)
    else:
        print("\nInvalid Choice!!!!")
