""" 
# 1. student record
class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"hi {self.name} your avg score is {sum/n}")

# print("your list is: ", l)
# s1 = Student("Sahil", [92, 98, 89])

m= int(input("enter no. of students: "))

n = int(input("enter no. subjets: "))

for stu in range(m):
    name = input("enter name of student: ")

    marks = []

    for i in range(n):
        x= int(input("enter marks of each subject: "))
        marks.append(x)
    s1 = Student(name, marks)
    s1.avg() 

 """ 
# 2. bank record

class Account():
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit methord 
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs {amount} was debited")
        print("Total Balance = ", self.get_balance())

    #credit methord
    def credit(self, amount):
        self.balance += amount
        print(f"Rs {amount} was credited")
        print("Total Balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc_no = int(input("Enter your account no.: "))
balance = int(input("Enter balance of your account: "))
deb = int(input("Enter account deducted from your account : "))
cred = int(input("Enter account creditted in your account : "))

# acc1 = Account(10000, 123456)
acc1 = Account(balance, acc_no)
acc1.debit(deb)
acc1.credit(cred)
