def is_perfect_number(n):
    end = round(n / 2) + 1
    divisors_sum = 0

    for i in range(1, end):
        if n % i == 0:
            divisors_sum += i

    return divisors_sum == n


# print(is_perfect_number(28))


def collatz_sequence(n):
    print(n)
    num = n
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
        print(num)


# collatz_sequence(5)


def boring_numbers(n):
    str = format(n)

    for i in range(len(str) - 1):

        if str[i] != str[i + 1]:
            return False

    return True


# print(boring_numbers(666))


def lucky_number(n):
    str = format(n)
    odd_sum = 0
    even_sum = 0

    for i in range(len(str)):
        if i % 2 == 0:
            odd_sum += int(str[i])
        else:
            even_sum += int(str[i])

    return odd_sum == even_sum


# print(lucky_number(15224))


def interval_lucky_number(min, max):
    odd_lucky_numbers = []

    for num in range(min, max):
        if lucky_number(num) and num % 2 == 1:
            odd_lucky_numbers.append(num)

    return odd_lucky_numbers


# print(interval_lucky_number(200, 300))


def sorting(arr, str1):
    res = []

    for i in range(len(arr)):
        if str1 == 'desc':
            target = max(arr)
        else:
            target = min(arr)
        target_index = arr.index(target)
        res.append(target)
        arr.pop(target_index)
    print(res)


sorting([5, 2, 6], 'desc')
sorting([9, 2, 3], 'asc')


def task7(str1):
    arr = str1.split(' ')

    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()

    res = ' '.join(arr)
    return res


# print(task7('Hi bye hello politics'))


def polynomial(n):
    return 3 * (n ** 2) - n + 2


# print(polynomial(2))


def line_of_best_fit(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum([x[i] * y[i] for i in range(n)])
    sum_x_squared = sum([x[i] ** 2 for i in range(n)])
    x_bar = sum_x / n
    y_bar = sum_y / n

    m = (sum_xy - sum_x * sum_y / n) / (sum_x_squared - sum_x ** 2 / n)
    b = y_bar - m * x_bar

    rounded_m = m.__round__(2)
    rounded_b = b.__round__(2)

    return f'y = {rounded_m}x + {rounded_b}'


def my_max(x, y):
    return x if x >= y else y


# print(my_max(-2, -3))
