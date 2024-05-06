import random 

def guess_number():
    #creating a number for user to guess
    secret_number = random.randint(1,100)
    #defining number of max attempts and initial attempts user has done
    attempts = 0
    maxattempt = 7
    print()
    print()
    print("------------------Welcome to the Guess the number game-------------------------")
    print()
    print(f"You have to guess the number in {maxattempt} attempts")
    print()
    
    #while loop is used to run the code until the max attempt is over or user has won
    while attempts < maxattempt:
        print()
        #taking guess from the user
        guess = int(input("Guess the nunmber : "))
        print()

        #chekcing if the number is smaller or greater
        if guess < secret_number:
            print("Too low!, Try larger number :)")
            print()
        elif guess > secret_number:
            print("Too High!, Try a smaller number :)")
            print()
        #breaing the loop if the user has won
        else:
            print()
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Congratulation you gussed the number right_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print()
            print(f"________________________________________THE NUMBER WAS {secret_number}___________________________________________")
            print()
            print("Game is automatically Closed")
            print()
            break
        #increasing number of attempts by one as the user attempts it
        attempts += 1 
        #checking how much attempt is left
        attempts_left = maxattempt - attempts
        #providing user the information that how much attempt is left
        print(f"{attempts_left}  Attempts left")

        #For the case where user has used all of thier attempt left

        if attempts == maxattempt:
            print("----------------!!-Game Over-!!---------------------")
            print()
            print(f"You have zero attempts left, the number was {secret_number}")
            print()
            print("Game is automatically Closed")
            print()
            break

def main():
    guess_number()
#try and except function to handle any unexpected error
try:
    if __name__=="__main__":
        main()
except:
    print("We were not ready for that :(")