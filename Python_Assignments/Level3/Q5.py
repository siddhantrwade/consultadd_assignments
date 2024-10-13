class Time():

    def __init__(self, hours, minutes):

        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, other):
        
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        total_time = total_hours + total_minutes // 60

        # convert original time to less than 60 mins

        total_minutes %= 60

        return Time(total_hours, total_minutes)
    
    def display(self):

        print('Time is as follows:', self.hours,'hrs ',self.minutes,'mins')


    def displayTime(self):

        print(self.Hours,"Hrs ", self.minutes, 'Mins')

    def displayMinutes(self):

        total_mins = (self.hours * 60) + self.minutes
        print('Time elapsed in minutes: ', total_mins)

if __name__ == "__main__":
      
    time1 = Time(10, 26)  
    time2 = Time(4, 15)  

    # Adding two times using class
    time3 = time1.addTime(time2)

# execute all displays for times
   
    print("Time 1:")
    time1.display()
    
    print("Time 2:")
    time2.display()
    
    print("Sum of Time 1 and Time 2:")
    time3.display()

    print('Total mins')
    time3.displayMinutes()
