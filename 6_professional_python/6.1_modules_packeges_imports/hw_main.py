from application.db.hw_people import get_employees
from application.hw_salary import calculate_salary
from datetime import date
import pandas as pd
import openpyxl

if __name__ == '__main__':
    current_date = date.today()
    print(current_date)
    calculate_salary()
    get_employees()
    print()
    df = pd.read_excel('data.xlsx')
    print(df)
