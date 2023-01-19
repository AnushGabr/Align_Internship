def task1():
    colors = {'blue', 'pink', 'white', 'green'}
    # in the output we can see different ordered elements
    print(colors)

    # when we try to get element using indexes it will cause TypeError
    # print(s[0])

    # we can add elements in set so it's mutable
    colors.add('yellow')
    print(colors)


def task2():
    fav_country = {
        'name': 'Switzerland',
        'capital': 'Bern',
        'area': '41,285 km2 ',
        'driving side': 'right',
        'population': 8636896
    }


def task3():
    arr = []
    for i in range(0, 3):
        num = float(input('Enter number ... '))
        arr.append(num)
    arr.sort()
    index = int((len(arr) / 2))
    print('The median is', arr[index])


def task4():
    num = float(input("Input a dog's age in human years: "))
    final_age = 0
    while num - 2 > 0:
        final_age += 4
        num -= 1

    final_age += 2 * 10.5
    print(f"The dog's age in dog's years is {final_age}")


def task4_1():
    dog_age = float(input("Input a dog's age in human years: "))
    if dog_age <= 2:
        print(f'The dog\'s age in dog\'s years is {dog_age * 10.5}')
        return

    res = (dog_age - 2) * 4 + 21
    print(f'The dog\'s age in dog\'s years is {res}')


def task5():
    temp = input('Enter temperature ...')
    degree = float(temp[:-1])
    temp_type = temp[-1].lower()
    converted_temp = 0
    converted_temp_type = ''

    if temp_type == 'c':
        converted_temp = int(round((9 * degree) / 5 + 32))
        converted_temp_type = 'F'
    elif temp_type == 'f':
        converted_temp = int(round((degree - 32) * 5 / 9))
        converted_temp_type = 'C'
    else:
        print("Input proper convention.")
        return

    print(f"{temp} is {converted_temp} in {converted_temp_type} ")





def task6():
    my_country = {'name': 'Armenia',
                  'capital': 'Yerevan',
                  'population': 2850000,
                  'is_member_of_EU': False
                  }

    for key in my_country:
        print(key)
    # second option
    print(my_country.keys())


def task7():
    my_country = {'name': 'Armenia',
                  'capital': 'Yerevan',
                  'population': 2850000,
                  'neighboring_countries': ['Iran', 'Georgia', 'Turkey']
                  }

    # task-8

    for key in my_country:
        if key == 'religion':
            print(key)
    else:
        print('No religion is specified')


def task9():
    password = input('Enter your password: ')
    hyphen = '-'

    if len(password) < 8:
        print('Your password is less than 8 letters')
        return

    if hyphen not in password:
        print('Your password is invalid it is not containing "-" ')
        return
    elif password.isupper():
        print('Your password is invalid it contains only uppercase')
        return
    elif password.islower():
        print('Your password is invalid it contains only lowercase')





def task10():
    name = input('Enter your name: ')
    nation = input('Enter your nationality: ').lower()

    nation_dict = {'armenian': 'Բարև',
                   'georgian': 'Добрый день',
                   'russian': 'Добрый день',
                   }

    if nation in nation_dict:
        print(nation_dict[nation], name)
    else:
        print('Hello', name)


