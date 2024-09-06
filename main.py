import pandas as pd
import csv
from data_entry import get_name_or_surname, get_age, get_salary, get_filter_type


class CSV:
    CSV_FILE = 'names.csv'
    COLUMNS = ['name', 'surname', 'age', 'salary']

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, name, surname, age, salary):
        data = {
            'name': name,
            'surname': surname,
            'age': age,
            'salary': salary,
        }
        with open(cls.CSV_FILE, 'a', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            csv_writer.writerow(data)
        print('Entry added successfully')

    @classmethod
    def get_filtered_text(cls, param, arg):
        with open(cls.CSV_FILE, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            param = param.lower()
            arg = (arg.lower()).title()

            if param == 'name':
                index = 0
            else:
                index = 1
            
            print(f'People with {param} {arg}:')
            for line in csv_reader:
                if line[index] == arg:
                    print(line)



    @classmethod
    def get_filtered_number(cls, param, filter_type, arg):
        with open(cls.CSV_FILE, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            param = param.lower()
            arg = int(arg)

            if param == 'age':
                index = 2
            else:
                index = 3

            if filter_type == 'M':
                print(f'People with {param} higher than {arg}:')
                for line in csv_reader:
                    if int(line[index]) > arg:
                        print(line)
            elif filter_type == 'L':
                print(f'People with {param} lower than {arg}:')
                for line in csv_reader:
                    if int(line[index]) < arg:
                        print(line)
            elif filter_type == 'E':
                print(f'People with {param} equal to {arg}:')
                for line in csv_reader:
                    if int(line[index]) == arg:
                        print(line)



def pause_for_user():
    input("\nPress Enter to continue...")


def add():
    CSV.initialize_csv()
    name = get_name_or_surname('name')
    surname = get_name_or_surname('surname')
    age = get_age()
    salary = get_salary()
    CSV.add_entry(name, surname, age, salary)


def get_filtered_data():
    print('Enter parameter: Name | Surname | Age | Salary ')
    param = (input('Choice: ')).lower()

    if param == 'name' or param == 'surname':
        arg = get_name_or_surname(param)
        CSV.get_filtered_text(param, arg)

    elif param == 'age':
        filter_type = get_filter_type()
        arg = get_age()
        CSV.get_filtered_number(param, filter_type, arg)

    elif param == 'salary':
        filter_type = get_filter_type()
        arg = get_salary()
        CSV.get_filtered_number(param, filter_type, arg)

    else:
        print('Invalid parameter')
        return


def main():
    while True:
        print ('\nWhat would you like to do?')
        print('1. Add new person')
        print("2. Filter people by parameter")
        print('3. Exit')
        choice = input("Enter your choice: ")
        if choice == '1':
            add()
            pause_for_user()
        elif choice == '2':
            get_filtered_data()
            pause_for_user()
        elif choice == '3':
            print('Exiting...')
            break
        else:
            print('Incorrect choice. Choose numbers 1,2 or 3')

if __name__ == '__main__':
    main()
