
def task1():
    info = input('Imagine you have a car. Tell me what to do with it. If you are a new user, enter "help" ')
    i = info.lower().strip()
    if i == 'help':
        print(""""\n* Enter start - to start the ride\n* Enter stop  - to stop the ride\n * Enter quit  - to quit the ride""")
        choose_option = input('Please enter start, stop or quit')
        l =choose_option.lower().strip()
        if l == 'start':
            print("Car started, ready to go")
        elif l == 'stop':
            print("Car stopped")
        else:
            print("Game ended")

task1()

def task2():

    num = int(input("Please enter number"))
    sum = 0
    for x in range(1, num + 1): #if number include num +1 else just num
        sum += x

    print(sum)

task2()

def task3():
    odd = [1, 3, 5, 7, 9]
    even = [0, 2, 4, 6, 8]
    odd.extend(even)
    even.clear() # or even = []
    print(even)
    del(even)
    print(odd)


task3()

def task4():
    arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9], [10, 11, 12]]
    arr1 = []
    arr1.append(arr[1][1])
    arr1.append(arr[1][2])
    print(arr1)

    arr2 = []
    arr3 = []
    list = []
    arr2.append(arr[0][-2])
    arr2.append(arr[0][-1])
    arr3.append(arr[1][0])
    arr3.append(arr[1][1])
    list.append(arr2)
    list.append(arr3)
    print(list)
    list2 = []
    list2.append(arr[0][-1]), list2.append(arr[0][-2])
    list2.append(arr[0][-3])
    list2.append(arr[1][-1]), list2.append(arr[2][0])
    print(list2)
    for x in arr:
        x.reverse()

    arr.reverse()
    print(arr)
task4()



def task5():
    arr1 = [2, 4, 6, 8, 10]
    print("These are even numbers " + f'{arr1}')

    arr2 = arr1
    sum = 0
    average = 0
    for x in arr2:
        sum += x

    average = sum / len(arr1)
    print(average)
    index_3 = arr2.pop(2)
    print(index_3)

    arr3 = [3, 5, 7, 9, 11]

    arr2.extend(arr3)
    arr2.sort()
    print(arr2)

task5()
def task6():
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    list2.reverse()
    print(list1 == list2)


task6()
def task7(num):
    first_element = 0
    second_element = 1
    count = 0

    while count < num:
        print(first_element)
        nth_element = first_element + second_element
        first_element = second_element
        second_element = nth_element
        count += 1


task7(50)

def task8():
    list1 = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
    index = list1.index(13)
    print("There is a 13 at index no:", f'{index}')


task8()
def task9():
    emoji = {':(': '😔', ':)': '😃 '}
    str = input('Enter your text: ')
    arr = str.split()
    res = ''
    for el in arr:
        if el in emoji:
            res += emoji.get(el)
        else:
            res += el
        res += ' '
    print(res)
task9()