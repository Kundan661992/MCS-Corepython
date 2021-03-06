"""
class structure
    # 1. Fields  - STATE
         class variables    - at class level,when state is shared among objects
         instance variables - at instance level, inside init method.
                              When each object required separate data
             local variables- inside init method/all other methods

    # 2. Methods - BEHAVIOR
         class method       - cls parameter,which works only on class variables
         instance method    - self parameter,which works on only instance variables
                                                            both instance,class variables
                                                            only class variables XX
        static method       - generic method

"""


class Employee:
    e_count = 0
    office = 'ORACLE'

    @classmethod
    def get_edata(cls):
        # print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)

    '''
    def __init__(self):
        pass
    '''


# no need to create object to call class methods
Employee.get_edata()  # Employee.get_edata(Employee)

# 2 way - Don't do it
obj = Employee()
print("Object address : ", obj)
obj.get_edata()  # ==> Employee.get_edata(obj)

print("------All methods---------")


class Employee:
    e_count = 0
    office = 'ORACLE'

    def __init__(self, eid, name, sal):
        self.eid = eid
        self.name = name
        self.sal = sal
        Employee.e_count += 1

    @classmethod
    def get_edata(cls):
        # print("Employees info : ",Employee.e_count,Employee.office)
        print("Employees info : ", cls.e_count, cls.office)

    def get_empinfo(self):
        print("Employee details : ", self.eid, self.name, self.sal)
        Employee.get_edata()
        # self.get_edata()


# to call class method
Employee.get_edata()
# to call instance method
ali = Employee(101, 'Ali Hussain', 15000)
ali.get_empinfo()
ali.get_edata()
Employee.get_edata()

print("-----static method--------")


# i want a behavior which neither deals with class variables nor instance variables

class Employee:
    @staticmethod
    def getinfo():
        print("Static method implementation")


Employee.getinfo()

'''
class Employee:
    1. STATE
    ----------
    # class variables
    # instance variables ==> init method

    2. BEHAVIOR
    -------------
    # class method      : works only on class variables 
    # instance method   : works only on instance variables 
                          works on both instance,class variables 
    # static method     : neither on class nor on instance variables 
'''
print(".......................................")


class Dog:
    def __init__(self, sound):
        self.sound = sound

    def bark(self):
        print("The dog makes the sound:", self.sound)


d1 = Dog("Bow Bow")
d1.bark()

print("...........................")


class Inst:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, My name is ", self.name)


i1 = Inst('Ali')
i1.introduce()

print('.................................................')


class Student:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def show(self):
        print('Name:', self.name, 'Age:', self.age)

    # static method
    @staticmethod
    def percentage(sub1, sub2):
        print('Percentage:', (sub1 + sub2) / 2)


emma = Student('Emma', 14)
emma.show()
emma.percentage(67, 62)
