class car:
    company="Audi"
    def __init__(self,mil,price):
        self.mil=mil
        self.price=price
    
car1=car(20,2000000)
car2=car(30,30000000)
print(car1.company)
print(car2.company)

print(id(car1.company),id(car2.company))

car1.company="bmw"

print(id(car1.company),id(car2.company))
print(car1.company)
print(car2.company)

car.company="rollsroyce"

print(id(car1.company),id(car2.company))
print(car1.company)
print(car2.company)










# n=int(input())
# lst=input().split()
# for i in lst:
#     print(sum(list(map(int,[*i]))),end=" ")



# p="praveen"
# k=[*p]
# print(type(k),k)4



