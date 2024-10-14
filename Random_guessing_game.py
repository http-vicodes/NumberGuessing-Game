import random
def generate_random_number():
  return random.randint(1, 10)

random_number = generate_random_number()



def guess_number(number):
  if number == random_number:
    return "Congratulations! You guessed it right."
  else:
    return "Wrong guess. Try again."



for i in range(3):
  guessed_number = int(input("Guess a number between 1 to 10: "))
  result = guess_number(guessed_number)
  if i < 2 and guessed_number != random_number:
    print(result)
  elif i <= 2 and guessed_number == random_number:
    print(result)
    break
  else:
    print(result)
    print(f"Sorry, you've run out of guesses. The number is: ", random_number)
    break