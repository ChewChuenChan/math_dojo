# Create a MathDojo class
class MathDojo:
    def __init__(self):
        self.result=0
    
# Write the add method and test it by calling it 3 times
# with different numbers of arguments each time
    def add(self, num, *nums):
        # print(f"{num}  {nums}")
        sum=0
        # self.result=0
        for index in nums:
            sum = sum + index
        self.result = self.result + num + sum
        # print(self.result)
        return self
        
    def subtract(self,num,*nums):
        sum =0
        # self.result =0
        for index in nums:
            sum = sum + index
        self.result = self.result - num - sum
        # print(self.result)
        return self



# create an instance:
md=MathDojo()

# Testing add method by calling it 3 times
# with different numbers of arguments each time
# md.add(1)
# md.add(1,2)
# md.add(1,2,3)

# Testing subtract method by calling it 3 times
# with different numbers of arguments each time
# md.subtract(2)
# md.subtract(2,1)
# md.subtract(6,2,3)

x= md.add(2).add(2,5,1).subtract(3,2).result
print(x)