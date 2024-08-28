#palindrome_number
#if the given number and reverse number both are same it is palindrome.

num = 545
num2 = num 
rev = 0 #sum of digits
while num>0:
    rem = num%10
    rev = (rev*10) + rem
    num = num//10 
#after reaching 5, value stored in num is "0", because in every loop num value is breaking. After 5, there is no digit is there. so for a comparison with rem value, we are storing num value as num2 initially.
print(rev)

if num2 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

