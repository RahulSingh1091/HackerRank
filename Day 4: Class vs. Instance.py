t = int(raw_input())
for i in range(0, t):
    age = int(raw_input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()        
    p.amIOld()
    print("")
    
    
    class Person:
    def __init__(self,initialAge):
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
        else:
            
            self.age = initialAge
            
    def amIOld(self):
        if self.age>=18:
            print("You are old.")
        elif self.age>=13:
            print("You are a teenager.")
        else:
            print("You are young.")
    def yearPasses(self):
        self.age +=1
