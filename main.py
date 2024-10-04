from random import choices, shuffle
from string import ascii_letters, digits

SYMBOLS = '!@#$%^&*()'


def main():
    print('Welcome to the PyPassword Generator!')
    letters = int(input('How many letters would you like in your password?: '))
    symbols = int(input('How many symbols would you like?: '))
    numbers = int(input('How many numbers would you like?: '))

    password = []
    add_characters(password, ascii_letters, letters)
    add_characters(password, SYMBOLS, symbols)
    add_characters(password, digits, numbers)
    shuffle(password)

    print(f'Here\'s your password: {"".join(password)}')


def add_characters(password, char_group, frequency):
    password.extend(choices(char_group, k=frequency))


if __name__ == '__main__':
    main()
