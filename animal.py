class animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 5
        return self
    def run(self):
        self.health -= 5
        return self 
    def status(self):
        print 'name' + str(self.name)
        print 'health' + str(self.health)
        return self
class dog(animal):
    def __init__ (self,name):
        self.name = name
        self.health = 150
    def doghealth(self): 
        self.health += 5
        return self
class dragon(animal):
    def __init__(self,name):
        self.name = name
        self.health = 170      
    def fly(self):
        self.health -= 10
        return self
    def show(status):
        print 'I am a dragon' + str(self.name)
        return self

# animal1 = animal('joe')
# animal1.walk().walk().walk().status().run().run().status()
dog1=dog('roger')
dog1.run().status().run
# dragon1=dragon('james')
# dragon1.status()

        