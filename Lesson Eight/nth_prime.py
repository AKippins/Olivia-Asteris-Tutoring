# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13. What is the 10 001st prime number?
import time

start_time = time.time()
target_prime = 10001
working_number = 2
found_primes = []
divisible_by_prime = False

while len(found_primes) != target_prime:
    for prime_number in found_primes:
        # print("Prime loop")
        if working_number % prime_number == 0:
            # Setting divisible by prime to True
            # print("Number is divisible by prime. Flipping boolean")
            divisible_by_prime = not divisible_by_prime
            break

    if divisible_by_prime:
        # Setting divisible by prime back to False
        # Number isn't prime since it's divisible by a found prime.
        divisible_by_prime = not divisible_by_prime
        working_number += 1

    for divisor in range(2, working_number + 1):
        if working_number == divisor:
            # Number is prime
            # print(str(working_number), "is prime")
            found_primes.append(working_number)
            # print("Found primes so far: ", found_primes)
        elif working_number % divisor == 0 and working_number != divisor:
            # Number isn't prime
            working_number += 1
            break

end_time = time.time()
runtime = end_time - start_time
print("Found primes were: ", found_primes)
nth_prime = found_primes[target_prime - 1]
print("The prime at position " + str(target_prime) + " is " + str(nth_prime))
print("Runtime came out to be:", runtime)