def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num -1) + fibonacci(num - 2)

# result = fibonacci(30)
# print(str(result))

def printfibsequence(n):
    for num in range(1,n):
        result = fibonacci(num)
        print(result)

printfibsequence(20)