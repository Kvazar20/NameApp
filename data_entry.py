import csv


def get_name_or_surname(name_type: str):
    name = input(f'Enter {name_type}: ')

    if all(char.isalpha() or char in {" ", "-", "'"} for char in name):
        return name
    else:
        print(f'{name_type} cannot contain special characters')
        return get_name_or_surname(name_type)


def get_age():
    age = input('Enter age: ')
    if age.isdigit():
        age = int(age)
        if 0 < age < 130:
            return age
        else:
            print('Incorrect age. Age must be >0 and <130.')
    else:
        print('Incorrect age. Age must be a number.')

    return get_age()


def get_salary():
    salary = input('Enter salary: ')
    if salary.isdigit():
        salary = int(salary)
        if 0 < salary < 500:
            return salary
        else:
            print('Salary must be between 0 and 500')
    else:
        print('Salary must be a number')

    return get_salary()


def get_filter_type():
    print("Enter filter_type: 'M' - more than arg |  'L' - less than arg  |  'E' - equals arg")
    filter_type = (input("Choice:")).upper()
    if filter_type in ('M', 'L', 'E'):
        return filter_type
    else:
        print('Invalid filter type')
        return get_filter_type()