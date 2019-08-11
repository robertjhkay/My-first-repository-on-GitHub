number = int(input("Enter a positive integer: "))


def fibonacci_seq(num):
    num_i1 = 0
    num_i2 = 1
    if num == 1:
        return 0
    elif num == 2:
        return 1
    elif num > 2:
        for x in range(num - 2):
            num_i2 = num_i2 + num_i1
            num_i1 = num_i2 - num_i1
        return num_i2


def fibonacci_sum(num):
    fibonacci_list = []
    for x in range(1, num + 1):
        fibonacci_list.append(fibonacci_seq(x))
    return sum(fibonacci_list)


print(fibonacci_sum(number))
