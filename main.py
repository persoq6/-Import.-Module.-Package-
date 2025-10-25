from application.salary import calculate_salary
from application.DB.people import get_employees
from datetime import datetime


if __name__ == "__main__":
    get_employees()
    calculate_salary()
    print(datetime.today())
print(__name__)