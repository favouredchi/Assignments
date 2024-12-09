# class is the parent
# attributes are the variable in the class
# methods are the functions written in the class

#abstraction define reuseable terms in other documents
# polymorphism blends with every new environment like a module, modularization
# inheritance just the name sounds 
# encapsulation bundling data into one single unit

# class car
    #width
    #height
    #color
    #engine_type
    #brand
    #model
    #year

#   def window
#   def doors

#       def model x
#       def model y
#       def model 3

# simple calculator class
#calculator.substract(2,1,4)

class Calculator:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add(self, num4):
        return self.num1 + self.num2 + self.num3 + num4


    def substract(self, num5, num6):
        return num5 + num6

    def substract(self):
        return self.num1 - self.num2

    def  multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


doris_calc = Calculator(2, 3, 4)
obinna_calc = Calculator(5, 6, 7)
chioma_calc = Calculator(8, 9, 10)
mofe_calc = Calculator(10, 11, 15)

print(doris_calc.add(5))