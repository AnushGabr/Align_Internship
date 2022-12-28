# task - 1;
print('Hello! This is my first Align_internship')

# task-2

if 5 % 2 == 0:
    print(True)
else:
    print(False)

# task-3

print('Հին աշխարհքը ամեն օր,')
print('    Հազար մարդ է մտնում նոր,')
print('        Հազար տարվա փորձ ու գործ')
print('             Ըսկսվում է ամեն օր։')

# version-2

print('''
Հին աշխարհքը ամեն օր,
\tՀազար մարդ է մտնում նոր,
\t\tՀազար տարվա փորձ ու գործ'
\t\t\tԸսկսվում է ամեն օր։
''')

# task-4

word = 'education'

print(word.upper())
print(word.lower())
print(word[0].upper() + word[1:])

# task-5

sentence = "The world is a copy of a copy of a copy"

if 'The' in sentence:
    print(sentence.index('The'))

newSentence = sentence.replace('The', 'This')
print(newSentence)

# task-6

name = "Anush"

# task-7

carname = 'BMW'

# task-8

year = 2015

# task-9

string = f'{name}, has a {carname} since, {year}'
print(string)

# task-10

side = 4.6

volume = 4.6 ** 3
print(volume)

# task-11

num1 = 5
num2 = 5.2
str1 = 'abc'
is_boolean = True

print(type(num1))
print(type(num2))
print(type(str1))
print(type(is_boolean))

# task-12

high_income = True
high_credit = False

if high_income and high_credit:
    print(True)
else:
    print(False)

# task-13

classmates_names = ['Ani', 'Mari', 'Tigran', 'Tatev', 'Aram']
classmates_names.append('Lilit')
index = len(classmates_names) - 1
print('Welcome ' + classmates_names[index])

# task-14

places = ["Italy", "France", "USA", "Germany", "Sweden"]

# 14.a
print(len(places))

# 14.b
places.sort()
print(places)

# 14.c

joined_places = ','.join(places)
new_places_str = joined_places.replace('Italy', "London")
new_places_list = new_places_str.split(',')

print(new_places_list)

# 14.d
places.pop()

# 14.e
if 'Madrid' in places:
    places.remove('Madrid')
else:
    places.insert(2, 'Madrid')
print(places)

# task-15

new_tuple = (1, 2, 3)
tuple_1 = tuple([4, 'f', 'a', 5])
tuple_2 = 'a', 5, 6

tuple_container = []

tuple_container.append(new_tuple)
tuple_container.append(tuple_1)
tuple_container.append(tuple_2)

tuple_container[1] = 'a'
print(tuple_container)
