"""
 class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student", self.name)

    def get_marks(self):
        return self.marks

s1 = Student("Sahil", 98)
s1.welcome()
print(s1.get_marks)
 """

""" s2 = Student("Divya")
print(s2.name)  """


# bank account

# 2 __ se private ho jata hai

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("56459", "abcde")

print(acc1.acc_no)
print(acc1.__acc_pass)


