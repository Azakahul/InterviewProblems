# How do you swap two numbers without using the third variable?
def swaptwovalues(firstX, secondY):
    x = firstX
    y = secondY
    x = x + y
    y = x - y
    x = x - y

    print("After swap, x = ", x, " y = ", y)

swaptwovalues(7, 10)