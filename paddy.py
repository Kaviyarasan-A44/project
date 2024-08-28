#paddy story
#man gets 1 paddy on day1, and it will doubles the count on everyday for 64 days.
#how much paddy he may have on the 64th day.

#day = 1
#paddy = 1
#day = 2
#paddy = 2
#day = 3
#paddy = 4
#day = 4
#paddy = 16
#day = 5
#paddy = 32
#day = 6
#paddy = 64
#day = 7
#paddy = 128
#day = 8
#paddy = 256
#day = 9
#paddy = 512
#day = 10
#paddy = 1024 #and so on for 64 days

#python version


paddy = 1
day = 1 #we are performing multiplication, so value 1 is assigned

while day<=64:
#here day is increasing,untill it reaches day64,loop should be repeated.so we are assigning "<="

    paddy = paddy*2
    day = day+1
print(paddy)









