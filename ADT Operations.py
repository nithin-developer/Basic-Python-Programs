class date:

    def __init__(self,a,b,c):

        self.d = a
        self.m = b
        self.y = c

    def day(self):
        print("Day = ",self.d)

    def month(self):
        print("Month = ",self.m)

    def year(self):
        print("Year = ",self.y)

    def monthName(self):
        month = ["Unknown","January","Febuary","March","April","May","June","July","August","September","October","November","December"]
        print("Month Name = ",month[self.m])

    def isLeap(self):

        if(self.y % 400 == 0) and (self.y % 100 == 0):
            print("It is a Leap year!")

        elif(self.y % 4 == 0) and (self.y % 100 != 0):
            print("It is a Leap Year!")

        else:
            print("It is not a Leap Year!")

d = date(3,8,2000)
d.day()
d.month()
d.year()
d.monthName()
d.isLeap()
