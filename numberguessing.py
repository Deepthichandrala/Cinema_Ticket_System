import random
secret_number = random.randint(1, 50)
    
print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 50. Can you guess it?")
num_guesses = 0
while True:
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        if guess == secret_number:
            print("Congratulations! You guessed the number in {} guesses.". format (num_guesses))
            break
        elif guess>secret_number and guess <=100:
        
            if guess>secret_number and (guess-secret_number) <5:
                print("Nearer to the number!,Try again.")
            else:
                print("Too high! Try Agin")    
        elif guess<secret_number and guess >=0:
            if guess<secret_number  and (secret_number-guess) <5:
                print("Nearer to the number!,Try again.")
            else:
                print("Too low!,Try again")
        else:
            print("Invalid number!,Try again.")

