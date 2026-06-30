# Generate a random number
# loop
# Ask the user to make a guess
# If not a valid number
#   print an error
# if number < guess
#   print too low
# If number > guess
#   print too high
# Else
#   print well done
import random
best_score = None
while True:
    number_to_guess = random.randint(1, 100)
    count = 0
    while True:
        try:
            guess = int(input("Enter the number for Guess (1-100) "))
            difference = abs(number_to_guess - guess)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
                continue
            count += 1
            if guess < number_to_guess:
                if difference <= 5:
                    print("Very close!")
                elif difference <= 10:
                    print("Close!")
                elif difference <= 20:
                    print("Not Too far")
                else:
                    print("Way too low")
                
            elif guess > number_to_guess:
                if difference <= 5:
                    print("Very close!")
                elif difference <= 10:
                    print("Close!")
                elif difference <= 20:
                    print("Not Too far")
                else:
                    print("Way too high")
            else:
                print("Congratulation!")
                print(f"you guessed the number in {count} attempts")

                if best_score is None:
                    best_score = count
                elif count < best_score:
                    best_score = count
                break
        except ValueError:
            print("Please Enter a valid number")
    again_play = input("Play again? Y/N ").lower()
    if again_play == "y":
        continue
    else:
        print("Thanks for playing")
        if best_score is not None:
            print(f"Your best score in all games is {best_score}")
        break
