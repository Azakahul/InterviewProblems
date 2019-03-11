def fizzbuzz(n, m):
    for num in range (n, m):
        if num % 3 == 0 and num & 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# fizzbuzz(1, 21)

def fizzbuzzconcat(n, m):
    for num in range (n, m):
        fizzbuzz = ""
        if num % 3 == 0:
            fizzbuzz = fizzbuzz + "Fizz"
        if num % 5 == 0:
            fizzbuzz = fizzbuzz + "Buzz"
        if num % 5 != 0 and num % 3 != 0:
            fizzbuzz = fizzbuzz + str(num)
        print(fizzbuzz)

fizzbuzzconcat(1,21)
