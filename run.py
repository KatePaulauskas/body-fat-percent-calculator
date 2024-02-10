import gspread
from google.oauth2.service_account import Credentials
import datetime
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('body-fat-percent-calculator')

def get_measurements_date():
    """
    Request the user to input the date, when measurements were taken
    """

    print('Welcome to Body Fat Percent Calculator')
    while True:
        print('Enter the date measurements were taken in the following format DD/MM/YYYY')

        date_measurements_taken = input('Enter date here:\n')

        if validate_date(date_measurements_taken):
            print('Date is valid!\n')
            # Exit the loop after validating the date
            break

    # Return the validated date       
    return date_measurements_taken

def validate_date(value):
    """
    Validate the date is entered in the correct format.
    Raise ValueError if date is not entered in the correct format
    Source: https://www.tutorialspoint.com/How-to-do-date-validation-in-Python
    """

    date_format = '%d/%m/%Y'

    try:
        datetime.datetime.strptime(value, date_format)
        return True

    except ValueError:
        print("Incorrect date format. Try again")
        return False


date = get_measurements_date()

def get_user_name():
    """
    Request the user to input their name
    """

    while True:
        print('Enter your name. You can use letters, hyphens, apostrophes, and spaces (where appropriate)')

        user_name = input('Enter your name here:\n')

        if validate_user_name(user_name):
            print('Name is valid!\n')
            # Exit the loop after validatign the name
            break

    return user_name


def validate_user_name(name):
    """
    Validate user name entry contains only letters, hyphens, apostrophes, and spaces
    Raise error message if the name was not entered in the required format
    Sources: https://stackoverflow.com/questions/28495822/best-way-to-validate-a-name-in-python, https://docs.python.org/3/howto/regex.html
    """
    pattern = r"^[a-zA-Z][a-zA-Z' -]+$"
    if re.match(pattern, name):
        return True
    else:
        print("Invalid name. Please ensure it contains only letters, hyphens, apostrophes, and spaces (where appropriate).")
        return False

user_name = get_user_name()
