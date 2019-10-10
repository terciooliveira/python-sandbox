__author__ = 'tércião'

name = input('Please, enter your name: ')

for i in range(10):
    greeting = 'Hello'
    # this is a comment
    print(greeting + ' ' + name, str(i))

print("String over\n\tmultiple lines\n\t\tthis is so cool")

strangeString = """String
    split over
        several lines"""

print(strangeString)

print("""Olha só que interessante, consigo usar aspas " ' " no meio sem problemas """)
