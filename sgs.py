class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating....")
    def sleep(self):
        print(f"{self.name} is sleeping...")
class prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing....")
class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting....")
class Rabbit(prey):
    pass
class Hwak(predator):
    pass
class Fish(prey, predator):
    pass

rabbit = Rabbit("Fardin")
hawk = Hwak("Amit")
fish = Fish("Atied")

rabbit.flee()
rabbit.eat()
rabbit.sleep()



