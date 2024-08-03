import random


top_of_Range = input("Type a number: ")

if top_of_Range.isdigit():
    top_of_Range = int(top_of_Range)
    
    if top_of_Range <=0:
        print("Please type a number larger than 0 next time.")
        quit()

else:
    print("Please type a number next time.")

x = random.randint(0,top_of_Range)
print(x)

guesses = 0 

while True:
    guesses += 1
    user_guess = input("Type a numbers: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Enter only the number ")
        continue

    if user_guess == top_of_Range:
        print("Matched :)")
        break

    else:
        print("InMatched :(")  
        
        
          
print("you guessed it in", guesses)













