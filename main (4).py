

def fact_rec(n):
  if n==0 or n==1:
     return 1
  else:
    return n* fact_rec(n-1)
number=int(input("enter a value"))  
res=fact_rec(number)
print("the factroial of {}is{}.".format(number,res))



def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0)or year % 400 == 0:
    return True
  else:
    return False
year = int(input("enter a year:"))  
if isLeapYear(year):
  print('{}is a leap year.'.format(year))
else:
  print('{} is not a leap year.'. format(year))

# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

#Define the base class playerclass player:
class player:
  def player(self):
    print("The player is playing cricket.")

#Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The Batsman is batting.")

#Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object 
batsman.play()
bowler.play(Program :1

def fact_rec(n):
  if n==0 or n==1:
     return 1
  else:
    return n* fact_rec(n-1)
number=int(input("enter a value"))  
res=fact_rec(number)
print("the factroial of {}is{}.".format(number,res))


program:2

def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0)or year % 400 == 0:
    return True
  else:
    return False
year = int(input("enter a year:"))  
if isLeapYear(year):
  print('{}is a leap year.'.format(year))
else:
  print('{} is not a leap year.'. format(year))

program:3
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s = Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

program  4:
#Define the base class playerclass player:
class player:
  def player(self):
    print("The player is playing cricket.")

#Define the derived class Batsman
class Batsman(player):
  def play(self):
    print("The Batsman is batting.")

#Define the derived class Bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

#create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object 
batsman.play()
bowler.play(