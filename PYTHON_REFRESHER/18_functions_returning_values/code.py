def add(x,y):
    return x+y
def divide(dividend, divisor):
    if divisor != 0:
        return int(dividend / divisor)
    else:
        return "divisor must be != 0"

print(add(5,5))
print(divide(5,0))