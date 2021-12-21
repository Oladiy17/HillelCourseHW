
a = input("введите номерной знак: ")

def hw_func(a):
    if len(a) == 8:
        return a[0:2], a[2:6], a[6:]
    else:
        return False

print(hw_func(a))

def num_func(a):
    m = 0
    for char in a:
        if char.isdigit():
            m += int(char)
    return f"The sum of numbers is: {m}"

print(num_func(a))