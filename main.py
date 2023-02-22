from random import choices, shuffle
from string import ascii_letters, digits

SYMBOLS = '!@#$%^&*()'


def main():
    print('Welcome to the PyPassword Generator')
    letters = int(input('How many letters would you like in your password: '))
    symbols = int(input('How many symbols would you like: '))
    numbers = int(input('How many numbers would you like: '))

    password = []
    password.extend(choices(ascii_letters, k=letters))
    password.extend(choices(SYMBOLS, k=symbols))
    password.extend(choices(digits, k=numbers))
    shuffle(password)

    print(f'Here\'s your password: {"".join(password)}')


if __name__ == '__main__':
    main()
