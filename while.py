#1 1 1 1 1

#print(1, end=" ")
#print(1, end=" ")
#print(1, end=" ")
#print(1, end=" ")
#print(1, end=" ")

num = 1
count = 1
while count<=5:
    print(num, end=" ")
    count = count+1
print(end="\t")

#   \t is used to create intendation of the value to be printed
#   end=" ", its used to get the result in the same line, and we can give any input between the double quotes. Here we have assigned a space

#--------------------------------------------

#1 2 3 4 5
num = 1
count = 1
while count<=5:
    print(num, end=" ")
    num = num+1
    count = count+1
print(end="\t")

#--------------------------------------------

#1 3 5 7 9
num = 1
count = 1
while count<=5:
    print(num, end=" ")
    num+=2
    count+=1
print(end="\t")

#---------------------------------------------

#2 4 6 8 10
num = 2
count = 1
while count<=5:
    print(num, end=" ")
    num+=2
    count+=1
print(end="\t")


#----------------------------------------------

#3 6 9 12 15
num = 3
count = 1
while count<=5:
    print(num, end=" ")
    num+=3
    count+=1
print(end="\t")

#------------------------------------------------

#1 2 3 4 5 
#3 6 9 12 15
#1 4 9 16 25
#1 8 27 64 125

num = 1
count = 1
while count<=5:
    print(num**3, end=" ")
    num = num+1
    count = count+1
print(end="\t")

#------------------------------------------------

#1 3 5 7 9 2 4 6 8 10

num = 1
count = 1
while count<=10:
    print(num, end=" ")
    num+=2
    count+=1
    if num==11:
        num=2
        print(num, end=" ")
        num+=2
        count+=1
print(end="\t")

#--------------------------------------------------

#7 10 8 11 9 12 ?


#num = 7
#count = 1
#print(num, end=" ")
#num+=3
#print(num, end=" ")
#num-=2
#print(num, end=" ")
#num+=3
#print(num, end=" ")
#num-=2
#print(num, end=" ")
#num+=3


num = 7
count = 1
while count<=7:
    print(num, end=" ")
    num+=3
    count+=1
    print(num, end=" ")
    num-=2
    count+=1
print(end="\t")













    









































































