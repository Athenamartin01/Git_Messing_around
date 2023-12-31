class student:
    '''
    Used to create and manipulate studetn class objects.
    contains the following methods:
    def avg_score(scr1,scr2,scr3) - used to find the average scores of the student

    '''
    def __init__(self,age:int,group:str,name:str='student') -> None:
        '''assigns all the attributes to the object
        '''
        self.name = name
        self.age = age
        self.group = group

    def avg_score(self,scr1:float,scr2:float,scr3:float) -> None:
        '''
        Takes the 3 scores the student obtained, and outputs tthe mean average score of the 3
        as an integer value
        '''
        print(f"{self.name} scored and average of {(scr1+scr2+scr3)//3}")
    
athena = student(22,'AMS - Awesomely Masterful Students','Athena')
athena.avg_score(1,1133,135)



class Budget:

    def __init__(self,category,amount):
        self.category = category
        self.amount = amount
    
    def deposit(self,amount):
        if amount >= 0: 
            self.amount += amount
            print(f"£{amount} deposited into {self.category}")

    def withdraw(self,amount):
        if amount >= 0:
            if amount > self.amount:
                print("Unable to withdraw, not enough funds.")
            else:
                self.amount -= amount
                print(f"£{amount} withdrawn from {self.category}")
    
    def transfer(self,other,amount):
        if amount > self.amount:
            print("Not enough funds to transfer")
        else:
            self.withdraw(amount)
            other.deposit(amount)
            
    


food = Budget("Food",121.12)
rent = Budget("Rent", 1290.91)

food.deposit(101.2)
rent.withdraw(20000)
rent.withdraw(100)

food.transfer(rent,152)


#####Polygon

class Rectangle:
    
    def __init__(self,height,width):
       self.height = height
       self.width = width

    def area(self):
       return(self.width * self.height)
   
    def perim(self):
       return(2*(self.width + self.height))

class Square(Rectangle):
    
    def __init__(self,height):
        self.height = height
        self.width = height


r1 = Rectangle(3,4)
s1 = Square(2)

print(s1.area())
print(r1.area())
print(s1.perim())
print(r1.perim())



######Clock
class Clock:
    def __init__(self,hour,minute,second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self._organise()
    
    def __str__(self):
        return(f'{self.hour}:{self.minute}:{self.second}')
    
    def tick(self):
        self.second += 1
        self._organise()

    def _organise(self):
        while (self.second >= 60) or (self.minute >= 60):
            if self.second == 60:
                self.second -= 60
                self.minute += 1
            if self.minute == 60:
                self.minute -= 60
                self.hour += 1

class Hr12clock(Clock):

    def _orangise(self):
        Clock._organise(self)
        while self.hour >= 12:
            self.hour -= 12
    def tick(self):
        self.second +=1
        self._orangise()

######LotteryBall

import random
class LotteryBall:
    
    def __init__(self,no_col:dict):
        self.no_col = no_col
    
    def total(self):
        return(sum(self.no_col[i] for i in self.no_col))
    
    def out_of_hat(self):
        total_balls = self.total()
        amount_taken = random.randint(0,total_balls)
        balls_left = self.no_col
        colours = list(i for i in self.no_col)
        balls_taken = {}

        for i in range(amount_taken):
            rng_num = random.randint(0,len(balls_left)-1)
            balls_left[colours[rng_num]] -= 1

            if not(colours[rng_num] in balls_taken):
                balls_taken[colours[rng_num]] = 0
            
            balls_taken[colours[rng_num]] += 1

            if balls_left[colours[rng_num]] == 0:
                del(balls_left[colours[rng_num]])
                
        
        print(f"no. of balls taken: {amount_taken} \nballs taken: {balls_taken} \nballs remaining{balls_left}")




Lotto1 = LotteryBall({"Red":3,"Yellow":7})
Lotto1.out_of_hat()