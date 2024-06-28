import random

#print(guess)
count = 0

while True:
    print("WELCOME:")
    secretnumber = random.randint(1, 10)
    while count <= 2:
        guess = int(input("Please Guess the Secret_Number Between 1 and 10: "))

        match guess:
            case _ if guess < secretnumber:
                print("Your Guess is LOWER_THAN the Secret_Number")
            case _ if guess == secretnumber:
                print("Congratulation, YOUR GUESS IS CORRECT")
                print(f"You have guess {count+1} times")
                count = 0
                break
            case _ if guess > secretnumber:
                print("Your Guess is HIGHER_THAN then Secret_Number")
        count +=1
        if count > 2:
            print(f"You've Attempted {count} Times, Please Try Again")
            print(f"The secret number is: {secretnumber}")
            count = 0
            break
    if int(input("Do you want to Play Again? 1 -> yes and 2 -> no ")) != 1:
        break
