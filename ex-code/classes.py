# python object oriented programming

# class Employee:
#     pass
#
# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)
#
# emp_1.first = 'King'
# emp_1.last = 'OA'
# emp_1.email = 'king@oa.com'
# emp_1.income = 200000
#
# emp_2.first = 'Des'
# emp_2.last = 'OA'
# emp_2.email = 'des@oa.com'
# emp_2.income = 200000
#
# print(emp_1.email)
# print(emp_2.email)

# KEEP YOUR CODE DRY

class Employee:

    raise_amount = 1.04 #class variable

    def __init__(self, first, last, pay):
        self.fname = first
        self.lname = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@oa.com'

    def fullname(self): # self argument is req for it to run - without a TypeError
        print('FirstName:{} LastName:{} ContactEmail:{} Income:{}'.format(self.fname, self.lname, self.email, self.pay))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) # raise_amount variable has to be accessed from the class itself 'Employee' or the INSTANCE OF THE CLASS 'self' not just on

emp_1 = Employee('King', 'OA', 200000)
emp_2 = Employee('Des', 'OA', 200000)

# print(emp_1)
# print(emp_2)

# print(emp_1.email)
# print(emp_2.email)

# print('{} {}'.format(emp_1.fname, emp_1.lname)) # long to type and repetitive use a function above
# now print the fullname using the method inside Employee
# print(emp_1.fullname())
# print(emp_2.fullname())

emp_1.fullname()
# print(Employee.fullname(emp_1))
# Employee.fullname(emp_2) # class names can be used to call
