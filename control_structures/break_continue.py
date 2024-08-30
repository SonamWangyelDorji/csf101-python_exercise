count = 0
while True:
    print(count)
    count += 1 
    if count >= 5:
        break
print('loop ended')
for num in range(1,6):
    if num % 2 == 0:
        continue 
    print(num)




numbers = [4, 2, 7, 1, 8, 3, 6]
search_no = 8
for num in numbers:
    if num == search_no:
        print(f"Found {search_no}")
        break
    print(f"Not {search_no}")



import random 
secret_number = random.randint(1,10)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 to 10: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
    elif guess< secret_number:
        print("Too low! Try Again")
    else:
        print("Too high! Try again")


def is_prime(n):
    if n < 2 : 
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
number = 17
if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")



