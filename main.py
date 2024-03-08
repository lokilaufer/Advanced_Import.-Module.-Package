import datetime
import db.salary as salary
import db.people as people

if __name__ == '__main__':
    current_date = datetime.datetime.now()
    print(f'Current date: {current_date}')

    salary.calculate_salary()
    people.get_employees()
