# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def get_avg(self):
#         sum =0
#         for i in self.marks:
#             sum+=i
#         print("hi", self.name,"your avg marks is ",sum/3)
# s1=Student("shamique Khan",[99,98,97])
# print(s1.name,s1.marks)
# s1.get_avg()
#_----------------------------------------------------------------
class Account:
    def __init__(self,bal,acc):
        self.bal =bal
        self.acc =acc
    def debit(self,ammount):
        self.bal-=ammount
        print("rs", ammount,"was debited")
        print("total balance = ", self.get_bal())
    def credit(self,ammount):
        self.bal+=ammount
        print("rs", ammount,"was credited")
        print("total balance = ", self.get_bal())
    def get_bal(self):
        return self.bal
    
acc1=Account(100000,12345)
# print(acc1.bal)
# print(acc1.acc)
acc1.debit(1000)
acc1.credit(500)
