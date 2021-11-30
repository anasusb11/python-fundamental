trying = 0
secret_number = 9
limit = 3

while trying < limit:
    guess = input("Guess the number (1-9): ")
    guess = int(guess)
    
    if guess == secret_number:
        print("Congrats, you win")
        break
    trying += 1
