class car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax()

    def printall(self):
        print 'price is $' + str(self.price)
        print 'speed is:' + str(self.speed)
        print 'fuel:' + str(self.fuel)
        print 'mileage:' + str(self.mileage)
        print 'tax:' + str(self.tax)

    def tax(self):
        if self.price >= 10000:
            self.tax = .15
        else: self.tax = .12

car1 = car(20000, '30mph', 'empty', '30mpg')
car1.printall()
car2 = car(9300, '20mph', 'full', '47mpg')
car2.printall()