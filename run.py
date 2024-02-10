import gspread
from google.oauth2.service_account import Credentials
import datetime

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
    Raise error message if the name input was not in the text format
    Source: https://stackoverflow.com/questions/28495822/best-way-to-validate-a-name-in-python
    """

    while True:
        print('Enter your name in a text format')

        user_name = input('Enter your name here:\n')

        if user_name.isalpha():
            print('Name is valid!\n')
            return user_name
        else:
            print('Invalid input. Please enter text only.')


user_name = get_user_name()

