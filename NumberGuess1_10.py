import random
integer1 = random.randint(1,10)
user_number = 0
number_guesses = 1
#The setup of having the randomly generated number and an open number for the user to begin guessing 
# and a counter to count the number of guesses starting at 1 since they will at least need 1 try. 
while user_number != integer1:
    user_number = int(input("Insert a Number Between 1-10 \nNote: If You Wanna Give Up Type 0:\n"))
    if user_number == integer1:
        print("Congrats You've Guessed the Generated Number:",integer1,"\n You guessed it in",number_guesses,"tries")
        break
    if user_number == 0:
        print("You Gave :(")
        break
# I had these as conditions played after the checks to continue the while loop of the number not being guessed 
    print("Try Again")
    number_guesses += 1
