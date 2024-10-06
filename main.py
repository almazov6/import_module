import datetime
import art

from application import salary
from application.db import people

if __name__ == '__main__':
    date_now = datetime.date.today()
    print(f'Текущая дата: {date_now}')
    salary.calculate_salary()
    people.get_employees()
    print(art.text2art("NETOLOGY", font='small'))