class Calculator:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def perform_operation(self):
        return self.num1 + self.num2 if self.operator == '+'\
               else  self.num1 * self.num2 if self.operator == '*'\
               else  self.num1 - self.num2 if self.operator == '-'\
               else  self.num1 / self.num2 if self.operator == '/'\
               else None

class AddMoreOperation(Calculator):
    def __init__(self, num1, num2, operator):
        Calculator.__init__(self, num1, num2, operator)

    def performOperations(self):
        return self.num1 % self.num2 if self.operator == '%'\
        else Calculator.perform_operation(self)


#calc = AddMoreOperation(20,6,'+')
#print(calc.performOperations())
import time
l_fact = lambda n: 1 if n ==0  else n * l_fact(n-1)

l_timestamp = lambda fnc, args: (time.time(), fnc(args), time.time())
l_timediff = lambda t0, retval, t1: t1 - t0
l_main = l_timediff(*l_timestamp(l_fact, 10))
print(l_main)
