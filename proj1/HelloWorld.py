__author__ = 'tércião'

name = __author__ #input('Please, enter your name: ')

for i in range(10):
    greeting = 'Hello'
    # this is a comment
    print(greeting + ' ' + name, str(i))

print("String over\n\tmultiple lines\n\t\tthis is so cool")

strangeString = """String
    split over
        several lines"""

print(strangeString)

tripleAspas = """Olha só que interessante, consigo usar aspas "_'_" no meio sem problemas"""

print(tripleAspas)

print(tripleAspas[:6])
print(tripleAspas[6:])

print(tripleAspas[-4:-2])

print(tripleAspas[0::2])


numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

print("eita " * 10)

print("A Mariana tem " + str(5+2) + " anos!")

print("A Mariana tem {0} anos de idade".format(5+2))

print("A Mariana tem %d anos de idade e é uma pessoa muito %s" % (7, "legal"))

print("""Era {0} {2} 
{1} 
{0}""".format("uma", "eita", "vez"))
