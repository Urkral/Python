class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def next_second(self): 
        self.seconds += 1

    def prev_second(self):
        self.seconds -= 1

    def display_timer(self):
        if self.hours or self.minutes or self.seconds >= 10:
            print(self.hours,":",self.minutes,":",self.seconds)
        elif self.hours or self.minutes or self.seconds <= 10:
            print("0",self.hours,":","0",self.minutes,":","0",self.seconds)



timer1 = Timer(hours = 4, minutes=5,seconds=9)
timer1.display_timer()
timer1.next_second()
timer1.display_timer()
