class Calculator:
    def add(self,x,y):
        return x + y
    def sub(self,x,y):
        return x - y
    def mul(self,x,y):
        return x * y
    def div(self,x,y):
        if y !=  0:
            return x/y
        else:
            return "Cannot Divided by Zero"
calc=Calculator()
result=calc.add(4,3)        
print("x + y=",result) 

result=calc.sub(10,3)
print("x - y:",result)

result=calc.mul(7,1)
print("x * y:",result)

result=calc.div(49,7)
print("x / y:",result)