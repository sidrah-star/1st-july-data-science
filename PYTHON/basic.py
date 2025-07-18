#print("Hello world")
#>>>>>list<<<<<
#lst = [1,2,3,4,5,6,7,2.3,]
#print(lst) 
#lst.reverse()
#print(lst)
#lst.remove(2.3)
#print(lst)
#lst.sort()
#print(lst)
#print(lst.count(2))
#print(lst)

#>>>>>tuple<<<<
#tpl = (1,2,3,5,585,5, "ritik", 2.3)
#print("my first tuple :", tpl)
#print("len of tuples: ", len(tpl))
#print("type of tuple: ",type(tpl))

#print(tpl[0])
#print(tpl[2])
#print(tpl[0:6])
#build

#a = 1,2,58,5,58,5,5,85,2
#print(a)
#print(type(a)) ## <class 'tuple'>
#print(len(a))  ##9

#a, b, c =(1,2,3)
#print(a)
#print(b)
#print(c)
#a,b,c = 1,2,3
#print(a)
#print(b)
#print(c)

#tpl = (1,2,58,2,8,2,8)
#print("max of tuple",max(tpl))
#print("min of tuple:",min(tpl))
#print("sum of tuple:",sum(tpl))

#>>>>>dict<<<<<
#my_dict = {
    #"name":"Sidra",
    # "class": "3rd yr",
    #"Roll no": "2022297",
    #"Adress": "dehradun","name": "Sidra"
#}
##print("my first dict: ",my_dict)
#print("len of dict: ",len(my_dict))
##print("type of dict: ",type(my_dict))
##print(my_dict['name'])
#print(my_dict['class'])
#print(my_dict['Adress'])
#my_dict['Adress'] = "Mumbai"
#print(my_dict)
#my_dict = {
    #"name":"Sidra", ##name, ckass, roll no and adress>>>>keys
    # "class": "3rd yr", #sidra,2nd yr, 2022297 and mumbai >>>values
    #"Roll no": "2022297",
    #"Adress": "dehradun","name": "Sidra" ###>>
#}
#my_dict['branch'] = "CSE"
#print(my_dict)

#my_dict.clear()
#print(my_dict)

#a=  input("Enter a number: ")
#b = input("Enter second number: ")
##print(a*b)
#print(type(a))

#>>>Typecasting<<<<<
#a=  int(input("Enter a number: "))
#b = int(input("Enter second number: "))
#print(a*b)

#lst = [1,2,6,8,5,58]
#print("this is my list",lst)
#print("type of list:",type(lst))
#tpl = tuple(lst)
#print("this is my tuple",tpl)
#print("type of tuple:",type(tpl))

##>>>>>>SET<<<<<<<<
#y_set = { 1,2,3,5,41,6,1,5,"Sidra"}
#print("this is my first set:",my_set)
#print("len of my set: ",len(my_set))
#print("my type of set:",type(my_set))
 
 #task>>>
#my_set.union()
#my_set.intersection()
#my_set.difference()

#lst=list(my_set)
#lst.append(1000)
#print(set(lst))



# Program 1: Find the Largest Number
#print("--- Find the Largest Number ---")
#num1 = float(input("Enter first number: "))
#num2 = float(input("Enter second number: "))
#num3 = float(input("Enter third number: "))

#largest = max(num1, num2, num3)
#print(f"The largest number is: {largest}")

# Program 2: Check Even or Odd
#print("\n--- Check Even or Odd ---")
#number = int(input("Enter an integer: "))
#if number % 2 == 0:
#    print(f"{number} is even")
#else:
#    print(f"{number} is odd")

# Program 3: Leap Year Checker
#print("\n--- Leap Year Checker ---")
#year = int(input("Enter a year: "))
#if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
 #   print(f"{year} is a leap year")
#else:
#    print(f"{year} is not a leap year")

#def calculate_grade(score):
 #   if score >= 90:
 #       return "A"
  #  elif score >= 75:
 #       return "B"
 #   elif score >= 60:
  #      return "C"
  #  else:
  #      return "D"

# Example usage:
#score = float(input("Enter your score: "))
#grade = calculate_grade(score)
#print(f"Your grade is: {grade}")

#Traffic Light System
#color = input("Enter the traffic light color (red, yellow, green): ").lower()

#if color == "red":
 #   print("Stop")
#elif color == "yellow":
#    print("Wait")
#elif color == "green":
##    print("Go")
#else:
 #   print("Invalid color")

#class BMICalculator:
 #   def __init__(self, weight, height):
  #      self.weight = weight  # in kilograms
 ##       self.height = height  # in meters

  #  def calculate_bmi(self):
   #     bmi = self.weight / (self.height ** 2)
   #     return bmi

   # def category(self):
   #     bmi = self.calculate_bmi()
   #     if bmi < 18.5:
   #         return "Underweight"
   #     elif 18.5 <= bmi < 24.9:
   #         return "Normal weight"
    #    elif 25 <= bmi < 29.9:
   #         return "Overweight"
    #    else:
    #        return "Obese"

# Example usage
##weight = float(input("Enter your weight in kg: "))
#height = float(input("Enter your height in meters: "))

#bmi_calculator = BMICalculator(weight, height)
#bmi = bmi_calculator.calculate_bmi()
#status = bmi_calculator.category()

#print(f"Your BMI is: {bmi:.2f}")
#print(f"Category: {status}")

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"\nYour current balance is ₹{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("\nDeposit amount must be positive.")
        else:
            self.balance += amount
            print(f"\n₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("\nWithdrawal amount must be positive.")
        elif amount > self.balance:
            print("\nInsufficient balance.")
        else:
            self.balance -= amount
            print(f"\n₹{amount} withdrawn successfully.")

    def run(self):
        print("=== Welcome to Python ATM ===")
        while True:
            print("\nPlease choose an option:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter choice (1/2/3/4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: ₹"))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: ₹"))
                self.withdraw(amount)
            elif choice == '4':
                print("\nThank you for using Python ATM!")
                break
            else:
                print("\nInvalid option. Please try again.")

# Create ATM instance and run
atm_machine = ATM(balance=5000)  # Starting balance ₹5000
atm_machine.run()
