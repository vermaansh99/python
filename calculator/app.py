class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print(self.num1+self.num2)
    
    def subtraction(self):
        print(self.num1-self.num2)

    def multiplication(self):
        print(self.num1*self.num2)

    def division(self):
        print(self.num1/self.num2)



while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = int(input("Enter your choice: "))
    num1 = int(input("Number 1"))
    num2 = int(input("Number 2"))
    calculator = Calculator(num1,num2)
    
    if choice == 1:
        calculator.addition()
    elif choice == 2:
        calculator.subtraction()
    elif choice == 3:
        calculator.multiplication()
    elif choice == 4:
        calculator.division()
    elif choice == 5:
        break
    else:
        print("Invalid choice")