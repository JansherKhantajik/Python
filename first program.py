#print a program which input number from user and you will give 5 guess to equvalate with your answer

print("Word of Guess Number, Input Your Guess that You have five chance")
guess = int(input())
i=0

while (True):
 if (guess <15):
     print("Please Enter more then",guess)
     break
 elif guess <20 and guess >15:
     print("little More then",guess)
 elif guess <35 and guess >25:
     print("Enter less then",guess)
 elif guess <25 and guess >20:
      print("Congurate You Have Got it Number is Between 20 to 25 .. your guess ",guess)
 else:
     print("Invelid number")

 i=i+1
 break