class bike(object):
    def __init__(self,price,max_speed): 
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def info(self):
        print 'Price is: $' + str(self.price)
        print 'Max speed: ' + str(self.max_speed) + 'mph'
        print 'Total miles: ' + str(self.miles) + ' miles'
        return self 
    def drive(self):
        print 'Driving'
        self.miles += 10
        return self 
    def reverse(self):
        print 'Reversing'
        # prevent negative miles
        if self.miles >= 5:
            self.miles -= 5
        return self 
bike1 = bike(200, "25mph")
bike1.drive().reverse().info();
bike2 = bike(300, "12 mph")
bike2.drive().reverse().info();
bike3 = bike(100,"1mph")
bike3.drive().reverse().info();

